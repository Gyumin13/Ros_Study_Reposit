import rclpy
from rclpy.node import Node


class TimerNode(Node):
    def __init__(self):
        super().__init__('timer_node')
        self.count = 0
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Timer Node has started.')

    def timer_callback(self):
        self.count += 1
        self.get_logger().info(f'Hello ROS 2 Timer: {self.count}')


def main(args=None):
    rclpy.init(args=args)
    node = TimerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
