# Serial bridge between Raspberry Pi and STM32
import rclpy
from rclpy.node import Node
import serial

class SerialBridgeNode(Node):
    def __init__(self):
        super().__init__('serial_bridge')
        self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        self.get_logger().info("Serial bridge initialized")
        self.timer = self.create_timer(0.5, self.read_serial)

    def read_serial(self):
        if self.ser.in_waiting:
            data = self.ser.readline().decode().strip()
            self.get_logger().info(f"Received from STM32: {data}")

def main():
    rclpy.init()
    rclpy.spin(SerialBridgeNode())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
