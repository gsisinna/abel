#!/usr/bin/env python3

from math import pi
import rospy
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from dynamixel_workbench_msgs.msg import DynamixelState, DynamixelStateList
from dynamixel_workbench_msgs.srv import DynamixelCommand, DynamixelCommandRequest
from std_msgs.msg import Header

from AbelMove import *

class AbelMove(object):
    def __init__(self):
        # We subscribe to the joint states to have info of the system (joints)
        self.joint_states_topic_name = '/dynamixel_workbench/joint_states'
        # We subscribe to the dynamixel state to have info of the system (motors)
        self.dynamixel_state_topic_name = '/dynamixel_workbench/dynamixel_state'
        sub = rospy.Subscriber(self.joint_states_topic_name, JointState, self.joint_states_callback)
        sub_dynamixel = rospy.Subscriber(self.dynamixel_state_topic_name, DynamixelStateList, self.get_motor)
        # We start the Publisher for the positions of the joints
        self.goal_dynamixel_position_publisher = rospy.Publisher('/dynamixel_workbench/joint_trajectory', JointTrajectory, queue_size=10)
        # Wait for the service client /joint_command to be running
        joint_command_service_name = "/dynamixel_workbench/dynamixel_command"
        rospy.wait_for_service(joint_command_service_name)
        # Create the connection to the service
        self.joint_command_service = rospy.ServiceProxy(joint_command_service_name, DynamixelCommand)        

    def joint_states_callback(self,msg):
        """
        rosmsg show sensor_msgs/JointState
            std_msgs/Header header
              uint32 seq
              time stamp
              string frame_id
            string[] name
            float64[] position
            float64[] velocity
            float64[] effort

        :param msg:
        :return:
        """
        self.joint_states_msg = msg

    def check_join_states_ready(self):
        self.joint_states_msg = None
        rospy.logdebug("Waiting for "+self.joint_states_topic_name+" to be READY...")
        while self.joint_states_msg is None and not rospy.is_shutdown():
            try:
                self.joint_states_msg = rospy.wait_for_message(self.joint_states_topic_name, JointState, timeout=5.0)
                rospy.logdebug("Current "+self.joint_states_topic_name+" READY=>")

            except:
                rospy.logerr("Current "+self.joint_states_topic_name+" not ready yet, retrying ")

    def move_all_joints(self, point):

        rospy.logwarn("move_all_joints STARTED")
        
        joints_str = JointTrajectory()
        joints_str.header = Header()
        joints_str.header.stamp = rospy.Time.now()
        joints_str.joint_names = ['shoulder1', 'shoulder2', 'biceps', 'elbow', 'forearm']
    
        #Adding the point to the points list
        joints_str.points.append(point)

        rospy.logwarn("PUBLISH STARTED")
        self.goal_dynamixel_position_publisher.publish(joints_str)
        rospy.logwarn("PUBLISH FINISHED")

        rospy.logwarn("move_all_joints FINISHED")


    def move_one_joint(self, joint_id, position, unit="rad"):
        """
        rossrv show dynamixel_workbench_msgs/DynamixelCommand
            string command

            uint8 id
            string addr_name
            int32 value

            ---

            bool comm_result

        :param joint_id:
        :param position:
        :param units:
        :return:
        """
        joint_cmd_req = DynamixelCommandRequest()
        joint_cmd_req.addr_name = 'Goal_Position'
        joint_cmd_req.id = joint_id
        joint_cmd_req.value = position

        result = self.joint_command_service(joint_cmd_req)
        rospy.logwarn("move_one_joint went ok?="+str(result))

    def send_command(self, id, addr_name, value):
        """
        rossrv show dynamixel_workbench_msgs/DynamixelCommand
            string command

            uint8 id
            string addr_name
            int32 value

            ---

            bool comm_result

        :param joint_id:
        :param position:
        :param units:
        :return:
        """
        cmd_req = DynamixelCommandRequest()
        cmd_req.id = id
        cmd_req.addr_name = addr_name
        cmd_req.value = value

        result = self.joint_command_service(cmd_req)
        rospy.logwarn("send_command went ok?= "+str(result))

    def get_joint_names(self):
        return self.joint_states_msg.name


    def get_motor(self, msg):
        self.get_motor_msg = msg
        return(msg)


