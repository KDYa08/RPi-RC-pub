cmake_minimum_required(VERSION 3.0.2)
project(pub_sub_dialog)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)
catkin_python_setup()

generate_messages(
    DEPENDENCIES
    std_msgs
)

catkin_package(
  CATKIN_DEPENDS
    rospy
    std_msgs
    message_runtime
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  nodes/listener
  nodes/talker
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
