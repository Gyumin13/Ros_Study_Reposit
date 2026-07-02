import math

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class WallAvoidTurtleNode(Node):
    def __init__(self):
        super().__init__('wall_avoid_turtle_node')
        self.declare_parameter('forward_speed', 0.8)
        self.declare_parameter('near_wall_speed', 0.5)
        self.declare_parameter('turn_gain', 4.0)
        self.declare_parameter('wall_limit', 3.0)
        self.declare_parameter('center_x', 5.5)
        self.declare_parameter('center_y', 5.5)
        self.create_subscription(Pose, '/turtle1/pose', self.on_pose, 10)
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def normalize_angle(self, angle):
        return math.atan2(math.sin(angle), math.cos(angle))

    def on_pose(self, pose):
        wall_limit = self.get_parameter('wall_limit').value
        center_x = self.get_parameter('center_x').value
        center_y = self.get_parameter('center_y').value
        forward_speed = self.get_parameter('forward_speed').value
        near_wall_speed = self.get_parameter('near_wall_speed').value
        turn_gain = self.get_parameter('turn_gain').value

        near_wall = (
            pose.x < wall_limit or pose.x > 11.0 - wall_limit or
            pose.y < wall_limit or pose.y > 11.0 - wall_limit
        )

        cmd = Twist()
        if near_wall:
            target_angle = math.atan2(center_y - pose.y, center_x - pose.x)
            angle_error = self.normalize_angle(target_angle - pose.theta)
            cmd.linear.x = near_wall_speed
            cmd.angular.z = turn_gain * angle_error
        else:
            cmd.linear.x = forward_speed

        self.publisher.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = WallAvoidTurtleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
