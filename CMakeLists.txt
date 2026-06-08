cmake_minimum_required(VERSION 3.8)
project(sas_kuka_control_template)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(sas_robot_driver_kuka REQUIRED)

# According to https://github.com/SmartArmStack/sas_robot_driver/blob/ros2/CMakeLists.txt
##### LAUNCH FILES #####

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)

##END## LAUNCH FILES #####

# According to https://github.com/SmartArmStack/sas_datalogger/blob/78ac681f9cb049c5b9715d215f163565f16b5cdc/CMakeLists.txt
##### PYTHON EXECUTABLES #####
install(PROGRAMS
  scripts/joint_interface_example.py
  scripts/kinematic_control.py
  DESTINATION lib/${PROJECT_NAME}
)
##END## PYTHON EXECUTABLES #####

ament_package()    
