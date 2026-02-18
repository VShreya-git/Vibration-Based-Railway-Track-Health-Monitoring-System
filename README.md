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

### Firmware Implementation

Developed using Energia (C/C++).

Libraries used:

•	WiFi.h

•	WiFiClient.h

•	math.h

•	UART interface for GPS

•	SPI interface for SD logging

The firmware handles:

•	ADC sampling

•	RMS-like vibration magnitude calculation

•	Threshold comparison

•	HTTP GET alert generation

•	Structured log storage

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
