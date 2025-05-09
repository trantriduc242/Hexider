# UART utility for serial communication with STM32 or ESP32
import serial

def send_command(port='/dev/ttyUSB0', baud=115200, message='walk_tripod'):
    with serial.Serial(port, baud, timeout=1) as ser:
        ser.write((message + '\n').encode())
        print(f"Sent: {message}")

def read_response(port='/dev/ttyUSB0', baud=115200):
    with serial.Serial(port, baud, timeout=1) as ser:
        if ser.in_waiting:
            return ser.readline().decode().strip()
    return None