#Create the object for Abel
abel_obj = AbelMove()

def neutral_pose(duration):
    # Neutrale
    joint_position_home = JointTrajectoryPoint()
    joint_position_home.positions = [-0.5, -0.2, 0, 0.75, 0]
    joint_position_home.time_from_start = rospy.Duration(duration)

    abel_obj.move_all_joints(joint_position_home)

def neutral_high(duration):
    # Neutrale, braccia alte per configurazione bicipite senza collisioni
    joint_position_home = JointTrajectoryPoint()
    joint_position_home.positions = [0.5, 0.75, 0, 0.75, 0]
    joint_position_home.time_from_start = rospy.Duration(duration)

    abel_obj.move_all_joints(joint_position_home)

def zero_pose(duration):
    # Zero joints
    joint_position_zero = JointTrajectoryPoint()
    joint_position_zero.positions = [0,0,0,0,0]
    joint_position_zero.time_from_start = rospy.Duration(duration)

    abel_obj.move_all_joints(joint_position_zero)

def mano_pose(duration):
    joint_position_hand = JointTrajectoryPoint()
    joint_position_hand.positions = [0.9, -0.2, -0.75, -0.2, 0.5]
    joint_position_hand.time_from_start = rospy.Duration(duration)

    abel_obj.move_all_joints(joint_position_hand)

def hug_pose(duration):
    # Abbraccio
    joint_position_hug = JointTrajectoryPoint()
    joint_position_hug.positions = [1.57, 1.25, -1, 0.7, 1]
    joint_position_hug.time_from_start = rospy.Duration(duration)

    abel_obj.move_all_joints(joint_position_hug)
    

def hello_pose(duration):
    # Saluto
    joint_position_hello = JointTrajectoryPoint()
    joint_position_hello.positions = [1, 1.57, 0.75, -0.75, 0]
    joint_position_hello.time_from_start = rospy.Duration(duration)

    abel_obj.move_all_joints(joint_position_hello)

def initialize():
        rospy.loginfo("AbelMove INIT...Please wait")
        rospy.loginfo("Checking joints for stability...")
        biceps = abel_obj.joint_states_msg.position[0]
        rospy.loginfo(biceps)
        if biceps < -2.5 or biceps > 2:
            rospy.loginfo("Attenzione, bicipite in zona di instabilita. Riposizionamento sicuro ...")
            neutral_high(10)
        rospy.loginfo("AbelMove Ready!")

def set_joints_torque(state):
    #Set 1 to enable the torque, 0 otherwise
    if state == 1:
        abel_obj.send_command(6, 'Torque_Enable', 1 )
        abel_obj.send_command(7, 'Torque_Enable', 1 )
        abel_obj.send_command(8, 'Torque_Enable', 1 )
        abel_obj.send_command(9, 'Torque_Enable', 1 )
        abel_obj.send_command(10, 'Torque_Enable', 1 )
    else:
        abel_obj.send_command(6, 'Torque_Enable', 0 )
        abel_obj.send_command(7, 'Torque_Enable', 0 )
        abel_obj.send_command(8, 'Torque_Enable', 0 )
        abel_obj.send_command(9, 'Torque_Enable', 0 )
        abel_obj.send_command(10, 'Torque_Enable',0 )

def capture_position(lag):
    rospy.loginfo("Starting position acquisition...")
    rospy.loginfo("In 3 sec the torque will be disabled, keep the arms in a safe position...")
    rospy.sleep(3)
    set_joints_torque(0)
    rospy.loginfo("Now you have _lag_ seconds to create a pose...")
    rospy.sleep(lag)
    set_joints_torque(1)
    rospy.loginfo("The values of the joints are: ")
    pose = abel_obj.joint_states_msg
    rospy.loginfo(pose.position)


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
    rospy.init_node('move_abel', log_level=rospy.DEBUG)
    
    initialize()
    rospy.sleep(3)

    #neutral_high(5)
    movement_sequence_test(5)

    #capture_position(10)

