import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class AutoTurtleNode(Node):
    def __init__(self):
        super().__init__('auto_turtle_node')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.publish_velocity)
        self.count = 0

    def publish_velocity(self):
        msg = Twist()
        if self.count < 10:
            msg.linear.x = 2.0
        else:
            msg.angular.z = 1.5
        self.publisher_.publish(msg)
        self.count = (self.count + 1) % 20


def main(args=None):
    rclpy.init(args=args)
    node = AutoTurtleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
