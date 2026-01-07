# 🌐 IoT-Vision — Real-Time Sensor Data Dashboard

> *Turning live sensor data into meaningful insights — in real time.*

---

## 📌 Project Overview

**IoT-Vision** is a real-time IoT monitoring dashboard built using **Python, MQTT, and Plotly Dash**.  
It subscribes to an MQTT broker, receives live **temperature and humidity** data from sensors, and visualizes it using **interactive gauges and trend graphs**.

This project demonstrates **end-to-end IoT data flow** — from message ingestion to real-time visualization — making it ideal for learning and showcasing IoT + Data Visualization skills.

---

## ✨ Key Highlights

| Feature | Description |
|------|------------|
| 🔄 Real-Time Updates | Live data updates every few seconds |
| 📡 MQTT Integration | Subscribes to MQTT topics for sensor data |
| 🌡️ Live Gauges | Temperature & humidity gauges |
| 📈 Trend Graphs | Line charts showing sensor history |
| 🧵 Thread-Safe | Uses threading for stable MQTT handling |
| 🎨 Clean UI | Minimal, modern Dash interface |

---

## 🛠️ Tech Stack

| Category | Technologies |
|-------|-------------|
| Programming Language | Python 🐍 |
| Communication Protocol | MQTT |
| Dashboard Framework | Dash |
| Visualization | Plotly (Graph Objects & Express) |
| Data Handling | Pandas |
| Concurrency | Threading |

---

## 📂 Project Structure

```text
📁 IoT-Vision/
│
├── 📄 app.py                # Main dashboard & MQTT logic
├── 📄 README.md             # Project documentation
├── 📄 requirements.txt      # Required Python libraries
