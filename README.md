# 📡 Network Status Monitor

A Python-based **Network Status Monitor** that checks the online/offline status of network devices and serves real-time updates via a Flask API.

## 🚀 Project Overview

This project helps monitor the availability of network devices by **pinging them**, storing their status in a JSON file, and providing a simple API to view or update their status.

### 🔹 Features:
- ✅ **Checks network device status** using Python's `subprocess` and `ping`
- ✅ **Stores results in a JSON file** (`status_log.json`)
- ✅ **Flask API to retrieve the latest status**
- ✅ **Manually trigger status checks via API**
- ✅ **Lightweight & easy to use**

---

## ⚙️ Tech Stack
- **Python** 🐍
- **Flask** 🌎
- **Subprocess (ping command)**
- **JSON (for logging status data)**

---

## 🛠 Installation & Setup

1️⃣ **Clone the repository:**
```bash
git clone https://github.com/Edsilva25/NetworkStatusMonitor.git
cd NetworkStatusMonitor
