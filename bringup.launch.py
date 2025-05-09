from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hexapod_control',
            executable='gait_node',
            output='screen'
        ),
        Node(
            package='hexapod_control',
            executable='imu_node',
            output='screen'
        )
    ])
