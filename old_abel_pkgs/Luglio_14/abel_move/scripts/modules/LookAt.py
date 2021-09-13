#gestione della testa di abel

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