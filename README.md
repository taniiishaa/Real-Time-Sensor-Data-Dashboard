# 🌐 Real-Time-Sensor-Data-Dashboard

> *A live IoT dashboard that transforms real-time sensor data into clear, interactive visual insights.*

---

## 📌 Project Overview

**Real-Time-Sensor-Data-Dashboard** is a Python-based IoT monitoring application that visualizes **live temperature and humidity data** using an interactive web dashboard.

The system subscribes to an **MQTT broker**, receives sensor data in real time, and displays it through **gauges and trend graphs** using **Dash and Plotly**.  
This project demonstrates the complete IoT pipeline — from data ingestion to real-time visualization.

---

## ✨ Key Features

| Feature | Description |
|------|------------|
| 🔄 Real-Time Updates | Automatically refreshes live sensor data |
| 📡 MQTT Connectivity | Subscribes to MQTT topics |
| 🌡️ Live Gauges | Displays current temperature & humidity |
| 📈 Trend Charts | Shows historical data in line graphs |
| 🧵 Thread-Safe Design | Stable data handling using threading |
| 🎨 Clean UI | Simple, minimal, and user-friendly interface |

---

## 🛠️ Tech Stack

| Category | Tools |
|------|------|
| Programming Language | Python 🐍 |
| Communication Protocol | MQTT |
| Dashboard Framework | Dash |
| Data Visualization | Plotly |
| Data Processing | Pandas |
| Concurrency | Threading |

---

## 📂 Project Structure

```text
📁 Real-Time-Sensor-Data-Dashboard/
│
├── 📄 iot_dashboard.py     # Main MQTT logic & Dash application
├── 📄 requirements.txt     # Python dependencies
├── 📄 .gitignore           # Ignored files for Git
├── 📄 README.md            # Project documentation
