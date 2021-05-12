# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "abel: 3 messages, 3 services")

set(MSG_I_FLAGS "-Iabel:/home/gabriele/catkin_ws/src/abel/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators

add_custom_target(abel_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/gabriele/catkin_ws/src/abel/msg/SetPosition.msg" NAME_WE)
add_custom_target(_abel_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "abel" "/home/gabriele/catkin_ws/src/abel/msg/SetPosition.msg" ""
)

get_filename_component(_filename "/home/gabriele/catkin_ws/src/abel/msg/SyncSetPosition.msg" NAME_WE)
add_custom_target(_abel_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "abel" "/home/gabriele/catkin_ws/src/abel/msg/SyncSetPosition.msg" ""
)

get_filename_component(_filename "/home/gabriele/catkin_ws/src/abel/msg/BulkSetItem.msg" NAME_WE)
add_custom_target(_abel_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "abel" "/home/gabriele/catkin_ws/src/abel/msg/BulkSetItem.msg" ""
)

get_filename_component(_filename "/home/gabriele/catkin_ws/src/abel/srv/GetPosition.srv" NAME_WE)
add_custom_target(_abel_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "abel" "/home/gabriele/catkin_ws/src/abel/srv/GetPosition.srv" ""
)

get_filename_component(_filename "/home/gabriele/catkin_ws/src/abel/srv/SyncGetPosition.srv" NAME_WE)
add_custom_target(_abel_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "abel" "/home/gabriele/catkin_ws/src/abel/srv/SyncGetPosition.srv" ""
)

get_filename_component(_filename "/home/gabriele/catkin_ws/src/abel/srv/BulkGetItem.srv" NAME_WE)
add_custom_target(_abel_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "abel" "/home/gabriele/catkin_ws/src/abel/srv/BulkGetItem.srv" ""
)

#
#  langs = 
#


