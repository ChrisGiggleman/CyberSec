# ⚡ PowerShell Usage Guide

This repository is a quick reference for working with PowerShell, covering operators, file management, scripting essentials, and automation examples.

## 📑 Table of Contents  

- [Comparison Operators](#-comparison-operators)  
- [File & Directory Management](#-file--directory-management-commands)  
- [Common Parameters](#️-common-parameters)  
- [Remote & Local Command Execution](#️-remote--local-command-execution)  
- [Pipeline Basics](#-pipeline-basics)  
- [Scripting Essentials](#-scripting-essentials)  
- [Examples](#-examples)  
- [Additional Resources](#-additional-resources)  
- [📖 PowerShell Examples (Full Cookbook)](powershell_examples.md)  
- [⚡ Scripts Folder](scripts/README.md)  

---

## 🔍 Comparison Operators  

| Operator | Meaning | Example |
|----------|---------|---------|
| `-eq` | Equal to | `Where-Object {$_.Extension -eq ".txt"}` |
| `-ne` | Not equal to | `Where-Object {$_.Extension -ne ".log"}` |
| `-gt` | Greater than | `Where-Object {$_.Length -gt 100MB}` |
| `-ge` | Greater than or equal to | `Where-Object {$_.Length -ge 1GB}` |
| `-lt` | Less than | `Where-Object {$_.Length -lt 1MB}` |
| `-le` | Less than or equal to | `Where-Object {$_.Length -le 50KB}` |

---

## 📂 File & Directory Management Commands  

| Command | Description | Example |
|---------|-------------|---------|
| `New-Item` | Creates a new file or directory. | `New-Item -Path "C:\Logs" -Name "newfile.txt" -ItemType File` |
| `Remove-Item` | Deletes files or directories. | `Remove-Item -Path "C:\Logs\oldfile.txt"` |
| `Set-Location` | Changes current working directory. | `Set-Location -Path "C:\Windows"` |
| `Get-ChildItem` | Lists files and directories. | `Get-ChildItem -Path "C:\Logs"` |

---

## ⚙️ Common Parameters  

| Parameter | Description | Example |
|-----------|-------------|---------|
| `-Recurse` | Applies action to all subdirectories. | `Get-ChildItem -Path C:\Logs -Recurse` |
| `-Force` | Shows hidden/system files. | `Get-ChildItem -Force` |
| `-Filter` | Filters results based on condition. | `Get-ChildItem -Filter *.txt` |

---

## 🌐 Remote & Local Command Execution  

| Command | Description | Example |
|---------|-------------|---------|
| `Invoke-Command` | Executes commands locally or remotely. | `Invoke-Command -ComputerName Server01 -ScriptBlock {Get-Process}` |
| `Enter-PSSession` | Starts interactive remote session. | `Enter-PSSession -ComputerName Server01` |
| `Exit-PSSession` | Ends remote session. | `Exit-PSSession` |

---

## 🔗 Pipeline Basics  

```powershell
# Example: list all txt files larger than 1MB
Get-ChildItem -Path "C:\Docs" -Recurse |
  Where-Object {$_.Extension -eq ".txt" -and $_.Length -gt 1MB} |
  Select-Object Name, Length
📜 Scripting Essentials
Use .ps1 extension for scripts.

Add comments with # to explain steps.

Parameters can be added with param(...) blocks.

Example script:

powershell
Copy code
param(
  [string]$Path = "C:\Logs",
  [int]$SizeLimitMB = 100
)

Get-ChildItem -Path $Path -Recurse |
  Where-Object { $_.Length -gt ($SizeLimitMB * 1MB) } |
  Select-Object FullName, Length
🧑‍💻 Examples
Here are some inline examples.
For a full list of practical scripts and recipes, see the 👉 PowerShell Examples Cookbook.

📚 Additional Resources
Microsoft PowerShell Docs

SS64 PowerShell Reference

PowerShell Gallery

yaml
Copy code

---

## 📌 File 2 — `powershell_examples.md`

```markdown
# 📖 PowerShell Examples Cookbook

A collection of practical examples and snippets for common PowerShell usage.

---

## 🔍 Filtering Files by Extension  

```powershell
Get-ChildItem -Path "C:\Docs" | Where-Object {$_.Extension -eq ".txt"}
🔄 Comparison Operators
powershell
Copy code
# Not equal
Get-ChildItem | Where-Object {$_.Extension -ne ".log"}

# Greater than 100MB
Get-ChildItem | Where-Object {$_.Length -gt 100MB}

# Less than or equal to 1MB
Get-ChildItem | Where-Object {$_.Length -le 1MB}
📂 File & Directory Management
powershell
Copy code
# Create a new file
New-Item -Path "C:\Logs" -Name "test.txt" -ItemType File

# Remove a directory
Remove-Item -Path "C:\Logs\Old"

# Change directory
Set-Location -Path "C:\Windows"
🌐 Remote & Local Command Execution
powershell
Copy code
# Run command remotely
Invoke-Command -ComputerName Server01 -ScriptBlock {Get-Service}

# Start interactive remote session
Enter-PSSession -ComputerName Server01
🔗 Pipeline Example
powershell
Copy code
# List txt files larger than 1MB
Get-ChildItem -Path "C:\Docs" -Recurse |
  Where-Object {$_.Extension -eq ".txt" -and $_.Length -gt 1MB} |
  Select-Object Name, Length
📜 Scripting Example
powershell
Copy code
param(
  [string]$Path = "C:\Logs",
  [int]$SizeLimitMB = 100
)

Get-ChildItem -Path $Path -Recurse |
  Where-Object { $_.Length -gt ($SizeLimitMB * 1MB) } |
  Select-Object FullName, Length
yaml
Copy code

---

## 📌 File 3 — `/scripts/README.md`

```markdown
# 📂 PowerShell Scripts

This folder contains ready-to-use PowerShell scripts. Each script is self-contained, documented, and parameterized where possible.

🔗 Quick Links:  
- [📖 PowerShell Examples Cookbook](../powershell_examples.md) – copy-paste snippets and recipes  
- [⚡ Scripts Folder (You Are Here)](README.md) – full `.ps1` files, ready to run  

---

## 📑 Script Index  

### 🔹 Quick Scripts  
| Script | Description | Example Usage |
|--------|-------------|---------------|
| **Get-TxtFiles.ps1** | Lists all `.txt` files in a given directory. | `.\Get-TxtFiles.ps1 -Path "C:\Docs"` |
| **Check-Uptime.ps1** | Retrieves uptime info for one or more servers. | `.\Check-Uptime.ps1 -Servers "DC01","Web01"` |
| **Rename-WithPrefix.ps1** | Adds a prefix to files in a directory. | `.\Rename-WithPrefix.ps1 -Path "C:\Files" -Prefix "Backup_"` |

### 🔹 Full Automation Scripts  
| Script | Description | Example Usage |
|--------|-------------|---------------|
| **Find-LargeFiles.ps1** | Finds files larger than a given size and exports results. | `.\Find-LargeFiles.ps1 -Path "C:\Users" -SizeLimitMB 500 -OutputFile BigFiles.csv` |
| **Export-Services.ps1** | Exports all running services to CSV. | `.\Export-Services.ps1 -OutputFile Running.csv` |
| **Remote-Check.ps1** | Executes a PowerShell command remotely on multiple computers. | `.\Remote-Check.ps1 -Computers Server01,Server02 -Command "Get-Process"` |

---

## 🛠️ How to Use

```powershell
# Example: running a script
.\Find-LargeFiles.ps1 -Path "C:\Users" -SizeLimitMB 500 -OutputFile BigFiles.csv
If execution policy blocks scripts:

powershell
Copy code
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
📌 Notes
Each script is safe to run locally and parameterized for reuse.

You can extend these or integrate into bigger automation workflows.

Contributions welcome — drop new .ps1 files here and update this index.
