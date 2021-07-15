#!/usr/bin/env python3

from numpy import float64
import rospy
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from dynamixel_workbench_msgs.msg import DynamixelState, DynamixelStateList
from dynamixel_workbench_msgs.srv import DynamixelCommand, DynamixelCommandRequest
from std_msgs.msg import Header

from modules.AbelMove import *
from modules.AbelGesture import *


class MoveAbelNeck(object):
    def __init__(self):
        #Create the object for Abel
        abel = AbelMove()
        gesture = AbelGesture()

        self.neck_gesture_topic = '/abel_move/neck/gesture'
        self.neck_gesture_save = '/abel_move/neck/gesture/save'
        self.lookat_topic = '/abel_move/neck/lookat'

        self.neck_gesture_pub = rospy.Publisher('/abel_move/neck/gesture', String, queue_size=10)
        self.neck_save_pub = rospy.Publisher('/abel_move/neck/gesture/save', String, queue_size=10)
        self.lookat_pub = rospy.Publisher('/abel_move/neck/lookat', float64, queue_size=10)

    def look_xy(self, x, y, duration):
        """ Questa funzione dovrà convertire un punto del piano frontale in un movimento del collo"""
        ## la normalizzazione avviene fra 0 e 1, sia nel caso dell'asse x che dell'asse y
        # Asse X
        if (x>=0 and x<=1) and (y>=0 and y<=1):
            self.lookat_point = JointTrajectoryPoint()
            self.lookat_point.positions = [x, 0, 0, 0, 0,
                                           0, 0, 0, 0, 0,
                                           0, 0, 0, 0, 0]
            self.lookat_point.time_from_start = rospy.Duration(duration)
            self.abel.move_all_joints(self.lookat_point)

            self.lookat_pub.publish(x,y)

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
        self.abel.move_all_joints(self.joint_position_neutral)
        self.neck_gesture_pub.publish("neck_neutral")

    def neck_up(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [-0.015339808538556099, 0.8283496499061584, -1.1443496942520142, -1.1198060512542725, 1.4879614114761353, 
                                     0, 0, 0, 0, 0, 
                                     0, 0, 0, 0, 0]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_zero)
        self.neck_gesture_pub.publish("neck_up")

    def neck_down(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [-0.026077674701809883, -0.452524334192276, 0.4801360070705414, 0.3267379105091095, -0.026077674701809883, 
                                              0, 0, 0, 0, 0, 
                                              0, 0, 0, 0, 0]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_zero)
        self.neck_gesture_pub.publish("neck_down")

    def neck_rotate_right(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [-0.6166602969169617, -0.1733398288488388, -0.5491651296615601, -0.48166999220848083, 0.2316311001777649, 
                                              0, 0, 0, 0, 0, 
                                              0, 0, 0, 0, 0]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_zero)
        self.neck_gesture_pub.publish("neck_rotate_right")

    def neck_rotate_left(self, duration):
        """Zero joints"""
        self.joint_position_zero = JointTrajectoryPoint()
        self.joint_position_zero.positions = [0.630466103553772, -0.010737866163253784, 0.1702718734741211, -0.1672039031982422, 0.8283496499061584, 
                                              0, 0, 0, 0, 0, 
                                              0, 0, 0, 0, 0]

        self.joint_position_zero.time_from_start = rospy.Duration(duration)
        self.abel.move_all_joints(self.joint_position_zero)
        self.neck_gesture_pub.publish("neck_rotate_left")


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
    rate = rospy.Rate(10)
    rospy.spin()