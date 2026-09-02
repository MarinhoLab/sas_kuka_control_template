"""Refer to the repository's README.md"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    config_file = LaunchConfiguration('config_file')

    return LaunchDescription([
        DeclareLaunchArgument(
            'config_file',
            default_value=os.path.join(get_package_share_directory('sas_kuka_control_template'), 'config', 'config.yaml')
        ),
        Node(
            package='sas_kuka_control_template',
            executable='kinematic_control.py',
            output='screen',
            emulate_tty=True,
            name='sas_kuka_control_template_kinematic_control',
            parameters=[config_file]
        )
    ])
