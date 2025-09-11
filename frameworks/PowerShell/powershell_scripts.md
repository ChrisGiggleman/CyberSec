# PowerShell Scripts

This folder contains PowerShell scripts ranging from **small one-liners** to **larger automation scripts**.  
You can drop your `.ps1` files here and use this document as an **index & explanation guide**.

---

## 📌 Quick Scripts

### 1. Create a Text File With Content
```powershell
# Creates a file and writes "Hello World" inside
New-Item -Path . -Name "hello.txt" -ItemType File
Set-Content -Path "hello.txt" -Value "Hello World"
2. Delete All .log Files in a Directory
powershell
Copy code
# Removes all log files from current folder
Get-ChildItem -Path . -Filter *.log | Remove-Item -Force
3. Show Top 5 Processes by Memory Usage
powershell
Copy code
# Displays the 5 most memory-intensive processes
Get-Process | Sort-Object -Property WS -Descending | Select-Object -First 5
📂 Larger Automation Scripts
1. Backup Script
powershell
Copy code
# Backup-Script.ps1
# Copies files from source to backup folder with timestamp

param (
    [string]$Source = "C:\Data",
    [string]$Destination = "C:\Backup"
)

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$backupPath = Join-Path $Destination "Backup_$timestamp"

Write-Output "Starting backup..."
Copy-Item -Path $Source -Destination $backupPath -Recurse
Write-Output "Backup completed: $backupPath"
2. Remote Command Execution
powershell
Copy code
# Remote-Command.ps1
# Runs a given command on multiple remote computers

param (
    [string[]]$Computers,
    [string]$Command
)

foreach ($comp in $Computers) {
    Invoke-Command -ComputerName $comp -ScriptBlock { Invoke-Expression $using:Command }
}
🚀 How to Run Scripts
Save the script as a .ps1 file.

Open PowerShell and navigate to the script folder.

Allow script execution if needed:

powershell
Copy code
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
Run the script:

powershell
Copy code
.\scriptname.ps1
