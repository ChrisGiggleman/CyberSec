#!/bin/bash
# This script can run on Linux (bash) or Windows (PowerShell).

# =========================
# Linux (bash) section
# =========================
if [ "$(uname -s)" = "Linux" ]; then
    echo "[*] Detected Linux. Updating via apt..."
    sudo apt-get update -y
    sudo apt-get upgrade -y
    sudo apt-get dist-upgrade -y
    sudo apt-get autoremove -y
    echo "[+] Linux updates complete!"
    exit 0
fi

# =========================
# Windows (PowerShell) section
# =========================
: <<'POWERSHELL'
# Requires: winget + PowerShell 5/7
Write-Host "[*] Detected Windows. Running updates..."

# Update via winget
winget upgrade --all --accept-source-agreements --accept-package-agreements

# Windows Update (system patches)
if (-not (Get-Module -ListAvailable -Name PSWindowsUpdate)) {
    Install-Module PSWindowsUpdate -Force -Scope CurrentUser
}
Import-Module PSWindowsUpdate
Get-WindowsUpdate -Install -AcceptAll -AutoReboot

Write-Host "[+] Windows updates complete!"
exit
POWERSHELL
