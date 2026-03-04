# ROS2 Robot Arm MoveIt2 Demo 🚀

Production-ready **ROS2 Jazzy** robot arm with **MoveIt2 path planning**. Built for Deakin University competitive robotics.

![Robot Arm RViz](https://via.placeholder.com/800x400/1e3a8a/ffffff?text=RViz+MoveIt2+Demo)

## 🎯 Features

- ✅ **3-DOF robot arm** (base_yaw, shoulder_pitch, elbow_pitch)
- ✅ **MoveIt2 path planning** with collision checking
- ✅ **RViz visualization** + MotionPlanning panel
- ✅ **Production launch files** (demo + controllers)
- ✅ **Fixed URDF** (cylinders, inertials, joint limits)

## 🚀 Quick Start (2 minutes)

🎮 RViz Controls
Fixed Frame → base_link

MotionPlanning panel → Planning Group arm

Drag end-effector marker → Plan → Execute ✅

🏗️ Architecture
```bash
# Clone and build
git clone https://github.com/atharvamavle/arm-control-demo.git ~/arm_ws/src
cd ~/arm_ws
source /opt/ros/jazzy/setup.bash
colcon build --merge-install
source install/setup.bash

# Launch MoveIt2 demo
ros2 launch robot_arm_moveit_config2 demo.launch.py
your_robot_description/    ← URDF + meshes
robot_arm_moveit_config2/  ← MoveIt2 configs
├── config/
│   ├── joint_limits.yaml
│   ├── kinematics.yaml
│   └── controllers.yaml
├── launch/
│   └── demo.launch.py
└── srdf/robot_arm.srdf    ← Planning groups

📱 Next Features (Planned)
🎮 PS4 controller teleop (MoveIt Servo)

📹 Next.js GUI (4 camera feeds)

⚙️ Real hardware (Dynamixel/Arduino motors)

🔄 Pick & place demo

🔧 Tech Stack

ROS2 Jazzy -  MoveIt2 -  ros2_control -  RViz2 -  Python3

