project(steering)

find_package(catkin REQUIRED COMPONENTS
   roscpp
   rospy
   std_msgs
   message_generation
)

add_message_files(
  FILES
  steerCommand.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

add_service_files(
    FILES
    steeringService.srv
)
catkin_package(
  CATKIN_DEPENDS message_runtime
)

