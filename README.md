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

•	Start the system and initialize all sensors, Wi-Fi, and SD card modules. 

•	Read sensor values from accelerometer and piezo sensors. 

•	Acquire GPS data (speed, latitude, longitude). 

•	Check conditions: 
•	If speed > threshold → set overspeed_flag = true. 
•	If vibration > threshold → set vibration_flag = true. 

•	If either flag is true: 
•	Prepare alert message with all details. 
•	Send alert to remote server via Wi-Fi. 
•	Log data with timestamp into the SD card. 

•	If both conditions are normal: 
•	Continue logging routine readings for reference.

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
