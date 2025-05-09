# Placeholder for IMU node
import rclpy
from rclpy.node import Node

class ImuNode(Node):
    def __init__(self):
        super().__init__('imu_node')
        self.get_logger().info("IMU node initialized")

def main():
    rclpy.init()
    rclpy.spin(ImuNode())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
