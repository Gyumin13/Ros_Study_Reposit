import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class SquareTurtleNode(Node):
    def __init__(self):
        super().__init__('square_turtle_node')
        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )
        self.timer = self.create_timer(0.5, self.publish_velocity)
        self.step = 0
        self.get_logger().info('Square Turtle Node has started.')

    def publish_velocity(self):
        msg = Twist()
        current_step = self.step % 8

        if current_step in [0, 2, 4, 6]:
            msg.linear.x = 2.0
            msg.angular.z = 0.0
        else:
            msg.linear.x = 0.0
            msg.angular.z = 1.57

        self.publisher_.publish(msg)
        self.step += 1


def main(args=None):
    rclpy.init(args=args)
    node = SquareTurtleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
