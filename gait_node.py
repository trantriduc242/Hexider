import rclpy
from rclpy.node import Node
import serial

class GaitNode(Node):
    def __init__(self):
        super().__init__('gait_node')
        self.ser = serial.Serial('/dev/ttyUSB0', 115200)
        self.timer = self.create_timer(1.0, self.send_command)

    def send_command(self):
        self.ser.write(b'walk_tripod\n')

def main():
    rclpy.init()
    rclpy.spin(GaitNode())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
