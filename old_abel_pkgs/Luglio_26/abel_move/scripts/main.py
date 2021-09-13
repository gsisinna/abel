#!/usr/bin/env python3

import numpy as np
import rospy
import pinocchio

from abel_move.AbelGesture  import AbelGesture
from abel_move.AbelMove     import AbelMove
from abel_move.MoveAbelArms import MoveAbelArms
from abel_move.MoveAbelNeck import MoveAbelNeck


from dynamixel_workbench_msgs.msg import DynamixelState, DynamixelStateList
from dynamixel_workbench_msgs.srv import (DynamixelCommand,
                                          DynamixelCommandRequest)

from moveit_msgs.msg import DisplayTrajectory
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64, Float64MultiArray, Header
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

abel    = AbelMove()
arms    = MoveAbelArms()
neck    = MoveAbelNeck()
gesture = AbelGesture()

def lookat_callback(data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        if (abs(data.data[0])<=1) and (abs(data.data[1])<=1):
                x = data.data[0]
                y = data.data[1]
                neck.look_xy(x, y, 5)
        else:
                rospy.WARN("Inserire dei valori compresi fra -1 ed 1...")

def inv_kin_callback(data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        arms.inverse_kinematics(data.data[0], data.data[1], data.data[2])

def gesture_arms_callback(data):
        gesture.gesture_arms_list()
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
        getattr(gesture, str(data))()

def gesture_neck_callback(data):
        neck.gesture_neck_list()
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
        getattr(neck, str(data))()

def capture_arms_callback(data):
        if data == 1:
                abel.capture_position_arms(10)
        else:
                rospy.loginfo("Send 1 if you want to start arms gesture acquisition...")

def capture_neck_callback(data):
        if data == 1:
                abel.capture_position_neck(10)
        else:
                rospy.loginfo("Send 1 if you want to start neck gesture acquisition...")

def moveit_callback(data):
        pos = data.position
        rospy.loginfo(pos)
        point = JointTrajectoryPoint()

        point.positions = [0.003067961661145091, -0.39576706290245056, 0.2929903268814087, -0.43411657214164734, 0.8590292930603027, 
                           pos[0], pos[1], pos[2], pos[3], pos[4], 
                           pos[5], pos[6], pos[7], pos[8], pos[9] ]

        point.time_from_start = rospy.Duration(2)

        abel.move_all_joints(point)

def planned_path_callback(data):
        #rospy.loginfo(data)
        #rospy.loginfo(data.trajectory)
        rospy.loginfo(data.trajectory[0].joint_trajectory)

        joints_str = data.trajectory[0].joint_trajectory
        abel.goal_dynamixel_position_publisher.publish(joints_str)


if __name__ == "__main__":
    rospy.init_node('main', log_level=rospy.DEBUG)
    rate = rospy.Rate(10)
    
    lookat_subscriber = rospy.Subscriber("/abel_move/neck/lookat", Float64MultiArray, lookat_callback )
    inv_kin_subscriber = rospy.Subscriber("/abel_move/arms/inverse_kinematics", Float64MultiArray, inv_kin_callback )

#     gesture_arms_subscriber = rospy.Subscriber("/abel_move/arms/gesture", String, gesture_arms_callback )
#     gesture_neck_subscriber = rospy.Subscriber("/abel_move/neck/gesture", String, gesture_neck_callback )

    capture_arms_subscriber = rospy.Subscriber("/abel_move/arms/capture", Float64, capture_arms_callback )
    capture_neck_subscriber = rospy.Subscriber("/abel_move/neck/capture", Float64, capture_neck_callback )
    
    ## -- MOVEIT TEST FOR JOINTS VALUES -- ##
    #moveit_subscriber = rospy.Subscriber("/joint_states", JointState, moveit_callback, queue_size=100 )
    #moveit_subscriber2 = rospy.Subscriber("/planned_trajectory", JointTrajectory, moveit_callback2, queue_size=100 )
    #planned_path_subscriber = rospy.Subscriber("move_group/display_planned_path", DisplayTrajectory, planned_path_callback,  queue_size=100 )


    ## -- INIT -- ##
    #arms.initialize()
    #rospy.sleep(3)

    gesture.neutral_high(5)
    rospy.sleep(3)

    
    ## -- MOVEMENT SEQUENCE -- ##
    #gesture.movement_sequence_test(5)
    #neck.neck_sequence_test(5)
    gesture.zero_pose(5)


    ## -- ESPLORAZIONE MOTORI COLLO -- ##
    #neck.explore()
    #neck.initialize()

    
    ## -- TEST LOOK_XY -- ##
    #neck.lookat_sequence_test()

    ## -- TEST CINEMATICA DIRETTA ED INVERSA -- ##
#     arms.direct_kinematics()
    
#     for i in range(10):
#         arms.inverse_kinematics(-0.2-np.cos(i/10)/10, 0.5, -0.2+np.sin(i/10)/10)
#         arms.direct_kinematics()
#         rospy.sleep(2)

    ##TEST CAPTURE POSITION##
    #abel.capture_position_arms(5)
    #abel.capture_position_neck(10)


    ## TEST COMPLIANCE ##
    #abel.set_joints_compliance(100)


    ##TEST CURRENT LIMIT##
    #abel.set_joints_current(95)


    ##TEST VELOCITY AND ACCELERATION --> GESTURE.PY ##
    #abel.set_joints_velocity(50)
    #abel.set_joints_acceleration(50)


    #rospy.spin()
