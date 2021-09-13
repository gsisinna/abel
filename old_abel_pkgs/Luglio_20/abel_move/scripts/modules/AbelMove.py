#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from dynamixel_workbench_msgs.msg import DynamixelState, DynamixelStateList
from dynamixel_workbench_msgs.srv import DynamixelCommand, DynamixelCommandRequest
from std_msgs.msg import Header
import numpy as np

class AbelMove(object):
    def __init__(self):
        # We subscribe to the joint states to have info of the system (joints)
        self.joint_states_topic_name = '/dynamixel_workbench/joint_states'

        # We subscribe to the dynamixel state to have info of the system (motors)
        self.dynamixel_state_topic_name = '/dynamixel_workbench/dynamixel_state'
        sub = rospy.Subscriber(self.joint_states_topic_name, JointState, self.joint_states_callback)
        sub_dynamixel = rospy.Subscriber(self.dynamixel_state_topic_name, DynamixelStateList, self.get_motor)

        # We start the Publisher for the positions of the joints
        self.goal_dynamixel_position_publisher = rospy.Publisher('/dynamixel_workbench/joint_trajectory', JointTrajectory, queue_size=100)

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


    def min_jerk(self, setpoint, frequency, move_time):
        current = self.joint_states_msg.position
        timefreq = int(move_time * frequency)

        trajectory = []
        trajectory_derivative = []

        rospy.logwarn("Min_Jerk trajectory generation...")
    
        for time in range(1, timefreq):
            trajectory.append(
                current + (setpoint - current) *
                (10.0 * (time/timefreq)**3
                - 15.0 * (time/timefreq)**4
                + 6.0 * (time/timefreq)**5))

            trajectory_derivative.append(
                frequency * (1.0/timefreq) * (setpoint - current) *
                (30.0 * (time/timefreq)**2.0
                - 60.0 * (time/timefreq)**3.0
                + 30.0 * (time/timefreq)**4.0))

            trajectory = trajectory.toalist()
            trajectory_derivative = trajectory_derivative.toalist()

        joints_str = JointTrajectory()
        joints_str.header = Header()
        joints_str.header.stamp = rospy.Time.now()
        joints_str.joint_names = ['neck_1',      'neck_2',      'neck_3',   'neck_4',  'neck_5',
                                  'shoulder_l1', 'shoulder_l2', 'biceps_l', 'elbow_l', 'forearm_l', 
                                  'shoulder_r1', 'shoulder_r2', 'biceps_r', 'elbow_r', 'forearm_r' ]

        rospy.logwarn("Waypoints generation...")
    
        #Adding the point to the points list
        for i in range(1, timefreq):
            point = JointTrajectoryPoint()
            point.positions = trajectory[i]
            point.velocities = trajectory_derivative[i]
            point.time_from_start = rospy.Duration(move_time)      ##dipende da quanti punti prendiamo? testare
            joints_str.append(point)
            
        self.goal_dynamixel_position_publisher.publish(joints_str)

        rospy.logwarn("Trajectory published!")


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

    def sort_joints(self):
        out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        joints = list(self.joint_states_msg.position)
        #neck
        out[0] = joints[6]
        out[1] = joints[7]
        out[2] = joints[8]
        out[3] = joints[9]
        out[4] = joints[10]
        
        out[5] = joints[11]
        out[6] = joints[12]

        out[7] =   joints[0]
        out[8] =   joints[2]
        out[9] =   joints[4]
        out[10] =  joints[13]
        out[11] =  joints[14]
        out[12] =  joints[1]
        out[13] =  joints[3]
        out[14] =  joints[5]

        return out

    ## spostare in move_abel_arms
    def capture_position_arms(self, lag):
        rospy.loginfo("Starting position acquisition...")
        rospy.loginfo("In 3 sec the arms torques will be disabled, keep the arms in a safe position...")
        rospy.sleep(3)
        self.set_joints_torque(0)
        #self.set_neck_torque(0)

        rospy.loginfo("Now you have _lag_ seconds to create a pose...")
        rospy.sleep(lag)
        self.set_joints_torque(1)
        #self.set_neck_torque(1)

        rospy.loginfo("The values of the joints (check ordering) are: ")    
        pose = self.sort_joints()

        rospy.loginfo("joints = [shoulder_l1, shoulder_l2, biceps_l, elbow_l, forearm_l, shoulder_r1, shoulder_r2, biceps_r, elbow_r, forearm_r ]")
        rospy.loginfo(pose[5:14])

    ## spostare in move_abel_neck
    def capture_position_neck(self, lag):
        rospy.loginfo("Starting position acquisition...")
        rospy.loginfo("In 3 sec the neck torques will be disabled, keep the neck in a safe position...")
        rospy.sleep(3)
        self.set_neck_torque(0)

        rospy.loginfo("Now you have _lag_ seconds to create a pose...")
        rospy.sleep(lag)
        self.set_neck_torque(1)

        rospy.loginfo("The values of the joints (check ordering) are: ")    
        pose = self.sort_joints()

        rospy.loginfo("joints = [ neck_1, neck_2, neck_3, neck_4, neck_5]")
        rospy.loginfo(pose[0:5])

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
