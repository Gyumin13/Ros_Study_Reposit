from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_first_ros',
            executable='parameter_node',
            name='parameter_node',
            parameters=[
                {'message': 'Hello from launch file'},
                {'count_limit': 10}
            ]
        )
    ])
