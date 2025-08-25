# 🪟 Windows File System Hierarchy

The Windows file system organizes system, program, and user data across key directories.  
Understanding these locations is critical for system administration, forensics, and incident response.

## 📂 Directory Overview

| Directory | Purpose |
|-----------|---------|
| `C:\` | Primary root of the Windows file system. |
| `C:\Windows\` | Core operating system files and configuration. |
| `C:\Windows\System32\` | Critical 32-bit and 64-bit system executables, drivers, and DLLs. |
| `C:\Windows\SysWOW64\` | 32-bit libraries and binaries on 64-bit Windows systems. |
| `C:\Program Files\` | Default location for installed applications (64-bit). |
| `C:\Program Files (x86)\` | Default location for installed applications (32-bit). |
| `C:\Users\` | User profile directories (Documents, Downloads, Desktop, etc.). |
| `C:\Users\Public\` | Shared data accessible to all users. |
| `C:\ProgramData\` | Application data shared among all users (hidden by default). |
| `C:\Temp\` | Temporary files (often used during installations or updates). |
| `C:\Windows\Temp\` | System temporary files (used by OS and services). |
| `C:\Windows\System32\drivers\etc\` | Contains `hosts` file and network configuration. |
| `C:\Windows\Logs\` | System and diagnostic log files. |
| `C:\Windows\Prefetch\` | Prefetch files used to speed up application loading (useful in forensics). |
| `C:\Windows\WinSxS\` | Windows component store (side-by-side assemblies for system stability). |
| `C:\Recycle.Bin\` | Recycle Bin for deleted files (hidden). |
| `C:\Windows\System32\winevt\Logs\` | Event logs in `.evtx` format (Security, Application, System). |
| `C:\Windows\System32\config\` | Windows registry hive files (`SYSTEM`, `SAM`, `SOFTWARE`, etc.). |
