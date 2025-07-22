# 🛡️ Network Traffic Analyzer

A modular Python-based network traffic analyzer built from scratch to support cybersecurity monitoring, logging, and visualization. Designed to capture real-time packets, parse them, detect suspicious behaviors, log detailed insights, and visualize traffic patterns.

---

## 🚀 Features

- 🔎 **Packet Capture** – Real-time packet sniffing using Scapy
- 🧩 **Parser Module** – Extracts source/destination IPs, ports, protocols
- 📊 **Analyzer Module** – Detects anomalies like port scans and suspicious spikes
- 🗃️ **Logger Module** – Saves logs in JSON format for review
- 📈 **Visualizer Module** – Uses Matplotlib to generate traffic graphs
- 💡 Modular architecture – Easy to extend and integrate with other tools

---

## 🧠 How It Works

The system is broken into modular components:

1. **Capture Module** – Captures packets from the selected interface.
2. **Parser Module** – Extracts structured info (IPs, ports, protocols).
3. **Analyzer Module** – Detects suspicious behaviors and aggregates stats.
4. **Logger Module** – Stores parsed packets and analysis reports in JSON logs.
5. **Visualizer Module** – Loads logs and visualizes protocol/IP/port distributions.

---

## 📦 Requirements

Install required dependencies:
