"""This is a launch file that calls the two launch files and the example script to make the simulated robot
move in CoppeliaSim. For more details, refer to the repository's README.md"""

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, GroupAction
from launch_ros.actions import SetRemap, Node
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    robot_example_py_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('sas_kuka_control_template'), 'launch'),
            '/robot_example_py_launch.py'])
    )

    # The topic has been created in the script inside CoppeliaSim so we have to relay instead of remap.
    ## https://github.com/ros-tooling/topic_tools/blob/rolling/topic_tools/src/relay_node.cpp
    relay_node = Node(
        package='topic_tools',
        executable='relay_node',
        name='kuka_1_relay',
        parameters=[{
            "input_topic": "/sas_robot_driver_coppeliasim/LBR_iiwa_14_R820/set/target_joint_positions",
            "output_topic": "/kuka_1/set/target_joint_positions"
        }]
    ),

    return LaunchDescription([
        robot_example_py_launch,
        relay_node
    ])
