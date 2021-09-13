#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from dynamixel_workbench_msgs.msg import DynamixelState, DynamixelStateList
from dynamixel_workbench_msgs.srv import DynamixelCommand, DynamixelCommandRequest
from std_msgs.msg import Header
from std_msgs.msg import String

from .AbelMove import *

class AbelGesture(object):
    def __init__(self):
        self.abel = AbelMove()
        # Topic for gestures
        self.gesture_topic_name = '/abel_move/gesture'

        # We start the Publisher for the topic created
        self.gesture_publisher = rospy.Publisher('/abel_move/gesture', String, queue_size=10)

    def neutral_pose(self, duration):
        """ Neutrale"""
        self.joint_position_home = JointTrajectoryPoint()
        self.joint_position_home.positions = [-0.003067961661145091, 0.15186409652233124, -0.3604854941368103, -0.5645049214363098, 0.8774370551109314, 
                                             -0.5, -0.2,    0,     0.75, 0, 
                                              0.5,  0.2,    0,    -0.75, 0]

        self.joint_position_home.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_home)

    def neutral_high(self, duration):
        """ Neutrale, braccia alte per configurazione bicipite senza collisioni """
        self.joint_position_home = JointTrajectoryPoint()
        self.joint_position_home.positions = [-0.003067961661145091, 0.15186409652233124, -0.3604854941368103, -0.5645049214363098, 0.8774370551109314, 
                                              0.5, 0.9,  0.25,  0,  0.25, 
                                             -0.5, -0.9, -0.25, -0.75, 0]

        self.joint_position_home.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_home)

    def zero_pose(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [-0.003067961661145091, 0.15186409652233124, -0.3604854941368103, -0.5645049214363098, 0.8774370551109314, 
                                              0,  0,    0,     0,    0, 
                                              0,  0,    0,     0,    0]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_zero)

    def mano_pose(self, duration):
        """ Stretta di mano """
        self.joint_position_hand = JointTrajectoryPoint()
        self.joint_position_hand.positions = [-0.003067961661145091, 0.15186409652233124, -0.3604854941368103, -0.5645049214363098, 0.8774370551109314, 
                                             -0.22549518942832947, -0.010737866163253784, -1.4434759616851807, 0.9295923709869385, 1.274738073348999, 
                                             -1.3543108320236206, 0.10737866163253784, 0.9449321627616882, 0.2684466540813446, -0.6563301706314087]

        self.joint_position_hand.velocities = [0, 0, 0, 0, 0,
                                               50,40,20,5,1,
                                               0, 0, 0, 0, 0]

        self.joint_position_hand.accelerations = [0, 0, 0, 0, 0,
                                                  50,40,20,5,1,
                                                  0, 0, 0, 0, 0]

        self.joint_position_hand.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_hand)

    def hug_pose(self, duration):
        """Abbraccio"""
        self.joint_position_hug = JointTrajectoryPoint()
        self.joint_position_hug.positions = [-0.003067961661145091, 0.15186409652233124, -0.3604854941368103, -0.5645049214363098, 0.8774370551109314, 
                                    1.9173012399673462, 0.8482913970947266, -0.3037281930446625, -0.07976700365543365, 0.5568350553512573, 
                                    -1.418932318687439, -0.771592378616333, 0.35895150899887085, 0.5322913527488708, -0.5016117095947266]

        self.joint_position_hug.velocities = [ 0, 0, 0, 0, 0,
                                               50,40,20,5,1,
                                               50,40,20,5,1, ]

        self.joint_position_hug.accelerations = [0, 0, 0, 0, 0,
                                                  50,40,20,5,1,
                                                  50,40,20,5,1,]

        self.joint_position_hug.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_hug)
    

    def hello_pose(self, duration):
        """Saluto"""
        self.joint_position_hello = JointTrajectoryPoint()
        self.joint_position_hello.positions = [-0.003067961661145091, 0.15186409652233124, -0.3604854941368103, -0.5645049214363098, 0.8774370551109314,
                                      -0.47400006651878357, -0.09050486981868744, -0.08283496648073196, 0.8774370551109314, 
                                       0.47400006651878357, -2.015650749206543, -1.0707186460494995, -0.019941750913858414, -2.885417938232422]

        self.joint_position_hello.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_hello)

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
        self.joint_position_zero.positions = [-0.015339808538556099, 0.8283496499061584, -1.1443496942520142, -1.1198060512542725, 1.4879614114761353, 
                                     0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_zero)

    def neck_down(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [-0.026077674701809883, -0.452524334192276, 0.4801360070705414, 0.3267379105091095, -0.026077674701809883, 
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

    def up_right_arm(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [0,   -0.25,   0.25, -0.25, 0.25, 
                                     0.37582531571388245, 0.14879614114761353, -2.7243499755859375, 0.8084079027175903, 0.26998063921928406, 
                                     -1.522335815429688, -1.0753206014633179, 0.452524334192276, 0.7900001406669617, -1.3]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_zero)


    def movement_sequence_test(self, time):
        """Perform a simple sequence of movement for testing and debugging"""    
        self.neutral_high(time)
        rospy.sleep(time)

        self.neutral_pose(time)
        rospy.sleep(time)

        self.mano_pose(time)
        rospy.sleep(time)

        self.hug_pose(time)
        rospy.sleep(time)

        self.hello_pose(time)
        rospy.sleep(time)

        self.neutral_pose(time)
        rospy.sleep(time)

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


if __name__ == "__main__":
    rospy.init_node('AbelGesture', log_level=rospy.DEBUG)

