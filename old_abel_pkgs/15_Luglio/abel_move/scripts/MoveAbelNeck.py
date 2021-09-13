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

import os

class MoveAbelNeck(object):
    def __init__(self):
        #Create the object for Abel
        abel = AbelMove()
        gesture = AbelGesture()

    def look_xy(self, x, y):
        """ Questa funzione dovrà convertire un punto del piano frontale in un movimento del collo"""


    def neck_zero(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_zero)

    def neck_neutral(self, duration):
        """Neutral (visual)"""
        self.joint_position_neutral = JointTrajectoryPoint()
        self.joint_position_neutral.positions = [0.003067961661145091, -0.39576706290245056, 0.2929903268814087, -0.43411657214164734, 0.8590292930603027, 
                                     0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0]

        self.joint_position_neutral.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_neutral)

    def neck_up(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [-0.003067961661145091, 0.15186409652233124, -0.3604854941368103, -0.5645049214363098, 0.8774370551109314, 
                                     0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_zero)

    def neck_down(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [0.00920388475060463, -0.5921165943145752, 0.5276893973350525, 0.5399612784385681, -0.13192234933376312, 
                                              0, 0, 0, 0, 0, 
                                              0, 0, 0, 0, 0]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_zero)

    def neck_rotate_right(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [-0.6166602969169617, -0.1733398288488388, -0.5491651296615601, -0.48166999220848083, 0.2316311001777649, 
                                              0, 0, 0, 0, 0, 
                                              0, 0, 0, 0, 0]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_zero)

    def neck_rotate_left(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [0.630466103553772, -0.010737866163253784, 0.1702718734741211, -0.1672039031982422, 0.8283496499061584, 
                                              0, 0, 0, 0, 0, 
                                              0, 0, 0, 0, 0]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_zero)



    def neck_sequence_test(self, time):
        """Perform a simple sequence of movement for testing and debugging"""
        self.gesture.neck_neutral(time)
        rospy.sleep(time)

        self.gesture.neck_up(time)
        rospy.sleep(time)

        self.gesture.neck_neutral(time)
        rospy.sleep(time)

        self.gesture.neck_down(time)
        rospy.sleep(time)

        self.gesture.neck_neutral(time)
        rospy.sleep(time)

        self.gesture.neck_rotate_right(time)
        rospy.sleep(time)

        self.gesture.neck_neutral(time)
        rospy.sleep(time)

        self.gesture.neck_rotate_left(time)
        rospy.sleep(time)

        self.gesture.neck_neutral(time)
        rospy.sleep(time)


if __name__ == "__main__":
    rospy.init_node('MoveAbelNeck', log_level=rospy.DEBUG)

    #AbelGesture.neck_sequence_test(5)

    ##TEST CAPTURE POSITION##
    #AbelMove.capture_position_neck(10)

    ## TEST COMPLIANCE ##
    #AbelMove.set_joints_compliance(95)

    ##TEST CURRENT LIMIT##
    #AbelMove.set_joints_current(95)

    ##TEST VELOCITY AND ACCELERATION --> GESTURE.PY ##
    #AbelMove.set_joints_velocity(50)
    #AbelMove.set_joints_acceleration(50)
