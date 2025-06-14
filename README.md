# 🕵️‍♂️ CodeAlpha – Basic Network Sniffer (Task 1)

## 🧑‍💻 Intern Name: Mohan  
**Task:** Task 1 - Basic Network Sniffer  
**Internship:** CodeAlpha Cybersecurity Internship  
**Repository:** CodeAlpha_BasicNetworkSniffer

---

## 🎯 Objective

This project involves building a **basic Python program** that captures and analyzes **network traffic packets**. The goal is to understand how data flows across the network and get hands-on experience with packet sniffing using the `scapy` library.

---

## 🛠 Tools & Technologies

- Python 3.10+
- Scapy (`pip install scapy`)
- Wireshark (for comparison/testing)
- VS Code

---

## ⚙️ Features

- Captures live packets on a specified network interface  
- Extracts and displays:
  - Source IP address  
  - Destination IP address  
  - Protocol type  
  - Raw payload (optional)

- Supports filtering by protocol
- Lightweight and terminal-based

---

## 📦 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/CodeAlpha_BasicNetworkSniffer
cd CodeAlpha_BasicNetworkSniffer

# 2. Install dependencies
pip install scapy

# 3. Run the sniffer
sudo python3 sniffer.py
