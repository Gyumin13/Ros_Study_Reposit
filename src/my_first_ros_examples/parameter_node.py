import rclpy
from rclpy.node import Node


class ParameterNode(Node):
    def __init__(self):
        super().__init__('parameter_node')

        self.declare_parameter('message', 'Hello ROS 2 Parameter')
        self.declare_parameter('count_limit', 5)

        self.count = 0
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Parameter Node has started.')

    def timer_callback(self):
        message = self.get_parameter('message').value
        count_limit = self.get_parameter('count_limit').value

        self.count += 1
        self.get_logger().info(f'[{self.count}/{count_limit}] message: {message}')

        if self.count >= count_limit:
            self.get_logger().info('count_limit reached. Count reset.')
            self.count = 0


def main(args=None):
    rclpy.init(args=args)
    node = ParameterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
