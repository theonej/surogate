project(steering)

find_package(catkin REQUIRED COMPONENTS
   roscpp
   rospy
   std_msgs
   message_generation
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

add_message_files(
  FILES
  steerCommand.msg
)

catkin_package(
  CATKIN_DEPENDS message_runtime
)

