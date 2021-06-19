#!/usr/bin/env python

from math import pi
import rospy
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from dynamixel_workbench_msgs.msg import DynamixelState, DynamixelStateList
from dynamixel_workbench_msgs.srv import DynamixelCommand, DynamixelCommandRequest
from std_msgs.msg import Header

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