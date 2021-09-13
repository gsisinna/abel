from __future__ import print_function

#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from dynamixel_workbench_msgs.msg import DynamixelState, DynamixelStateList
from dynamixel_workbench_msgs.srv import DynamixelCommand, DynamixelCommandRequest
from std_msgs.msg import Header


#Import all the class attributes, methods and gestures class
from modules.AbelMove import *
from modules.AbelGesture import *

abel = AbelMove()
gesture = AbelGesture()

import os
import rbdl
import pinocchio

import numpy as np
from numpy.linalg import norm, solve

class MoveAbelArms(object):
    def __init__(self):
        #Create the object for Abel
        abel = AbelMove()
        gesture = AbelGesture()   


    def safety_check(self):
        """
        Check joint values for a safe initialization
        """
        ## creare thread e gestione continua in loop
        # da sistemare per il check su motori 8,10,13,15 # LAB

        biceps_l = abel.joint_states_msg.position[7]
        forearm_l = abel.joint_states_msg.position[9]
        biceps_r = abel.joint_states_msg.position[12]
        forearm_r = abel.joint_states_msg.position[14]

        safety_data = [biceps_l, forearm_l, biceps_r, forearm_r]

        rospy.loginfo(safety_data)

        if (biceps_l < -2.5 or biceps_l > 2):
            rospy.loginfo("Attenzione, bicipite in zona di instabilita. Riposizionamento sicuro ...")
            gesture.neutral_high(10)

    def initialize(self):
        """
        Initializiation of Abel joint controller, safety check and neutral pose.
        """
        rospy.loginfo("AbelMove INIT...Please wait")

        # rospy.loginfo("Launching Dynamixel Controller...")
        # os.system("roslaunch dynamixel_workbench_controllers dynamixel_controllers.launch")
        # rospy.sleep(3)
        
        rospy.loginfo("Checking joints for stability...")
        self.safety_check()

        gesture.neutral_high(5) 
        rospy.sleep(5)

        rospy.loginfo("AbelMove Ready!")

    def direct_kinematics(self):
        """
        Compute the direct kinematics for left and right hand (end-effector) by using the URDF model
        """
        q = self.abel.joint_states_msg.position
        q = np.asarray(q)

        pos_left = rbdl.CalcBodyToBaseCoordinates(self.model, q, 6, np.zeros(3))
        pos_right = rbdl.CalcBodyToBaseCoordinates(self.model, q, 12, np.zeros(3))
        rospy.loginfo("Posizioni end-effector: sx = "+pos_left+" dx = "+pos_right)

    def inverse_kinematics(self, x, y, z):
        """Calculate the joint values for a desired cartesian position"""
        model = pinocchio.buildModelFromUrdf("/home/gabriele/catkin_ws/src/abel_move/scripts/abel_arms_full.urdf")
        data  = model.createData()

        JOINT_ID = 10
        pose_des = pinocchio.SE3(np.eye(3), np.array([x, y, z]))

        q = pinocchio.neutral(model)

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

        rospy.loginfo(q)

        point = JointTrajectoryPoint()
        point.positions = [  0,0,0,0,0,
                            q[0],q[1],q[2],q[3],q[4],
                            q[5],q[6],q[7],q[8],q[9] ]

        abel.move_all_joints(point)

        print('\nresult: %s' % q.flatten().tolist())
        print('\nfinal error: %s' % err.T)
        

if __name__ == "__main__":
    rospy.init_node('MoveAbelArms', log_level=rospy.DEBUG)
    rate = rospy.Rate(10)
