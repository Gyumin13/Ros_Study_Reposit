from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    publisher = Node(
        package='my_first_ros',
        executable='publisher_node',
        name='my_publisher'
    )

    subscriber = Node(
        package='my_first_ros',
        executable='subscriber_node',
        name='my_subscriber'
    )

    return LaunchDescription([
        publisher,
        subscriber
    ])
