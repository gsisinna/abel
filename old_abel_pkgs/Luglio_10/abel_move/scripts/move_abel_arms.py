#!/usr/bin/env python3

from math import pi
import rospy
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from dynamixel_workbench_msgs.msg import DynamixelState, DynamixelStateList
from dynamixel_workbench_msgs.srv import DynamixelCommand, DynamixelCommandRequest
from std_msgs.msg import Header

from AbelMove import *
from gestures import *

#Create the object for Abel
abel_obj = AbelMove()


#  joints = [ neck_1, neck_2, neck_3, neck_4, neck_5,
#             shoulder_l1, shoulder_l2, biceps_l, elbow_l, forearm_l, 
#             shoulder_r1, shoulder_r2, biceps_r, elbow_r, forearm_r ]

def safety_check():
    
    # da sistemare per il check su motori 8,10,13,15 #

    biceps = abel_obj.joint_states_msg.position[0]
    rospy.loginfo(biceps)
    if biceps < -2.5 or biceps > 2:
        rospy.loginfo("Attenzione, bicipite in zona di instabilita. Riposizionamento sicuro ...")
        neutral_high(10)

def initialize():
        rospy.loginfo("AbelMove INIT...Please wait")
        rospy.loginfo("Checking joints for stability...")
        
        # safety_check()

        rospy.loginfo("AbelMove Ready!")

def set_joints_torque(state):
    #Set 1 to enable the torque, 0 otherwise
    if state == 1:
        abel_obj.send_command(6, 'Torque_Enable', 1 )
        abel_obj.send_command(7, 'Torque_Enable', 1 )
        abel_obj.send_command(8, 'Torque_Enable', 1 )
        abel_obj.send_command(9, 'Torque_Enable', 1 )
        abel_obj.send_command(10, 'Torque_Enable', 1 )
        abel_obj.send_command(11, 'Torque_Enable', 1 )
        abel_obj.send_command(12, 'Torque_Enable', 1 )
        abel_obj.send_command(13, 'Torque_Enable', 1 )
        abel_obj.send_command(14, 'Torque_Enable', 1 )
        abel_obj.send_command(15, 'Torque_Enable', 1 )
    else:
        abel_obj.send_command(6, 'Torque_Enable', 0 )
        abel_obj.send_command(7, 'Torque_Enable', 0 )
        abel_obj.send_command(8, 'Torque_Enable', 0 )
        abel_obj.send_command(9, 'Torque_Enable', 0 )
        abel_obj.send_command(10, 'Torque_Enable', 0 )
        abel_obj.send_command(11, 'Torque_Enable', 0 )
        abel_obj.send_command(12, 'Torque_Enable', 0 )
        abel_obj.send_command(13, 'Torque_Enable', 0 )
        abel_obj.send_command(14, 'Torque_Enable', 0 )
        abel_obj.send_command(15, 'Torque_Enable', 0 )

def set_neck_torque(state):
    #Set 1 to enable the torque, 0 otherwise
    if state == 1:
        abel_obj.send_command(1, 'Torque_Enable', 1 )
        abel_obj.send_command(2, 'Torque_Enable', 1 )
        abel_obj.send_command(3, 'Torque_Enable', 1 )
        abel_obj.send_command(4, 'Torque_Enable', 1 )
        abel_obj.send_command(5, 'Torque_Enable', 1 )
    else:
        abel_obj.send_command(1, 'Torque_Enable', 0 )
        abel_obj.send_command(2, 'Torque_Enable', 0 )
        abel_obj.send_command(3, 'Torque_Enable', 0 )
        abel_obj.send_command(4, 'Torque_Enable', 0 )
        abel_obj.send_command(5, 'Torque_Enable', 0 )

def capture_position(lag):
    rospy.loginfo("Starting position acquisition...")
    rospy.loginfo("In 3 sec the torque will be disabled, keep the arms in a safe position...")
    rospy.sleep(3)
    set_joints_torque(0)
    rospy.loginfo("Now you have _lag_ seconds to create a pose...")
    rospy.sleep(lag)
    set_joints_torque(1)
    rospy.loginfo("The values of the joints (check ordering) are: ")    
    pose = abel_obj.joint_states_msg
    rospy.loginfo(pose.position)

    ## DA INSERIRE: ORDINARE GIUNTI PER FARLI COMBACIARE CON LA DEFINIZIONE NEL FILE .YAML
    ## ROS LI ORDINA IN MANIERA DIFFERENTE...


if __name__ == "__main__":
    rospy.init_node('move_abel_arms', log_level=rospy.DEBUG)
    
    initialize()
    rospy.sleep(3)

    zero_pose(5)

    #neutral_high(5)
    #movement_sequence_test(5)
    #capture_position(10)

