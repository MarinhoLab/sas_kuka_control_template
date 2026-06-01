from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    simulator_topic = LaunchConfiguration('simulator_topic')

    return LaunchDescription([
        DeclareLaunchArgument(
            'simulator_topic',
            default_value='/kuka_1_sim'
        ),
        Node(
            package='sas_kuka_control_template',
            executable='joint_interface_example.py',
            output='screen',
            emulate_tty=True,
            name='sas_kuka_control_template_joint_interface_example_py',
            parameters=[{
                "robot_topic_name": simulator_topic
            }]
        )
    ])
