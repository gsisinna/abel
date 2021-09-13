// Generated by gencpp from file dynamixel_workbench_msgs/XM.msg
// DO NOT EDIT!


#ifndef DYNAMIXEL_WORKBENCH_MSGS_MESSAGE_XM_H
#define DYNAMIXEL_WORKBENCH_MSGS_MESSAGE_XM_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace dynamixel_workbench_msgs
{
template <class ContainerAllocator>
struct XM_
{
  typedef XM_<ContainerAllocator> Type;

  XM_()
    : Model_Number(0)
    , Firmware_Version(0)
    , ID(0)
    , Baud_Rate(0)
    , Return_Delay_Time(0)
    , Drive_Mode(0)
    , Operating_Mode(0)
    , Secondary_ID(0)
    , Protocol_Version(0)
    , Homing_Offset(0)
    , Moving_Threshold(0)
    , Temperature_Limit(0)
    , Max_Voltage_Limit(0)
    , Min_Voltage_Limit(0)
    , PWM_Limit(0)
    , Current_Limit(0)
    , Acceleration_Limit(0)
    , Velocity_Limit(0)
    , Max_Position_Limit(0)
    , Min_Position_Limit(0)
    , Shutdown(0)
    , Torque_Enable(0)
    , LED(0)
    , Status_Return_Level(0)
    , Registered_Instruction(0)
    , Hardware_Error_Status(0)
    , Velocity_I_Gain(0)
    , Velocity_P_Gain(0)
    , Position_D_Gain(0)
    , Position_I_Gain(0)
    , Position_P_Gain(0)
    , Feedforward_2nd_Gain(0)
    , Feedforward_1st_Gain(0)
    , Bus_Watchdog(0)
    , Goal_PWM(0)
    , Goal_Current(0)
    , Goal_Velocity(0)
    , Profile_Acceleration(0)
    , Profile_Velocity(0)
    , Goal_Position(0)
    , Realtime_Tick(0)
    , Moving(0)
    , Moving_Status(0)
    , Present_PWM(0)
    , Present_Load(0)
    , Present_Current(0)
    , Present_Velocity(0)
    , Present_Position(0)
    , Velocity_Trajectory(0)
    , Position_Trajectory(0)
    , Present_Input_Voltage(0)
    , Present_Temperature(0)  {
    }
  XM_(const ContainerAllocator& _alloc)
    : Model_Number(0)
    , Firmware_Version(0)
    , ID(0)
    , Baud_Rate(0)
    , Return_Delay_Time(0)
    , Drive_Mode(0)
    , Operating_Mode(0)
    , Secondary_ID(0)
    , Protocol_Version(0)
    , Homing_Offset(0)
    , Moving_Threshold(0)
    , Temperature_Limit(0)
    , Max_Voltage_Limit(0)
    , Min_Voltage_Limit(0)
    , PWM_Limit(0)
    , Current_Limit(0)
    , Acceleration_Limit(0)
    , Velocity_Limit(0)
    , Max_Position_Limit(0)
    , Min_Position_Limit(0)
    , Shutdown(0)
    , Torque_Enable(0)
    , LED(0)
    , Status_Return_Level(0)
    , Registered_Instruction(0)
    , Hardware_Error_Status(0)
    , Velocity_I_Gain(0)
    , Velocity_P_Gain(0)
    , Position_D_Gain(0)
    , Position_I_Gain(0)
    , Position_P_Gain(0)
    , Feedforward_2nd_Gain(0)
    , Feedforward_1st_Gain(0)
    , Bus_Watchdog(0)
    , Goal_PWM(0)
    , Goal_Current(0)
    , Goal_Velocity(0)
    , Profile_Acceleration(0)
    , Profile_Velocity(0)
    , Goal_Position(0)
    , Realtime_Tick(0)
    , Moving(0)
    , Moving_Status(0)
    , Present_PWM(0)
    , Present_Load(0)
    , Present_Current(0)
    , Present_Velocity(0)
    , Present_Position(0)
    , Velocity_Trajectory(0)
    , Position_Trajectory(0)
    , Present_Input_Voltage(0)
    , Present_Temperature(0)  {
  (void)_alloc;
    }



   typedef uint16_t _Model_Number_type;
  _Model_Number_type Model_Number;

   typedef uint8_t _Firmware_Version_type;
  _Firmware_Version_type Firmware_Version;

   typedef uint8_t _ID_type;
  _ID_type ID;

   typedef uint8_t _Baud_Rate_type;
  _Baud_Rate_type Baud_Rate;

   typedef uint8_t _Return_Delay_Time_type;
  _Return_Delay_Time_type Return_Delay_Time;

   typedef uint8_t _Drive_Mode_type;
  _Drive_Mode_type Drive_Mode;

   typedef uint8_t _Operating_Mode_type;
  _Operating_Mode_type Operating_Mode;

   typedef uint8_t _Secondary_ID_type;
  _Secondary_ID_type Secondary_ID;

   typedef uint8_t _Protocol_Version_type;
  _Protocol_Version_type Protocol_Version;

   typedef int32_t _Homing_Offset_type;
  _Homing_Offset_type Homing_Offset;

   typedef uint32_t _Moving_Threshold_type;
  _Moving_Threshold_type Moving_Threshold;

   typedef uint8_t _Temperature_Limit_type;
  _Temperature_Limit_type Temperature_Limit;

   typedef uint16_t _Max_Voltage_Limit_type;
  _Max_Voltage_Limit_type Max_Voltage_Limit;

   typedef uint16_t _Min_Voltage_Limit_type;
  _Min_Voltage_Limit_type Min_Voltage_Limit;

   typedef uint16_t _PWM_Limit_type;
  _PWM_Limit_type PWM_Limit;

   typedef uint16_t _Current_Limit_type;
  _Current_Limit_type Current_Limit;

   typedef uint32_t _Acceleration_Limit_type;
  _Acceleration_Limit_type Acceleration_Limit;

   typedef uint32_t _Velocity_Limit_type;
  _Velocity_Limit_type Velocity_Limit;

   typedef uint32_t _Max_Position_Limit_type;
  _Max_Position_Limit_type Max_Position_Limit;

   typedef uint32_t _Min_Position_Limit_type;
  _Min_Position_Limit_type Min_Position_Limit;

   typedef uint8_t _Shutdown_type;
  _Shutdown_type Shutdown;

   typedef uint8_t _Torque_Enable_type;
  _Torque_Enable_type Torque_Enable;

   typedef uint8_t _LED_type;
  _LED_type LED;

   typedef uint8_t _Status_Return_Level_type;
  _Status_Return_Level_type Status_Return_Level;

   typedef uint8_t _Registered_Instruction_type;
  _Registered_Instruction_type Registered_Instruction;

   typedef uint8_t _Hardware_Error_Status_type;
  _Hardware_Error_Status_type Hardware_Error_Status;

   typedef uint16_t _Velocity_I_Gain_type;
  _Velocity_I_Gain_type Velocity_I_Gain;

   typedef uint16_t _Velocity_P_Gain_type;
  _Velocity_P_Gain_type Velocity_P_Gain;

   typedef uint16_t _Position_D_Gain_type;
  _Position_D_Gain_type Position_D_Gain;

   typedef uint16_t _Position_I_Gain_type;
  _Position_I_Gain_type Position_I_Gain;

   typedef uint16_t _Position_P_Gain_type;
  _Position_P_Gain_type Position_P_Gain;

   typedef uint16_t _Feedforward_2nd_Gain_type;
  _Feedforward_2nd_Gain_type Feedforward_2nd_Gain;

   typedef uint16_t _Feedforward_1st_Gain_type;
  _Feedforward_1st_Gain_type Feedforward_1st_Gain;

   typedef uint8_t _Bus_Watchdog_type;
  _Bus_Watchdog_type Bus_Watchdog;

   typedef int16_t _Goal_PWM_type;
  _Goal_PWM_type Goal_PWM;

   typedef int16_t _Goal_Current_type;
  _Goal_Current_type Goal_Current;

   typedef int32_t _Goal_Velocity_type;
  _Goal_Velocity_type Goal_Velocity;

   typedef uint32_t _Profile_Acceleration_type;
  _Profile_Acceleration_type Profile_Acceleration;

   typedef uint32_t _Profile_Velocity_type;
  _Profile_Velocity_type Profile_Velocity;

   typedef uint32_t _Goal_Position_type;
  _Goal_Position_type Goal_Position;

   typedef uint16_t _Realtime_Tick_type;
  _Realtime_Tick_type Realtime_Tick;

   typedef uint8_t _Moving_type;
  _Moving_type Moving;

   typedef uint8_t _Moving_Status_type;
  _Moving_Status_type Moving_Status;

   typedef int16_t _Present_PWM_type;
  _Present_PWM_type Present_PWM;

   typedef int16_t _Present_Load_type;
  _Present_Load_type Present_Load;

   typedef int16_t _Present_Current_type;
  _Present_Current_type Present_Current;

   typedef int32_t _Present_Velocity_type;
  _Present_Velocity_type Present_Velocity;

   typedef int32_t _Present_Position_type;
  _Present_Position_type Present_Position;

   typedef uint32_t _Velocity_Trajectory_type;
  _Velocity_Trajectory_type Velocity_Trajectory;

   typedef uint32_t _Position_Trajectory_type;
  _Position_Trajectory_type Position_Trajectory;

   typedef uint16_t _Present_Input_Voltage_type;
  _Present_Input_Voltage_type Present_Input_Voltage;

   typedef uint8_t _Present_Temperature_type;
  _Present_Temperature_type Present_Temperature;





  typedef boost::shared_ptr< ::dynamixel_workbench_msgs::XM_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::dynamixel_workbench_msgs::XM_<ContainerAllocator> const> ConstPtr;

}; // struct XM_

typedef ::dynamixel_workbench_msgs::XM_<std::allocator<void> > XM;

typedef boost::shared_ptr< ::dynamixel_workbench_msgs::XM > XMPtr;
typedef boost::shared_ptr< ::dynamixel_workbench_msgs::XM const> XMConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::dynamixel_workbench_msgs::XM_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::dynamixel_workbench_msgs::XM_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace dynamixel_workbench_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'dynamixel_workbench_msgs': ['/home/user/simulation_ws/src/open_manipulator_tc/dynamixel-workbench-msgs/dynamixel_workbench_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::dynamixel_workbench_msgs::XM_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dynamixel_workbench_msgs::XM_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dynamixel_workbench_msgs::XM_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dynamixel_workbench_msgs::XM_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dynamixel_workbench_msgs::XM_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dynamixel_workbench_msgs::XM_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::dynamixel_workbench_msgs::XM_<ContainerAllocator> >
{
  static const char* value()
  {
    return "625146aaba5730bf1ea1a9008887b10d";
  }

  static const char* value(const ::dynamixel_workbench_msgs::XM_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x625146aaba5730bfULL;
  static const uint64_t static_value2 = 0x1ea1a9008887b10dULL;
};

template<class ContainerAllocator>
struct DataType< ::dynamixel_workbench_msgs::XM_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dynamixel_workbench_msgs/XM";
  }

  static const char* value(const ::dynamixel_workbench_msgs::XM_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::dynamixel_workbench_msgs::XM_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# This message is compatible with control table of Dynamixel XM Series (XM430-W210, XM430-W350)\n\
# If you want to specific information about control table, please follow the link (http://support.robotis.com/en/)\n\
\n\
uint16 Model_Number\n\
uint8  Firmware_Version\n\
uint8  ID\n\
uint8  Baud_Rate\n\
uint8  Return_Delay_Time\n\
uint8  Drive_Mode\n\
uint8  Operating_Mode\n\
uint8  Secondary_ID\n\
uint8  Protocol_Version\n\
int32  Homing_Offset\n\
uint32 Moving_Threshold\n\
uint8  Temperature_Limit\n\
uint16 Max_Voltage_Limit\n\
uint16 Min_Voltage_Limit\n\
uint16 PWM_Limit\n\
uint16 Current_Limit\n\
uint32 Acceleration_Limit\n\
uint32 Velocity_Limit\n\
uint32 Max_Position_Limit\n\
uint32 Min_Position_Limit\n\
uint8  Shutdown\n\
\n\
uint8  Torque_Enable\n\
uint8  LED\n\
uint8  Status_Return_Level\n\
uint8  Registered_Instruction\n\
uint8  Hardware_Error_Status\n\
uint16 Velocity_I_Gain\n\
uint16 Velocity_P_Gain\n\
uint16 Position_D_Gain\n\
uint16 Position_I_Gain\n\
uint16 Position_P_Gain\n\
uint16 Feedforward_2nd_Gain\n\
uint16 Feedforward_1st_Gain\n\
uint8  Bus_Watchdog\n\
int16  Goal_PWM\n\
int16  Goal_Current\n\
int32  Goal_Velocity\n\
uint32 Profile_Acceleration\n\
uint32 Profile_Velocity\n\
uint32 Goal_Position\n\
uint16 Realtime_Tick\n\
uint8  Moving\n\
uint8  Moving_Status\n\
int16  Present_PWM\n\
int16  Present_Load\n\
int16  Present_Current\n\
int32  Present_Velocity\n\
int32  Present_Position\n\
uint32 Velocity_Trajectory\n\
uint32 Position_Trajectory\n\
uint16 Present_Input_Voltage\n\
uint8  Present_Temperature\n\
";
  }

  static const char* value(const ::dynamixel_workbench_msgs::XM_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::dynamixel_workbench_msgs::XM_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.Model_Number);
      stream.next(m.Firmware_Version);
      stream.next(m.ID);
      stream.next(m.Baud_Rate);
      stream.next(m.Return_Delay_Time);
      stream.next(m.Drive_Mode);
      stream.next(m.Operating_Mode);
      stream.next(m.Secondary_ID);
      stream.next(m.Protocol_Version);
      stream.next(m.Homing_Offset);
      stream.next(m.Moving_Threshold);
      stream.next(m.Temperature_Limit);
      stream.next(m.Max_Voltage_Limit);
      stream.next(m.Min_Voltage_Limit);
      stream.next(m.PWM_Limit);
      stream.next(m.Current_Limit);
      stream.next(m.Acceleration_Limit);
      stream.next(m.Velocity_Limit);
      stream.next(m.Max_Position_Limit);
      stream.next(m.Min_Position_Limit);
      stream.next(m.Shutdown);
      stream.next(m.Torque_Enable);
      stream.next(m.LED);
      stream.next(m.Status_Return_Level);
      stream.next(m.Registered_Instruction);
      stream.next(m.Hardware_Error_Status);
      stream.next(m.Velocity_I_Gain);
      stream.next(m.Velocity_P_Gain);
      stream.next(m.Position_D_Gain);
      stream.next(m.Position_I_Gain);
      stream.next(m.Position_P_Gain);
      stream.next(m.Feedforward_2nd_Gain);
      stream.next(m.Feedforward_1st_Gain);
      stream.next(m.Bus_Watchdog);
      stream.next(m.Goal_PWM);
      stream.next(m.Goal_Current);
      stream.next(m.Goal_Velocity);
      stream.next(m.Profile_Acceleration);
      stream.next(m.Profile_Velocity);
      stream.next(m.Goal_Position);
      stream.next(m.Realtime_Tick);
      stream.next(m.Moving);
      stream.next(m.Moving_Status);
      stream.next(m.Present_PWM);
      stream.next(m.Present_Load);
      stream.next(m.Present_Current);
      stream.next(m.Present_Velocity);
      stream.next(m.Present_Position);
      stream.next(m.Velocity_Trajectory);
      stream.next(m.Position_Trajectory);
      stream.next(m.Present_Input_Voltage);
      stream.next(m.Present_Temperature);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct XM_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::dynamixel_workbench_msgs::XM_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::dynamixel_workbench_msgs::XM_<ContainerAllocator>& v)
  {
    s << indent << "Model_Number: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.Model_Number);
    s << indent << "Firmware_Version: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Firmware_Version);
    s << indent << "ID: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.ID);
    s << indent << "Baud_Rate: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Baud_Rate);
    s << indent << "Return_Delay_Time: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Return_Delay_Time);
    s << indent << "Drive_Mode: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Drive_Mode);
    s << indent << "Operating_Mode: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Operating_Mode);
    s << indent << "Secondary_ID: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Secondary_ID);
    s << indent << "Protocol_Version: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Protocol_Version);
    s << indent << "Homing_Offset: ";
    Printer<int32_t>::stream(s, indent + "  ", v.Homing_Offset);
    s << indent << "Moving_Threshold: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.Moving_Threshold);
    s << indent << "Temperature_Limit: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Temperature_Limit);
    s << indent << "Max_Voltage_Limit: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.Max_Voltage_Limit);
    s << indent << "Min_Voltage_Limit: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.Min_Voltage_Limit);
    s << indent << "PWM_Limit: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.PWM_Limit);
    s << indent << "Current_Limit: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.Current_Limit);
    s << indent << "Acceleration_Limit: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.Acceleration_Limit);
    s << indent << "Velocity_Limit: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.Velocity_Limit);
    s << indent << "Max_Position_Limit: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.Max_Position_Limit);
    s << indent << "Min_Position_Limit: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.Min_Position_Limit);
    s << indent << "Shutdown: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Shutdown);
    s << indent << "Torque_Enable: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Torque_Enable);
    s << indent << "LED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.LED);
    s << indent << "Status_Return_Level: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Status_Return_Level);
    s << indent << "Registered_Instruction: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Registered_Instruction);
    s << indent << "Hardware_Error_Status: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Hardware_Error_Status);
    s << indent << "Velocity_I_Gain: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.Velocity_I_Gain);
    s << indent << "Velocity_P_Gain: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.Velocity_P_Gain);
    s << indent << "Position_D_Gain: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.Position_D_Gain);
    s << indent << "Position_I_Gain: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.Position_I_Gain);
    s << indent << "Position_P_Gain: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.Position_P_Gain);
    s << indent << "Feedforward_2nd_Gain: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.Feedforward_2nd_Gain);
    s << indent << "Feedforward_1st_Gain: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.Feedforward_1st_Gain);
    s << indent << "Bus_Watchdog: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Bus_Watchdog);
    s << indent << "Goal_PWM: ";
    Printer<int16_t>::stream(s, indent + "  ", v.Goal_PWM);
    s << indent << "Goal_Current: ";
    Printer<int16_t>::stream(s, indent + "  ", v.Goal_Current);
    s << indent << "Goal_Velocity: ";
    Printer<int32_t>::stream(s, indent + "  ", v.Goal_Velocity);
    s << indent << "Profile_Acceleration: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.Profile_Acceleration);
    s << indent << "Profile_Velocity: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.Profile_Velocity);
    s << indent << "Goal_Position: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.Goal_Position);
    s << indent << "Realtime_Tick: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.Realtime_Tick);
    s << indent << "Moving: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Moving);
    s << indent << "Moving_Status: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Moving_Status);
    s << indent << "Present_PWM: ";
    Printer<int16_t>::stream(s, indent + "  ", v.Present_PWM);
    s << indent << "Present_Load: ";
    Printer<int16_t>::stream(s, indent + "  ", v.Present_Load);
    s << indent << "Present_Current: ";
    Printer<int16_t>::stream(s, indent + "  ", v.Present_Current);
    s << indent << "Present_Velocity: ";
    Printer<int32_t>::stream(s, indent + "  ", v.Present_Velocity);
    s << indent << "Present_Position: ";
    Printer<int32_t>::stream(s, indent + "  ", v.Present_Position);
    s << indent << "Velocity_Trajectory: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.Velocity_Trajectory);
    s << indent << "Position_Trajectory: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.Position_Trajectory);
    s << indent << "Present_Input_Voltage: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.Present_Input_Voltage);
    s << indent << "Present_Temperature: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Present_Temperature);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DYNAMIXEL_WORKBENCH_MSGS_MESSAGE_XM_H