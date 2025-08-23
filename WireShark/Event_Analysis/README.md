# 🕵️ Wireshark Labs & Event Analysis

Welcome to the **Wireshark section** of the CyberSec Labs repository.  
This section focuses on **network traffic analysis**, **protocol dissection**, and **event investigation** using Wireshark.  

---

## 📂 Directory Structure
CyberSec/
└── Wireshark/
├── README.md # Overview of Wireshark labs
├── TLS_Analysis.md # TLS traffic analysis lab
├── Event_Analysis/ # Security event analysis case studies
│ ├── Brute_Force.md
│ ├── DNS_Tunneling.md
│ ├── Malware_Traffic.md
│ ├── Phishing.md
│ └── Data_Exfiltration.md
└── images/ # Screenshots and diagrams

yaml
Copy
Edit

---

## 📘 Lab Guides

- [TLS Analysis](./TLS_Analysis.md) – Understand TLS handshakes, certificate inspection, and encrypted sessions.  
- [Event Analysis](./Event_Analysis/) – Deep-dive case studies of attacks and anomalies.

---

## 🔍 Event Analysis Topics
Inside the **Event_Analysis/** folder, you will find detailed walkthroughs:

- [Brute Force Detection](./Event_Analysis/Brute_Force.md)  
- [DNS Tunneling](./Event_Analysis/DNS_Tunneling.md)  
- [Malware Traffic](./Event_Analysis/Malware_Traffic.md)  
- [Phishing Attack](./Event_Analysis/Phishing.md)  
- [Data Exfiltration](./Event_Analysis/Data_Exfiltration.md)  

---

## 📸 Screenshots
All screenshots are stored in the [`images/`](./images/) folder for reference.  
Example:  

![Wireshark Screenshot](./images/wireshark_overview.png)

---

## 🚀 Next Steps
- Expand each case study with **realistic PCAP captures**.  
- Add **filter cheatsheets** (`http`, `tcp.flags.syn==1 && tcp.flags.ack==0`, etc.).  
- Provide **analysis challenges** for practice.  

---
