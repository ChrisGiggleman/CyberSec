Write-Host "[*] Running Windows updates..."

# Update apps via winget
winget upgrade --all --accept-source-agreements --accept-package-agreements

# System Updates
if (-not (Get-Module -ListAvailable -Name PSWindowsUpdate)) {
    Install-Module PSWindowsUpdate -Force -Scope CurrentUser
}
Import-Module PSWindowsUpdate
Get-WindowsUpdate -Install -AcceptAll -AutoReboot

Write-Host "[+] Windows updates complete!"


#Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
#.\update.ps1
