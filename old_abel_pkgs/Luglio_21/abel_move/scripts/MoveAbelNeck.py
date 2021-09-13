#!/usr/bin/env python3

import numpy as np
import rospy
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from dynamixel_workbench_msgs.msg import DynamixelState, DynamixelStateList
from dynamixel_workbench_msgs.srv import DynamixelCommand, DynamixelCommandRequest
from std_msgs.msg import Header
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray
#from abel_move.msg import neck_joints
from matplotlib import pyplot as plt

from modules.AbelMove import *
from modules.AbelGesture import *

abel = AbelMove()
gesture = AbelGesture()


class MoveAbelNeck(object):
    def __init__(self):
        #Create the object for Abel
        abel = AbelMove()
        gesture = AbelGesture()

        self.neck_gesture_topic = '/abel_move/neck/gesture'
        self.neck_gesture_save = '/abel_move/neck/gesture/save'
        self.lookat_topic = '/abel_move/neck/lookat'

        self.neck_gesture_pub = rospy.Publisher('/abel_move/neck/gesture', String, queue_size=1)
        self.neck_save_pub = rospy.Publisher('/abel_move/neck/gesture/save', String, queue_size=1)
        self.lookat_pub = rospy.Publisher('/abel_move/neck/lookat', Float64MultiArray, queue_size=1)

    def initialize(self):
        rospy.loginfo("Setting neutral position for the  neck...")
        self.neck_neutral(5)
        rospy.sleep(5)
        rospy.loginfo("Neck is ready!")

    def look_xy(self, x, y, duration):
        """ Questa funzione dovrà convertire un punto del piano frontale in un movimento del collo"""
        ## la normalizzazione avviene fra 0 e 1, sia nel caso dell'asse x che dell'asse y
        
        # # Asse X
        # self.lookat_point = JointTrajectoryPoint()
        # self.lookat_point.positions = [0.6*x, -0.4, 0.4, -0.4, 0.85,
        #                               -0.5, -0.2,    0,     0.75, 0, 
        #                                0.5,  0.2,    0,    -0.75, 0]
        # self.lookat_point.time_from_start = rospy.Duration(duration)

        # abel.move_all_joints(self.lookat_point)

        # Assi X,Y
        self.lookat_point = JointTrajectoryPoint()
        self.lookat_point.positions = [0.6*x, -0.4 + 0.8*y, 0.4 - 0.8*y, -0.4, 0.85,
                                      -0.5, -0.2,    0,     0.75, 0, 
                                       0.5,  0.2,    0,    -0.75, 0]

        self.lookat_point.velocities = [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0]

        self.lookat_point.time_from_start = rospy.Duration(duration)

        abel.move_all_joints(self.lookat_point)


    def lookat_sequence_test(self):
        #Asse x, y=0
        self.look_xy(1,0,3)
        rospy.sleep(3)

        self.look_xy(-1,0,3)
        rospy.sleep(3)

        self.look_xy(0.5,0,3)
        rospy.sleep(3)

        self.look_xy(-0.5,0,3)
        rospy.sleep(3)


        #Asse y, x=0
        self.look_xy(0,1,3)
        rospy.sleep(3)

        self.look_xy(0,-1,3)
        rospy.sleep(3)

        self.look_xy(0,0.5,3)
        rospy.sleep(3)

        self.look_xy(0,-0.5,3)
        rospy.sleep(3)


        #Entrambi gli assi
        self.look_xy(1,1,3)
        rospy.sleep(3)

        self.look_xy(-1,-1,3)
        rospy.sleep(3)

        self.look_xy(0.5,0.5,53)
        rospy.sleep(3)

        self.look_xy(-0.5,-0.5,3)
        rospy.sleep(3)

        self.look_xy(1,-1,3)
        rospy.sleep(3)

        self.look_xy(1,-1,3)
        rospy.sleep(3)

        self.look_xy(0.5,-0.5,3)
        rospy.sleep(3)

        self.look_xy(0.5,-0.5,3)
        rospy.sleep(3)

    def gesture_neck_list(self):
        rospy.loginfo("Gesture available: neck_zero, neck_neutral, neck_up, neck_down, neck_rotate_right, neck_rotate_left, neck_sequence_test.")


    def neck_zero(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [0, 0, 0, 0, 0, 
                                              0, 0, 0, 0, 0, 
                                              0, 0, 0, 0, 0]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_zero)
        self.neck_gesture_pub.publish("neck_zero")

    def neck_neutral(self, duration):
        """Neutral (visual)"""
        self.joint_position_neutral = JointTrajectoryPoint()
        self.joint_position_neutral.positions = [0.003067961661145091, -0.39576706290245056, 0.2929903268814087, -0.43411657214164734, 0.8590292930603027, 
                                     0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0]

        self.joint_position_neutral.time_from_start = rospy.Duration(duration)
        abel.move_all_joints(self.joint_position_neutral)
        self.neck_gesture_pub.publish("neck_neutral")

    def neck_up(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [-0.015339808538556099, 0.8283496499061584, -1.1443496942520142, -1.1198060512542725, 1.4879614114761353, 
                                     0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        abel.move_all_joints(self.joint_position_zero)
        self.neck_gesture_pub.publish("neck_up")

    def neck_down(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [-0.026077674701809883, -0.452524334192276, 0.4801360070705414, 0.3267379105091095, -0.026077674701809883, 
                                              0, 0, 0, 0, 0, 
                                              0, 0, 0, 0, 0]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        abel.move_all_joints(self.joint_position_zero)
        self.neck_gesture_pub.publish("neck_down")

    def neck_rotate_right(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [-0.6166602969169617, -0.1733398288488388, -0.5491651296615601, -0.48166999220848083, 0.2316311001777649, 
                                              0, 0, 0, 0, 0, 
                                              0, 0, 0, 0, 0]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        abel.move_all_joints(self.joint_position_zero)
        self.neck_gesture_pub.publish("neck_rotate_right")

    def neck_rotate_left(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [0.630466103553772, -0.010737866163253784, 0.1702718734741211, -0.1672039031982422, 0.8283496499061584, 
                                              0, 0, 0, 0, 0, 
                                              0, 0, 0, 0, 0]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        abel.move_all_joints(self.joint_position_zero)
        self.neck_gesture_pub.publish("neck_rotate_left")


    def neck_sequence_test(self, time):
        """Perform a simple sequence of movement for testing and debugging"""
        self.neck_neutral(time)
        rospy.sleep(time)

        self.neck_up(time)
        rospy.sleep(time)

        self.neck_neutral(time)
        rospy.sleep(time)

        self.neck_down(time)
        rospy.sleep(time)

        self.neck_neutral(time)
        rospy.sleep(time)

        self.neck_rotate_right(time)
        rospy.sleep(time)

        self.neck_neutral(time)
        rospy.sleep(time)

        self.neck_rotate_left(time)
        rospy.sleep(time)

        self.neck_neutral(time)
        rospy.sleep(time)


    def explore(self):
        rospy.loginfo("In 3 secs the neck torques will be disabled...")
        rospy.sleep(3)
        abel.set_neck_torque(0)

        pub1 = rospy.Publisher('/neck_joint1', Float64, queue_size=10)
        pub2 = rospy.Publisher('/neck_joint2', Float64, queue_size=10)
        pub3 = rospy.Publisher('/neck_joint3', Float64, queue_size=10)
        pub4 = rospy.Publisher('/neck_joint4', Float64, queue_size=10)
        pub5 = rospy.Publisher('/neck_joint5', Float64, queue_size=10)

        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            neck1 = abel.joint_states_msg.position[6]
            neck2 = abel.joint_states_msg.position[7]
            neck3 = abel.joint_states_msg.position[8]
            neck4 = abel.joint_states_msg.position[9]
            neck5 = abel.joint_states_msg.position[10]

            #neck_msg = Float64MultiArray()
            #neck_msg.data = [neck1, neck2, neck3, neck4]

            pub1.publish(neck1)
            pub2.publish(neck2)
            pub3.publish(neck3)
            pub4.publish(neck4)
            pub5.publish(neck5)

            rate.sleep()

            ## OPEN RQT-PLOT TO VISUALIZE DATA ## rqt-plot

    


            


if __name__ == "__main__":
    rospy.init_node('MoveAbelNeck', log_level=rospy.DEBUG)
    rate = rospy.Rate(10)