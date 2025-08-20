---

### 3️⃣ `File_Exfiltration.md`

```markdown
# File Exfiltration

## Overview
Attackers may exfiltrate sensitive data over protocols like HTTP, SMB, FTP, or DNS. Detecting unusual transfers is critical for preventing data breaches.

## MITRE ATT&CK Mapping
- **T1041** – Exfiltration Over C2 Channel  
- **T1048** – Exfiltration Over Alternative Protocol  
- **T1020** – Automated Exfiltration  

## Indicators of Compromise
- Large file transfers to external hosts  
- Anonymous or unusual SMB access  
- HTTP POST requests with large payloads  
- Continuous small packets forming a data stream to external IPs  
- DNS tunneling or TXT record abuse  

## Advanced Wireshark Filters
```text
# HTTP POST exfil
http.request.method == "POST" && tcp.len > 1000

# SMB file transfers
smb2 && smb2.command == 0x05  # Write Request

# FTP file transfers
ftp-data

______________________________________________________

## Analysis Tips
Follow TCP/UDP streams to see transferred content

Inspect filenames and paths for sensitive data

Compare traffic patterns to baseline network behavior

Cross-reference with SIEM for large file transfers

##  Example Behavior
SMB write requests to hidden share \\192.168.1.50\C$

HTTP POST sending 500KB of internal data to external domain
