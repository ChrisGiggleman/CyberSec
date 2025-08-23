# 🕵️ Wireshark Labs & Event Analysis

Welcome to the **Wireshark section** of the CyberSec Labs repository.  
This section focuses on **network traffic analysis**, **protocol dissection**, and **event investigation** using Wireshark.  

---

# 🔍 Event Analysis with Wireshark

This section covers detailed investigations of different types of attacks and anomalies using Wireshark. Each subsection contains a dedicated lab guide with packet captures, screenshots, and explanations.

---

## 📂 Sections

- [Brute Force Attacks](Brute_Force.md)  
  Learn to detect brute force login attempts by analyzing repeated authentication failures in captured traffic.

- [DoS/DDoS Attacks](DoS_Attack.md)  
  Identify denial-of-service and distributed denial-of-service attacks by detecting abnormal traffic patterns.

- [DNS Tunneling](DNS_Tunneling.md)  
  Detect hidden communication through DNS queries used for data exfiltration.

- [Phishing](Phishing.md)  
  Investigate phishing attempts by analyzing suspicious HTTP, TLS, and SMTP traffic.

- [Malware Beaconing](Malware_Beaconing.md)  
  Detect periodic malicious connections to command-and-control (C2) servers.

- [Suspicious File Transfer](Suspicious_File_Transfer.md)  
  Analyze unauthorized or suspicious file transfers via FTP, HTTP, or SMB.

- [Insider Threat Activity](Insider_Threat.md)  
  Investigate malicious insider activity, such as exfiltration of sensitive data.

---

## 🛠 How to Use
1. Open the relevant `.md` file for the attack you want to study.  
2. Follow the guided lab steps.  
3. Use the provided `.pcap` files to practice real-world network traffic analysis.  
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

- [Brute Force Detection](./Brute_Force.md)  
- [DNS Tunneling](./Event_Analysis/DNS_Tunneling.md)  
- [Malware Traffic](./Event_Analysis/Malware_Traffic.md)  
- [Phishing Attack](./Event_Analysis/Phishing.md)  
- [Data Exfiltration](./File_Exfiltration.md)  

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
