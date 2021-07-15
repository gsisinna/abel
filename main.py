#!/usr/bin/env python3

##Invocare tutto e gestione dei topic fra i vari nodi
## Creare topic per interagire con i nodi

# /abel_move/arms/gesture (lista e esecuzione)
# /abel_move/arms/gesture/save

# /abel_move/neck/gesture
# /abel_move/neck/gesture/save
# /abel_move/neck/lookat

import rospy
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from dynamixel_workbench_msgs.msg import DynamixelState, DynamixelStateList
from dynamixel_workbench_msgs.srv import DynamixelCommand, DynamixelCommandRequest
from std_msgs.msg import Header

import os
import rbdl
import numpy as np

#Import all the class attributes, methods and gestures class
from modules.AbelMove import *
from modules.AbelGesture import *
from MoveAbelArms import *
from MoveAbelNeck import *

#Create the objects
abel = AbelMove()
gesture = AbelGesture()
arms = MoveAbelArms()
neck = MoveAbelNeck()



if __name__ == "__main__":
    rospy.init_node('main', log_level=rospy.DEBUG)
    rate = rospy.Rate(10)

    arms.initialize()
    rospy.sleep(3)

    gesture.neutral_high(5)
    rospy.sleep(5)
    
    gesture.movement_sequence_test(5)
    neck.neck_sequence_test(5)

    ##TEST CAPTURE POSITION##
    #abel.capture_position_arms(10)
    #abel.capture_position_neck(10)

    ## TEST COMPLIANCE ##
    #abel.set_joints_compliance(95)

    ##TEST CURRENT LIMIT##
    #abel.set_joints_current(95)

    ##TEST VELOCITY AND ACCELERATION --> GESTURE.PY ##
    #abel.set_joints_velocity(50)
    #abel.set_joints_acceleration(50)

    rospy.spin()
