# System Updater

Cross-platform system update scripts for **Linux (apt-based distros)** and **Windows (winget + Windows Update)**.

## 🚀 Usage

### Linux (Debian/Ubuntu)
```bash
chmod +x linux-update.sh
./linux-update.sh
```
This will:

Update package lists (apt-get update)

Upgrade installed packages (apt-get upgrade)

Run a distribution upgrade (apt-get dist-upgrade)

Remove unnecessary packages (apt-get autoremove)

##Windows (PowerShell)
Run the script in PowerShell (as Administrator):

```powershell

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\windows-update.ps1
```
This will:

Upgrade all apps using winget

Install all pending Windows Updates

Reboot automatically if required

##🛠 Requirements
Linux: Debian/Ubuntu or any apt-based system

Windows:

Windows 10/11

PowerShell 5.1 or 7+

winget

(Optional) PSWindowsUpdate

```yaml


---

### **linux-update.sh**
```bash
#!/bin/bash
echo "[*] Running Linux system update..."

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt-get autoremove -y

echo "[+] Linux system updated successfully!"
```
windows-update.ps1
```powershell

Write-Host "[*] Running Windows updates..."

# Update installed apps via winget
winget upgrade --all --accept-source-agreements --accept-package-agreements

# System Updates via PSWindowsUpdate
if (-not (Get-Module -ListAvailable -Name PSWindowsUpdate)) {
    Install-Module PSWindowsUpdate -Force -Scope CurrentUser
}
Import-Module PSWindowsUpdate
Get-WindowsUpdate -Install -AcceptAll -AutoReboot

Write-Host "[+] Windows updates complete!"
```
