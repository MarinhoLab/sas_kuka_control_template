"""Refer to the repository's README.md"""

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sas_kuka_control_template',
            executable='joint_interface_example.py',
            output='screen',
            emulate_tty=True,
            name='sas_kuka_control_template_joint_interface_example_py',
            parameters=[{
                "robot_topic_name": "sas_robot_driver_coppeliasim/LBR_iiwa_14_R820"
            }]
        )
    ])
