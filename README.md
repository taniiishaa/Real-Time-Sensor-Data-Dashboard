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

```
##📡 Expected MQTT Data Format

The dashboard expects sensor data in the following JSON format:

```text
{
  "temp": 25.5,
  "hum": 60
}

```
Make sure your IoT device or simulator publishes data in this format.

##⚙️ Configuration

You can configure the MQTT connection directly from the UI:

| Parameter |	Description |
|------|------|
| Broker IP |	MQTT broker address |
|Port	|Default: 1883 |
| Topic	| MQTT topic for sensor data |

---

Default values are pre-filled for convenience.

## ▶️ How to Run the Project

# 1️⃣ Install Dependencies
```text
pip install -r requirements.txt
```

# 2️⃣ Run the Application
```text
python app.py
```

# 3️⃣ Open in Browser
```text
http://localhost:8051
```

## 📊 Dashboard Components

| Component | Purpose |
|------|------|
| Temperature Gauge	| Displays latest temperature value |
| Humidity Gauge |	Displays latest humidity value |
| Temperature Trend | Shows temperature over time |
| Humidity Trend |	Shows humidity over time |
| Live Clock | Shows last update time |

---

##🧠 Learning Outcomes

This project helps you understand:
- MQTT publish-subscribe architecture
- Real-time data handling in Python
- Dash callbacks & UI components
- Thread-safe data sharing

Interactive data visualization using Plotly

##🚀 Use Cases

- IoT sensor monitoring
- Smart home dashboards
- Environmental tracking
- Academic & mini-projects
- IoT + Data Visualization demos

##🧩 Future Enhancements

- 📱 Mobile-responsive UI
- ☁️ Cloud MQTT broker support
- 💾 Database storage
- 📊 More sensor types
- 🔔 Alert system for threshold values

##👩‍💻 Author

Tanisha Chaudhary
-🎓 B.Tech CSE Student
-💡 Aspiring Software Engineer
-📍 Haryana, India

##⭐ Show Some Love

If you found this project helpful or inspiring:
- ⭐ Star this repository
- 🍴 Fork it
- 🧠 Learn & build on it
