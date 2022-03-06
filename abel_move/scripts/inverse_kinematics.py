from __future__ import print_function
 
import numpy as np
from numpy.linalg import norm, solve
 
import pinocchio
 
model, collision_model, visual_model = pinocchio.buildModelsFromUrdf("/home/gabriele/catkin_ws/src/abel_move/scripts/abel_arms_full.urdf")
data, collision_data, visual_data  = pinocchio.createDatas(model, collision_model, visual_model)
 
JOINT_ID = 5
oMdes = pinocchio.SE3(np.eye(3), np.array([-0.19, 0.50, -0.38]))

q      = pinocchio.neutral(model)
eps    = 1e-2
IT_MAX = 1000
DT     = 1e-4
damp   = 1e-12

i=0
while True:
    pinocchio.forwardKinematics(model,data,q)
    dMi = oMdes.actInv(data.oMi[JOINT_ID])
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

print('\nresult: %s' % q.flatten().tolist())
print('\nfinal error: %s' % err.T)