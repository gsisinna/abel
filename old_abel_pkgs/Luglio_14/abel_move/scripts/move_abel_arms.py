#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from dynamixel_workbench_msgs.msg import DynamixelState, DynamixelStateList
from dynamixel_workbench_msgs.srv import DynamixelCommand, DynamixelCommandRequest
from std_msgs.msg import Header

import os
import rbdl
import numpy as np
from numpy.linalg import inv
from numpy.linalg import norm
from numpy import matmul
from numpy.random import random

#Create the kinematics chain model by using the URDF
model = rbdl.loadModel("/home/gabriele/catkin_ws/src/abel_move/scripts/abel_arms_full.urdf")

#Import all the class attributes, methods and gestures library
from modules.AbelMove import *
from modules.gestures import *

#Create the object for Abel
abel = AbelMove()


#  joints = [ neck_1, neck_2, neck_3, neck_4, neck_5,
#             shoulder_l1, shoulder_l2, biceps_l, elbow_l, forearm_l, 
#             shoulder_r1, shoulder_r2, biceps_r, elbow_r, forearm_r ]

def safety_check():
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
        neutral_high(10)

def initialize():
    """
    Initializiation of Abel joint controller, safety check and neutral pose.
    """
    rospy.loginfo("AbelMove INIT...Please wait")

    # rospy.loginfo("Launching Dynamixel Controller...")
    # rospy.sleep(3)
    # os.system("roslaunch dynamixel_workbench_controllers dynamixel_controllers.launch")
    
    rospy.loginfo("Checking joints for stability...")
    safety_check()
    neutral_high(5) 

    rospy.sleep(3)
    rospy.loginfo("AbelMove Ready!")

def direct_kinematics():
    """
    Compute the direct kinematics for left and right hand (end-effector) by using the URDF model
    """
    q = abel.joint_states_msg.position
    q = np.asarray(q)

    pos_left = rbdl.CalcBodyToBaseCoordinates(model, q, 6, np.zeros(3))
    pos_right = rbdl.CalcBodyToBaseCoordinates(model, q, 12, np.zeros(3))
    rospy.loginfo("Posizioni end-effector: sx = "+pos_left+" dx = "+pos_right)

def inverse_kinematics():
    """Calculate the joint values for a desired cartesian position"""
    ### MoveIT + URDF###


if __name__ == "__main__":
    rospy.init_node('move_abel_arms', log_level=rospy.DEBUG)
    
    #initialize()
    rospy.sleep(3)
    neutral_high(10)
    #neutral_pose(5)
    #zero_pose(5)
    #mano_pose(5)
    #hug_pose(5)
    #up_right_arm(5)
    
    #abel.send_command(14, 'Torque_Enable', 1)
    
    #movement_sequence_test(5)

    ##TEST CAPTURE POSITION##
    #abel.capture_position_arms(5)
    #abel.capture_position_neck(5)

    ## TEST COMPLIANCE ##
    #abel.set_joints_compliance(95)

    ##TEST CURRENT LIMIT##
    #abel.set_joints_current(95)

    ##TEST VELOCITY AND ACCELERATION --> GESTURE.PY ##
    #abel.set_joints_velocity(50)
    #abel.set_joints_acceleration(50)

    ## LOOP: rospy.spin() ##

