from __future__ import print_function
from AbelMove import *

import numpy as np
from numpy.linalg import norm, solve

import pinocchio

abel = AbelMove()

model = pinocchio.buildModelFromUrdf("/home/gabriele/catkin_ws/src/abel_move/scripts/abel_arms_full.urdf")
data  = model.createData()

JOINT_ID = 10
pose_des = pinocchio.SE3(np.eye(3), np.array([0.2, 0.5, 0]))

q      = pinocchio.neutral(model)
eps    = 1e-1
IT_MAX = 1000
DT     = 1e-1
damp   = 1e-2

i=0
while True:
    pinocchio.forwardKinematics(model,data,q)
    dMi = pose_des.actInv(data.oMi[JOINT_ID])
    err = pinocchio.log(dMi).vector
    if norm(err) < eps:
        success = True
        break
    if i >= IT_MAX:
        success = False
        break
    J = pinocchio.computeJointJacobian(model,data,q,JOINT_ID)
    v = - J.T.dot(solve(J.dot(J.T) + damp * np.eye(6), err))
    q = pinocchio.integrate(model,q,v*DT)
    if not i % 10:
        print('%d: error = %s' % (i, err.T))
    i += 1

if success:
    print("Convergence achieved!")
else:
    print("\nWarning: the iterative algorithm has not reached convergence to the desired precision")

q = q.flatten().tolist()

point = JointTrajectoryPoint()
point.positions = [  0,0,0,0,0,
                   q[0],q[1],q[2],q[3],q[4],
                   q[5],q[6],q[7],q[8],q[9] ]

abel.move_all_joints(point)

print('\nresult: %s' % q.flatten().tolist())
print('\nfinal error: %s' % err.T)
