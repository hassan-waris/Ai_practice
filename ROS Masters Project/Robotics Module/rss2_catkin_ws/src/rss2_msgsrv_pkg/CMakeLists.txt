cmake_minimum_required(VERSION 3.0.2)
project(rss2_msgsrv_pkg)


find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  nav_msgs
  rospy
  std_msgs
  message_generation
)


## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   date_cmd_vel.msg
#   Message2.msg
 )

## Generate services in the 'srv' folder
 add_service_files(
   FILES
   srv_turtlebot3_move.srv
#   Service2.srv
 )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   geometry_msgs   
   nav_msgs   
   std_msgs
 )

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES rss2_msgsrv_pkg
  CATKIN_DEPENDS geometry_msgs nav_msgs rospy std_msgs message_runtime
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

