# Self-Balancing Robot Using Fuzzy Logic Controller

## Overview

This project implements a two-wheeled self-balancing robot using an ESP32 microcontroller and an MPU6050 IMU sensor. The robot maintains its balance by continuously measuring its tilt angle and applying a Fuzzy Logic Controller (FLC) to determine the appropriate motor speed and direction.

The system is designed to keep the robot upright by minimizing the error between the desired angle (0°) and the measured tilt angle.

---

## Features

- Real-time balancing using Fuzzy Logic Control
- MPU6050 sensor for angle measurement
- ESP32-based controller
- PID-free control algorithm
- PWM motor speed control
- Forward and backward balancing
- Serial Monitor for debugging and monitoring

---

## Hardware Requirements

- ESP32 Development Board
- MPU6050 Gyroscope & Accelerometer
- L298N Motor Driver
- 2 DC Geared Motors
- Robot Chassis
- Lithium Battery (7.4V or equivalent)
- Jumper Wires

---

## Software Requirements

- Arduino IDE
- ESP32 Board Package
- Required Libraries:
  - Wire.h
  - MPU6050 library
  - Fuzzy Logic library (if used)
  - Other dependencies included in the project

---

## Project Structure

```
Self-Balancing-Robot/
│
├── src/
│   ├── main.ino
│   ├── fuzzy_controller.cpp
│   ├── fuzzy_controller.h
│   ├── motor_control.cpp
│   ├── motor_control.h
│   └── sensor.cpp
│
├── include/
│
├── images/
│
├── docs/
│
└── README.md
```

---

## Working Principle

1. MPU6050 measures the robot's tilt angle.
2. ESP32 reads sensor data continuously.
3. The Fuzzy Logic Controller calculates the angle error.
4. Based on the fuzzy rules, the controller determines the motor output.
5. The motors rotate in the required direction to restore the robot's balance.
6. The process repeats continuously in real time.

---

## Fuzzy Logic Controller

### Inputs

- Error (Tilt Angle)
- Delta Error (Change of Error)

### Output

- Motor PWM Speed

The controller uses a rule base to determine the appropriate motor response based on the robot's current position.

---

## Wiring Diagram

| Component | ESP32 Pin |
|-----------|-----------|
| MPU6050 SDA | GPIO 21 |
| MPU6050 SCL | GPIO 22 |
| L298N IN1 | GPIO xx |
| L298N IN2 | GPIO xx |
| L298N IN3 | GPIO xx |
| L298N IN4 | GPIO xx |
| ENA | PWM GPIO xx |
| ENB | PWM GPIO xx |

Replace **xx** with the actual GPIO numbers used in your project.

---

## Installation

1. Clone this repository.

```bash
git clone https://github.com/yourusername/self-balancing-robot.git
```

2. Open the project in Arduino IDE.

3. Install all required libraries.

4. Select the correct ESP32 board.

5. Upload the program.

6. Open the Serial Monitor to observe sensor values and controller output.

---

## Future Improvements

- Bluetooth control
- Wi-Fi monitoring
- Automatic calibration
- Better sensor fusion using Kalman Filter
- Mobile application integration

---

## Authors

Developed as a Final Project by students of Industrial Electronics Engineering.

---

## License

This project is intended for educational and research purposes.
