#!/usr/bin/env python3

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
        joints_str.joint_names = ['neck_1',      'neck_2',      'neck_3',   'neck_4',  'neck_5',
                                  'shoulder_l1', 'shoulder_l2', 'biceps_l', 'elbow_l', 'forearm_l', 
                                  'shoulder_r1', 'shoulder_r2', 'biceps_r', 'elbow_r', 'forearm_r' ]
    
        #Adding the point to the points list
        joints_str.points.append(point)
        self.goal_dynamixel_position_publisher.publish(joints_str)

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

    def set_joints_torque(self, state):
        #Set 1 to enable the torque, 0 otherwise
        if state == 1:
            self.send_command(6, 'Torque_Enable', 1)
            self.send_command(7, 'Torque_Enable', 1)
            self.send_command(8, 'Torque_Enable', 1)
            self.send_command(9, 'Torque_Enable', 1)
            self.send_command(10, 'Torque_Enable', 1)
            self.send_command(11, 'Torque_Enable', 1)
            self.send_command(12, 'Torque_Enable', 1)
            self.send_command(13, 'Torque_Enable', 1)
            self.send_command(14, 'Torque_Enable', 1)
            self.send_command(15, 'Torque_Enable', 1)
        else:
            self.send_command(6, 'Torque_Enable', 0)
            self.send_command(7, 'Torque_Enable', 0)
            self.send_command(8, 'Torque_Enable', 0)
            self.send_command(9, 'Torque_Enable', 0)
            self.send_command(10, 'Torque_Enable', 0)
            self.send_command(11, 'Torque_Enable', 0)
            self.send_command(12, 'Torque_Enable', 0)
            self.send_command(13, 'Torque_Enable', 0)
            self.send_command(14, 'Torque_Enable', 0)
            self.send_command(15, 'Torque_Enable', 0)

    def set_neck_torque(self, state):
    #Set 1 to enable the torque, 0 otherwise
        if state == 1:
            self.send_command(1, 'Torque_Enable', 1 )
            self.send_command(2, 'Torque_Enable', 1 )
            self.send_command(3, 'Torque_Enable', 1 )
            self.send_command(4, 'Torque_Enable', 1 )
            self.send_command(5, 'Torque_Enable', 1 )
        else:
            self.send_command(1, 'Torque_Enable', 0 )
            self.send_command(2, 'Torque_Enable', 0 )
            self.send_command(3, 'Torque_Enable', 0 )
            self.send_command(4, 'Torque_Enable', 0 )
            self.send_command(5, 'Torque_Enable', 0 )

    def capture_position(self, lag):
        rospy.loginfo("Starting position acquisition...")
        rospy.loginfo("In 3 sec the arms torques will be disabled, keep the arms in a safe position...")
        rospy.sleep(3)
        self.set_joints_torque(0)

        rospy.loginfo("Now you have _lag_ seconds to create a pose...")
        rospy.sleep(lag)
        self.set_joints_torque(1)

        rospy.loginfo("The values of the joints (check ordering) are: ")    
        pose = self.joint_states_msg
        rospy.loginfo(pose.name)
        rospy.loginfo(pose.position)

        ## DA INSERIRE: ORDINARE GIUNTI PER FARLI COMBACIARE CON LA DEFINIZIONE NEL FILE .YAML
        ## ROS LI ORDINA IN MANIERA DIFFERENTE...

    def set_current(self, id, value):
        """ Set the current_limit to change the maximum torque, single joint (0-100%)"""
        m = float(2047/100)
        if value>=0 and value<=100:
            self.send_command(id, "Current_Limit", int(value * m) )
        else:
            rospy.loginfo("The value prompted for the current is outside the range 0-100...")

    def set_joints_current(self, value):
        """Set the current_limit for all the joints (0-100%)"""
        if value>=0 and value<=100:
            for i in range(6,16):
                self.set_current(i, value)
        else:
            rospy.loginfo("The value prompted for the current is outside the range 0-100...")

    def set_compliance(self, id, value):
        """ Set the spring K value for PID control of the single joint with a value from 0-100%"""
        m = 8
        if value>=0 and value<=100:
            self.send_command(id, "Position_P_Gain", int(value * m) )
        else:
            rospy.loginfo("The value prompted for the current is outside the range 0-100...")

    def set_joints_compliance(self, value):
        """Set the spring K values for all the joints (0-100%)"""
        if value>=0 and value<=100:
            for i in range(6,16):
                self.set_compliance(i, value)
        else:
            rospy.loginfo("The value prompted for the compliance is outside the range 0-100...")

    def set_velocity(self, id, value):
        """Set the velocity limit for the single joint (0-100%)"""
        m = 0.5
        if value>=0 and value<=100:
            self.send_command(id, "Profile_Velocity", int(value * m) )
        else:
            rospy.loginfo("The value prompted for the velocity is outside the range 0-100...")

    def set_joints_velocity(self, value):
        """Set the velocity limit for all the joints (0-100%)"""
        if value>=0 and value<=100:
            for i in range(6,16):
                self.set_velocity(i, value)
        else:
            rospy.loginfo("The value prompted for the velocity is outside the range 0-100...")

    def set_acceleration(self, id, value):
        """Set the acceleration limit for the single joint (0-100%)"""
        m = 0.5
        if value>=0 and value<=100:
            self.send_command(id, "Profile_Acceleration", int(value * m) )
        else:
            rospy.loginfo("The value prompted for the acceleration is outside the range 0-100...")

    def set_joints_acceleration(self, value):
        """Set the acceleration limit for all the joints (0-100%)"""
        if value>=0 and value<=100:
            for i in range(6,16):
                self.set_acceleration(i, value)
        else:
            rospy.loginfo("The value prompted for the acceleration is outside the range 0-100...")
