# esp32-robot-controller
# ESP32 Robot Controller 🤖🚗

Wireless robot control using **ESP32**, **L298N motor driver**, and **MicroPython**.
The robot is controlled via **WiFi using a web interface** served directly by the ESP32.

---

## 👤 Author
**Ahmed Dhrifi**  
📧 Email: ahmeddhrifi71@gmail.com  

---

## 🔧 Hardware Used

- ESP32 Dev Module
- L298N Motor Driver
- DC Motors (x2)
- LiPo Battery (recommended: 7.4V with DC-DC regulator)
- Breadboard & Jumper Wires

---

## 📁 Project Structure

esp32-robot-controller/
│── server-motor.py # Main MicroPython code
│── ui.html # Web control interface
│── README.md # Project documentation
## ⚡ Wiring Overview

### ESP32 → L298N
| ESP32 | L298N |
|-----|-------|
| GPIO 25 | IN1 |
| GPIO 26 | IN2 |
| GPIO 27 | IN3 |
| GPIO 14 | IN4 |
| GPIO 32 | ENA (PWM) |
| GPIO 33 | ENB (PWM) |
| GND | GND |
## 🌐 Features

✅ Web-based control (ESP32 Microdot server)  
✅ Forward / Backward / Left / Right  
✅ Combined directions (forward + left/right)  
✅ Speed control using PWM  
✅ Responsive web UI  
✅ Works without a computer after upload  
## 🚀 How to Run

1. Flash **MicroPython** on ESP32  
2. Upload the following files to ESP32:
   - `server-motor.py'
   - 'ui.html'
3. Power the ESP32
4. Connect your phone or PC to the same WiFi
5. Open the ESP32 IP address in a browser
6. Control the robot 🕹️

---

## 🔋 Power Notes

⚠️ Do **NOT** connect 7.4V LiPo directly to ESP32  
✅ Use a **DC-DC buck converter (5V)**  
✅ ESP32, L298N, and battery **must share GND**

---

## 🛠️ Future Improvements

- Camera streaming (ESP32-CAM)
- Autonomous / line-following mode
- MQTT / Cloud control
- Battery voltage monitoring
- Mobile app controller

---

## 📜 License
MIT License – free to use and modify
