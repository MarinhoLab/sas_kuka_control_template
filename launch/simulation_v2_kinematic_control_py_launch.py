"""Refer to the repository's README.md"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    xd_topic_name = LaunchConfiguration('xd_topic_name')
    simulator_topic = LaunchConfiguration('simulator_topic')

    return LaunchDescription([
        DeclareLaunchArgument(
            'xd_topic_name',
            default_value='/frame_xd'
        ),
        DeclareLaunchArgument(
            'simulator_topic',
            default_value='/kuka_1_sim'
        ),
        Node(
            package='sas_kuka_control_template',
            executable='kinematic_control.py',
            output='screen',
            emulate_tty=True,
            name='sas_kuka_control_template_joint_interface_example_py',
            parameters=[{
                "robot_topic_name": simulator_topic,
                "xd_topic_name": xd_topic_name
            }]
        )
    ])
