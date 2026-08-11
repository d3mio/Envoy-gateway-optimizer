# 🖥️ Envoy Gateway Studio — Visual Service Mesh & Route Config GUI

> Graphical desktop dashboard for Envoy service mesh route optimization, latency metrics, and circuit breakers.

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![GUI Type](https://img.shields.io/badge/interface-Visual%20GUI-purple.svg)

---

## ✨ Features

- **Visual Desktop GUI Interface**: Built with Python Tkinter dark theme aesthetics.
- **Interactive Control Panel**: Real-time action triggers, visual sliders, and parameter inputs.
- **Graphical Displays**: Tabular data views, live progress gauges, and real-time status monitors.
- **Zero Configuration**: Ready out-of-the-box with default mock feeds and fallback modes.

---

## 📋 Prerequisites

- **Python 3.10+** installed on your system.
- `pip` package manager.
- `tkinter` support (included by default with standard Python installations).

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/d3mio/Envoy-gateway-optimizer.git
cd Envoy-gateway-optimizer
```

### 2. Create and Activate Virtual Environment (Recommended)
- **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **Windows**:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🎮 How to Launch the Visual GUI Application

Run the main application script:

```bash
python gui_app.py
```

This will launch the desktop graphical user interface window!

---

## 🎮 GUI Controls & Usage Guide

1. **Top Header**: Displays system status and active port/connection telemetry.
2. **Interactive Controls**: Enter custom target paths, API keys, or test configurations in the input fields.
3. **Execution Button**: Click **`⚡ Run Action`** to trigger live processing.
4. **Visual Results Grid**: Inspect findings, metrics, and severity scores in the interactive table view.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
