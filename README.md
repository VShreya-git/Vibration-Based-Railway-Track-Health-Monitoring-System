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

1. Start the system and initialize all sensors, Wi-Fi, and SD card modules. 

2. Read sensor values from accelerometer and piezo sensors. 

3. Acquire GPS data (speed, latitude, longitude). 

4. Check conditions: 
o If speed > threshold → set overspeed_flag = true. 
o If vibration > threshold → set vibration_flag = true. 

5. If either flag is true: 
o Prepare alert message with all details. 
o Send alert to remote server via Wi-Fi. 
o Log data with timestamp into the SD card. 

6. If both conditions are normal: 
o Continue logging routine readings for reference.

### Firmware Implementation

Developed using Energia (C/C++).

Libraries used:

•	WiFi.h -  for establishing and managing Wi-Fi connections between the CC3200 and a wireless network. 

•	WiFiClient.h -  for creating a client instance that can send alert messages and data packets to a remote server or cloud platform using standard protocols such as HTTP or TCP. 

•	math.h - for performing essential mathematical operations, such as calculating RMS values, averages, and filtering raw accelerometer data to identify vibration magnitude.

### Server Implementation

A lightweight Python Flask server:

•	Receives HTTP alerts

•	Logs events to file

•	Sends Telegram notifications

•	Maintains event history

•	Enables scalable integration with dashboards or cloud systems.

### Results & Observations

•	GPS provides reliable outdoor speed/location.

•	CC3200 handles concurrent tasks without performance degradation.

•	Alerts are transmitted instantly on threshold violation.

•	SD card logging ensures data persistence during network failure.

The system demonstrates reliable real-time monitoring suitable for railway safety applications.
