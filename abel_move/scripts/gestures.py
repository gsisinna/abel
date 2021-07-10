#!/usr/bin/env python3

from math import pi
import rospy
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from dynamixel_workbench_msgs.msg import DynamixelState, DynamixelStateList
from dynamixel_workbench_msgs.srv import DynamixelCommand, DynamixelCommandRequest
from std_msgs.msg import Header

from AbelMove import *
abel_obj = AbelMove()

#  joints = [ neck_1, neck_2, neck_3, neck_4, neck_5,
#             shoulder_l1, shoulder_l2, biceps_l, elbow_l, forearm_l, 
#             shoulder_r1, shoulder_r2, biceps_r, elbow_r, forearm_r ]

def neutral_pose(duration):
    # Neutrale
    joint_position_home = JointTrajectoryPoint()
    joint_position_home.positions = [0, 0, 0, 0, 0, 
                                    -0.5, -0.2, 0, 0.75, 0, 
                                    -0.5, -0.2, 0, 0.75, 0]

    joint_position_home.time_from_start = rospy.Duration(duration)

    abel_obj.move_all_joints(joint_position_home)

def neutral_high(duration):
    # Neutrale, braccia alte per configurazione bicipite senza collisioni
    joint_position_home = JointTrajectoryPoint()
    joint_position_home.positions = [0, 0, 0, 0, 0, 
                                     0.5, 0.75, 0, 0.75, 0, 
                                     0.5, 0.75, 0, 0.75, 0]

    joint_position_home.time_from_start = rospy.Duration(duration)

    abel_obj.move_all_joints(joint_position_home)

def zero_pose(duration):
    # Zero joints
    joint_position_zero = JointTrajectoryPoint()
    joint_position_zero.positions = [0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0]

    joint_position_zero.time_from_start = rospy.Duration(duration)

    abel_obj.move_all_joints(joint_position_zero)

def mano_pose(duration):
    joint_position_hand = JointTrajectoryPoint()
    joint_position_hand.positions = [0, 0, 0, 0, 0, 
                                     0.9, -0.2, -0.75, -0.2, 0.5, 
                                     0.9, -0.2, -0.75, -0.2, 0.5]

    joint_position_hand.time_from_start = rospy.Duration(duration)

    abel_obj.move_all_joints(joint_position_hand)

def hug_pose(duration):
    # Abbraccio
    joint_position_hug = JointTrajectoryPoint()
    joint_position_hug.positions = [0, 0, 0, 0, 0, 
                                    1.57, 1.25, -1, 0.7, 1, 
                                    1.57, 1.25, -1, 0.7, 1]

    joint_position_hug.time_from_start = rospy.Duration(duration)

    abel_obj.move_all_joints(joint_position_hug)
    

def hello_pose(duration):
    # Saluto
    joint_position_hello = JointTrajectoryPoint()
    joint_position_hello.positions = [0, 0, 0, 0, 0, 
                                      1, 1.57, 0.75, -0.75, 0, 
                                      1, 1.57, 0.75, -0.75, 0]

    joint_position_hello.time_from_start = rospy.Duration(duration)

    abel_obj.move_all_joints(joint_position_hello)


def movement_sequence_test(time):    
    neutral_high(time)
    rospy.sleep(time)

    neutral_pose(time)
    rospy.sleep(time)

    mano_pose(time)
    rospy.sleep(time)

    hug_pose(time)
    rospy.sleep(time)

    hello_pose(time)
    rospy.sleep(time)

    neutral_pose(time)
    rospy.sleep(time)


if __name__ == "__main__":
    rospy.init_node('gestures', log_level=rospy.DEBUG)

