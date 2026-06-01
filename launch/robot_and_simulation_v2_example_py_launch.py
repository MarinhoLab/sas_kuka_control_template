"""This is a launch file that calls the two launch files and the example script to make the simulated robot
move in CoppeliaSim. For more details, refer to the repository's README.md"""

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, GroupAction
from launch_ros.actions import SetRemap, Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    robot_example_py_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('sas_kuka_control_template'), 'launch'),
            '/robot_example_py_launch.py'])
    )

    robot_topic = LaunchConfiguration('robot_topic')
    simulator_topic = LaunchConfiguration('simulator_topic')

    return LaunchDescription([
        DeclareLaunchArgument(
            'robot_topic',
            default_value='/kuka_1'
        ),
        DeclareLaunchArgument(
            'simulator_topic',
            default_value='/kuka_1_sim'
        ),
        robot_example_py_launch,
        Node(
            package='topic_tools',
            executable='relay_node',
            name='kuka_1_relay',
            parameters=[{
                "input_topic": f"{simulator_topic}/set/target_joint_positions",
                "output_topic": f"{robot_topic}/set/target_joint_positions"
            }]
        ),
    ])
