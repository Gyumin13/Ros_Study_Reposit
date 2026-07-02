from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim'
    )

    wall_avoid_node = Node(
        package='my_first_ros',
        executable='wall_avoid_turtle_node',
        name='wall_avoid_turtle_node',
        parameters=[
            {
                'forward_speed': 0.8,
                'near_wall_speed': 0.5,
                'turn_gain': 4.0,
                'wall_limit': 3.0,
                'center_x': 5.5,
                'center_y': 5.5,
            }
        ]
    )

    return LaunchDescription([
        turtlesim_node,
        wall_avoid_node
    ])
