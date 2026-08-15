cmake_minimum_required(VERSION 3.8)
project(sas_kuka_control_template)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(sas_robot_driver_kuka REQUIRED)

# According to https://github.com/SmartArmStack/sas_robot_driver/blob/ros2/CMakeLists.txt
##### LAUNCH FILES #####

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)

##END## LAUNCH FILES #####

# Python library
ament_python_install_package(${PROJECT_NAME})

#########################
# Scripts Block [BEGIN] #
# https://ros2-tutorial.readthedocs.io/en/latest/
install(DIRECTORY
        scripts/
        FILE_PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ
        DESTINATION lib/${PROJECT_NAME}
)
# ^^^^^^^^^^^^^^^^^^^ #
# Scripts Block [END] #
#######################

ament_package()    
