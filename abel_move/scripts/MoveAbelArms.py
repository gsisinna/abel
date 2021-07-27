from __future__ import print_function
#!/usr/bin/env python3

import rospy

from abel_move.AbelGesture import AbelGesture
from abel_move.AbelMove import AbelMove

from dynamixel_workbench_msgs.msg import DynamixelState, DynamixelStateList
from dynamixel_workbench_msgs.srv import (DynamixelCommand,
                                          DynamixelCommandRequest)
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

abel    = AbelMove()
gesture = AbelGesture()

import os

import numpy as np
import pinocchio
from numpy.linalg import norm, solve


class MoveAbelArms(object):
    def __init__(self):   
        self.model    = pinocchio.buildModelFromUrdf("/home/gabriele/catkin_ws/src/abel_move/scripts/abel_arms_full.urdf")

    def safety_check(self):
        """
        Check joint values for a safe initialization
        """
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
        """Initializiation of Abel joint controller, safety check and neutral pose."""
        rospy.loginfo("*** AbelMove Initialization ***")
        
        rospy.loginfo("Checking joints for stability...")
        self.safety_check()

        gesture.neutral_high(5) 
        rospy.sleep(5)

        rospy.loginfo("AbelMove Ready!")

    def direct_kinematics(self):
        """
        Compute the direct kinematics for left and right hand (end-effector) by using the URDF model
        """
        
        # Create data required by the algorithms
        model, collision_model, visual_model = pinocchio.buildModelsFromUrdf("/home/gabriele/catkin_ws/src/abel_move/scripts/abel_arms_full.urdf")
        data, collision_data, visual_data  = pinocchio.createDatas(model, collision_model, visual_model)

        q = pinocchio.neutral(self.model)

        pinocchio.forwardKinematics(model,data,q)

        for name, oMi in zip(self.model.names, data.oMi):
            print(("{:<24} : {: .2f} {: .2f} {: .2f}".format( name, *oMi.translation.T.flat )))

    def inverse_kinematics(self, x, y, z):
        """Calculate the joint values for a desired cartesian position"""
        model, collision_model, visual_model = pinocchio.buildModelsFromUrdf("/home/gabriele/catkin_ws/src/abel_move/scripts/abel_arms_full.urdf")
        data, collision_data, visual_data  = pinocchio.createDatas(model, collision_model, visual_model)
 
        JOINT_ID = 10
        oMdes = pinocchio.SE3(np.eye(3), np.array([x,y,z]))

        q      = pinocchio.neutral(model)
        eps    = 1e-1
        IT_MAX = 1000
        DT     = 1e-1
        damp   = 1e-3

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

    def collision_check():
        """Controllo collisioni basato su cinematica diretta"""
        ## creare thread e gestione continua in loop

        q = abel.joint_states_msg.position[5:14]
        #self.direct_kinematics()
        
        

if __name__ == "__main__":
    rospy.init_node('MoveAbelArms', log_level=rospy.DEBUG)
    rate = rospy.Rate(10)
