# Vibration-Based-Railway-Track-Health-Monitoring-System

### Overview

This project implements a real-time railway safety monitoring system using the TI CC3200 Wi-Fi-enabled microcontroller. The system detects over-speeding and abnormal vibration using an accelerometer and GPS module, sends instant Wi-Fi alerts, and logs all data to an SD card acting as a blackbox recorder.

### System Components

•	TI CC3200 LaunchPad – ARM Cortex-M4 with integrated Wi-Fi

•	Accelerometer – Vibration and motion sensing

•	NEO-6M GPS Module – Speed and location tracking

•	SD Card Module – Local event logging

•	Python Flask Server – Alert reception and logging

### Working Principle

•	Continuously read acceleration and GPS data.

•	Compute vibration magnitude and monitor train speed.

•	Compare values against predefined thresholds.

•	If threshold exceeded:

Send HTTP alert via Wi-Fi.

Log timestamp, speed, vibration, and GPS location to SD card.

•	Otherwise, continue routine monitoring.

This ensures dual redundancy: wireless alerting + local blackbox storage.
