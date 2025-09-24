# 🚀 Splunk SOAR (Unprivileged) 6.4.1 Setup Guide

This project is a step-by-step walkthrough for installing and running **Splunk SOAR (Security Orchestration, Automation and Response)** in **unprivileged mode** on Linux.

---

## 📦 Prerequisites

### Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install -y tar wget curl python3 python3-venv python3-pip \
    libpq-dev build-essential libssl-dev libffi-dev
```
## Amazon Linux 2023 / RHEL / Fedora:
```bash

sudo dnf update -y
sudo dnf install -y tar wget curl python3 python3-devel gcc gcc-c++ \
    postgresql-libs openssl-devel libffi-devel make
```
##📥 Download Splunk SOAR
```bash

wget https://download.splunk.com/products/soar/releases/6.4.1/linux/splunk_soar-unpriv-6.4.1.361-bea76553-amzn2023-x86_64.tgz
```
## 📂 Extract Installer
```bash

tar -xvzf splunk_soar-unpriv-6.4.1.361-bea76553-amzn2023-x86_64.tgz
cd splunk_soar-unpriv-6.4.1.361
```
## ⚙️ Run the Installer
```bash

./soar_unpriv_installer.sh
```
This installs SOAR in your user-space (no root needed).

## ▶️ Start Splunk SOAR
```bash

./soar_start.sh
```
(or)

```bash

./soar.sh start
```
## 🌐 Access the Web UI
Open your browser:

https://<your-vm-ip>:9999

Accept the self-signed certificate.

Create your admin account.

## 🛠 Managing SOAR
Stop SOAR:

```bash

./soar.sh stop
```
Restart SOAR:
```bash

./soar.sh restart
```
Run in background:

```bash

nohup ./soar.sh start &
```
## 📖 Next Steps
Connect SOAR to Splunk Enterprise/Cloud.

Install Apps/Connectors via the SOAR UI.

Build your first Playbook to automate actions.

## 📸 Screenshots
(Add screenshots in docs/screenshots/ and reference them here)

## ✅ Summary
Installed dependencies

Extracted SOAR installer

Ran setup

Started services

Accessed Web UI

```yaml


---

# 🛠 Example Helper Script (`scripts/start_soar.sh`)

```bash
#!/bin/bash
# Simple helper to start Splunk SOAR in background

cd ~/splunk_soar-unpriv-6.4.1.361 || exit
nohup ./soar.sh start > soar.log 2>&1 &
echo "Splunk SOAR is starting... Check soar.log for details."
