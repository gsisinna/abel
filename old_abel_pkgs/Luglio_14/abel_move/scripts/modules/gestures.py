#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from dynamixel_workbench_msgs.msg import DynamixelState, DynamixelStateList
from dynamixel_workbench_msgs.srv import DynamixelCommand, DynamixelCommandRequest
from std_msgs.msg import Header

from .AbelMove import *

#Create the object for abel
abel = AbelMove()

#  joints = [ neck_1, neck_2, neck_3, neck_4, neck_5,
#             shoulder_l1, shoulder_l2, biceps_l, elbow_l, forearm_l, 
#             shoulder_r1, shoulder_r2, biceps_r, elbow_r, forearm_r ]

def neutral_pose(duration):
    """ Neutrale"""
    joint_position_home = JointTrajectoryPoint()
    joint_position_home.positions = [0,   -0.25,   0.25, -0.25, 0.25, 
                                    -0.5, -0.2,    0,     0.75, 0, 
                                     0.5,  0.2,    0,    -0.75, 0]

    joint_position_home.time_from_start = rospy.Duration(duration)
    abel.move_all_joints(joint_position_home)

def neutral_high(duration):
    """ Neutrale, braccia alte per configurazione bicipite senza collisioni """
    joint_position_home = JointTrajectoryPoint()
    joint_position_home.positions = [0, -0.25, 0.25, -0.25, 0.25, 
                                     0.5, 0.9,  0.25,  0,  0.25, 
                                    -0.5, -0.9, -0.25, -0.75, 0]

    joint_position_home.time_from_start = rospy.Duration(duration)
    abel.move_all_joints(joint_position_home)

def zero_pose(duration):
    """Zero joints"""
    joint_position_zero = JointTrajectoryPoint()
    joint_position_zero.positions = [0, -0.25, 0.25, -0.25, 0.25, 
                                     0,  0,    0,     0,    0, 
                                     0,  0,    0,     0,    0]

    joint_position_zero.time_from_start = rospy.Duration(duration)
    abel.move_all_joints(joint_position_zero)

def mano_pose(duration):
    """ Stretta di mano """
    joint_position_hand = JointTrajectoryPoint()
    joint_position_hand.positions = [0, -0.25, 0.25, -0.25, 0.25, 
                                     -0.22549518942832947, -0.010737866163253784, -1.4434759616851807, 0.9295923709869385, 1.274738073348999, 
                                     -0.8943108320236206, 0.10737866163253784, 0.9449321627616882, 0.2684466540813446, -0.4663301706314087]

    joint_position_hand.time_from_start = rospy.Duration(duration)
    abel.move_all_joints(joint_position_hand)

def hug_pose(duration):
    """Abbraccio"""
    joint_position_hug = JointTrajectoryPoint()
    joint_position_hug.positions = [0,   -0.25,   0.25, -0.25, 0.25, 
                                    1.9173012399673462, 0.8482913970947266, -0.3037281930446625, -0.07976700365543365, 0.5568350553512573, 
                                    -1.418932318687439, -0.771592378616333, 0.35895150899887085, 0.5322913527488708, -0.5016117095947266]

    joint_position_hug.time_from_start = rospy.Duration(duration)
    abel.move_all_joints(joint_position_hug)
    

def hello_pose(duration):
    """Saluto"""
    joint_position_hello = JointTrajectoryPoint()
    joint_position_hello.positions = [0, 0, 0, 0, 0, 
                                      1, 1.57, 0.75, -0.75, 0, 
                                      1, 1.57, 0.75, -0.75, 0]

    joint_position_hello.time_from_start = rospy.Duration(duration)
    abel.move_all_joints(joint_position_hello)

def neck_zero(duration):
    """Zero joints"""
    joint_position_zero = JointTrajectoryPoint()
    joint_position_zero.positions = [0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0]

    joint_position_zero.time_from_start = rospy.Duration(duration)
    abel.move_all_joints(joint_position_zero)

def neck_up(duration):
    """Zero joints"""
    joint_position_zero = JointTrajectoryPoint()
    joint_position_zero.positions = [-0.003067961661145091, 0.15186409652233124, -0.3604854941368103, -0.5645049214363098, 0.8774370551109314, 
                                     0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0]

    joint_position_zero.time_from_start = rospy.Duration(duration)
    abel.move_all_joints(joint_position_zero)

def neck_down(duration):
    """Zero joints"""
    joint_position_zero = JointTrajectoryPoint()
    joint_position_zero.positions = [0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0]

    joint_position_zero.time_from_start = rospy.Duration(duration)
    abel.move_all_joints(joint_position_zero)

def neck_right(duration):
    """Zero joints"""
    joint_position_zero = JointTrajectoryPoint()
    joint_position_zero.positions = [0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0]

    joint_position_zero.time_from_start = rospy.Duration(duration)
    abel.move_all_joints(joint_position_zero)

def neck_left(duration):
    """Zero joints"""
    joint_position_zero = JointTrajectoryPoint()
    joint_position_zero.positions = [0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0]

    joint_position_zero.time_from_start = rospy.Duration(duration)
    abel.move_all_joints(joint_position_zero)

def up_right_arm(duration):
    """Zero joints"""
    joint_position_zero = JointTrajectoryPoint()
    joint_position_zero.positions = [0,   -0.25,   0.25, -0.25, 0.25, 
                                     0.37582531571388245, 0.14879614114761353, -2.7243499755859375, 0.8084079027175903, 0.26998063921928406, 
                                     -1.522335815429688, -1.0753206014633179, 0.452524334192276, 0.7900001406669617, -1.3]

    joint_position_zero.time_from_start = rospy.Duration(duration)
    abel.move_all_joints(joint_position_zero)


def movement_sequence_test(time):
    """Perform a simple sequence of movement for testing and debugging"""    
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

    ## Inserire test collo ##


if __name__ == "__main__":
    rospy.init_node('gestures', log_level=rospy.DEBUG)

