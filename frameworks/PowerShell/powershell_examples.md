# PowerShell Examples

This file contains useful PowerShell command references, examples, and explanations.  
It is designed to be a **quick reference guide** for common tasks.

---

## 🔍 Comparison Operators

PowerShell provides comparison operators to filter and evaluate data. These are commonly used with `Where-Object`.

| Operator | Meaning | Example |
|----------|---------|---------|
| `-eq` | Equal to | `Get-ChildItem \| Where-Object { $_.Extension -eq ".txt" }` |
| `-ne` | Not equal to | `Get-Process \| Where-Object { $_.Name -ne "explorer" }` |
| `-gt` | Greater than | `Get-ChildItem \| Where-Object { $_.Length -gt 1MB }` |
| `-ge` | Greater than or equal to | `Get-ChildItem \| Where-Object { $_.Length -ge 100KB }` |
| `-lt` | Less than | `Get-ChildItem \| Where-Object { $_.Length -lt 1KB }` |
| `-le` | Less than or equal to | `Get-ChildItem \| Where-Object { $_.Length -le 5MB }` |

---

## 📂 File & Directory Management

| Cmdlet | Purpose | Example |
|--------|---------|---------|
| `New-Item` | Creates a new file or folder | `New-Item -Path . -Name "test.txt" -ItemType File` |
| `Remove-Item` | Deletes a file or folder | `Remove-Item -Path "test.txt"` |
| `Set-Location` | Changes the current directory | `Set-Location C:\Users` |
| `Get-Location` | Displays the current directory | `Get-Location` |

---

## ⚡ Remote Commands

| Cmdlet | Purpose | Example |
|--------|---------|---------|
| `Invoke-Command` | Runs a command/script on a local or remote computer | `Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Process }` |
| `Enter-PSSession` | Starts an interactive session with a remote computer | `Enter-PSSession -ComputerName Server01` |
| `Exit-PSSession` | Ends the interactive session | `Exit-PSSession` |

---

## 🛠️ Example Workflows

### 1. List all `.txt` files in a directory
```powershell
Get-ChildItem -Path . | Where-Object { $_.Extension -eq ".txt" }
2. Find processes using more than 100 MB of memory
powershell
Copy code
Get-Process | Where-Object { $_.WorkingSet -gt 100MB }
3. Create a folder and navigate into it
powershell
Copy code
New-Item -Path . -Name "Logs" -ItemType Directory
Set-Location Logs
4. Run a command remotely
powershell
Copy code
Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Service }
