# SpiderBot

![platform](https://img.shields.io/badge/platform-Raspberry%20Pi-blue)
![status](https://img.shields.io/badge/status-WIP-orange)
![license](https://img.shields.io/badge/license-MIT-green)
![AI](https://img.shields.io/badge/ai-YOLOv5n%20%2B%20Coral%20USB-brightgreen)

> A terrain-capable, vision-guided hexapod robot that carries payloads, tracks objects, and navigates autonomously — built with Raspberry Pi 5, Coral USB, STM32, and ROS2.

---

## 🧠 Features

- 🤖 **3DOF Hexapod** – 18-DOF servo system (35KG torque), 5kg payload capacity
- 🧭 **Autonomous Locomotion** – ROS2-based gait generation, terrain-ready
- 🛠️ **Modular Frame** – Custom-designed in SolidWorks, 3D-printed and torque-optimized
- 🧠 **AI Vision** – YOLOv5n object detection accelerated with Coral USB
- 🧩 **Multi-Processor System** – STM32/ESP32 for real-time servo control, Pi for high-level ROS2 tasks
- 🌐 **Sensor Fusion** – Optional IMU + Lidar integration for navigation

---

## 🧰 Tech Stack

- **Languages**: Python 3.9+, C/C++
- **Middleware**: ROS2 Humble, micro-ROS, UART
- **AI**: YOLOv5n (TFLite quantized), Coral USB Accelerator, OpenCV
- **Microcontrollers**: STM32 (Nucleo), ESP32
- **Hardware**: Raspberry Pi 5, 35KG Serial Bus Servos, IMU, USB Camera
- **Mechanical Design**: SolidWorks (frame, servo mounts)
- **Power**: 3S LiPo Battery, UBEC, XT60 harness
- **Tools**: VS Code, PlatformIO, Git, RViz2

---

## 📁 Repo Structure

```
SpiderBot/
├── ros2_ws/              # ROS2 workspace
│   └── src/
│       └── hexapod_control/
│           ├── launch/
│           ├── hexapod_control/
│           │   ├── gait_node.py
│           │   ├── imu_node.py
│           │   └── serial_bridge.py
├── vision/               # Coral USB AI detection
│   ├── detect.py
│   └── tflite_model/
├── firmware/             # STM32 gait control code
│   └── main.c
├── solidworks/           # CAD source files
├── utils/                # UART & helper tools
├── README.md
└── requirements.txt
```

---

## 🚀 Quick Start

1. Flash STM32 with `main.c` (via STM32CubeIDE or PlatformIO)
2. Build and source ROS2 workspace:
```bash
cd ros2_ws && colcon build
source install/setup.bash
ros2 launch hexapod_control bringup.launch.py
```
3. Run object detection:
```bash
python3 vision/detect.py
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
