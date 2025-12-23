# 🚗 Workshop Automation System (ANPR)

This repository contains a **real-time vehicle entry–exit automation system** designed for service workshops.  
The system uses **CCTV (RTSP stream)** and **OCR-based number plate recognition** to automatically log vehicle entry and exit timings into a **MySQL database**.

The application is designed to run **24×7** with minimal delay and is structured in a **modular and scalable way** for future upgrades.
---
## 🔹 Key Features

- 📡 Live CCTV (RTSP) stream processing
- 🔍 Automatic number plate recognition using PaddleOCR
- 🚘 Supports **Normal** and **BH-series** number plates
- ⏱️ Automatic vehicle entry & exit time calculation
- 🗄️ MySQL database integration
- 🔁 Safe handling of repeated detections (prevents false exits)
- 🧩 Modular Python code structure
- 🖥️ Works on **Windows & Linux**
- 🚀 Ready for future AI upgrades (YOLO / Faster R-CNN)
---
## 📂 Repository Structure
Workshop-automation

│

├── main.py # Application entry point

├── camera.py # RTSP camera handling

├── ocr_module.py # OCR preprocessing & text extraction

├── vehicle_logic.py # Entry–exit decision logic

├── database.py # MySQL connection & queries

├── config.py # Configuration settings

├── requirements.txt # Python dependencies

└── README.md # Project documentation

 Install dependencies:
 pip install -r requirements.txt

Future Enhancements
  Vehicle & number plate detection using YOLO / Faster R-CNN
  Multi-gate support
  Direction-based entry/exit validation
  Web dashboard and analytics
  REST API integration

