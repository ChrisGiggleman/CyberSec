
---

### 3️⃣ `File_Exfiltration.md`

```markdown
# File Exfiltration

## Overview
Attackers may exfiltrate sensitive data over HTTP, SMB, FTP, or other protocols. Detecting large or unusual transfers is critical.

## Indicators of Compromise
- Large files transferred to external hosts
- Anonymous or unusual SMB access attempts
- Uncommon HTTP POST requests
- Multiple small packets forming a continuous flow to external IPs

## Wireshark Filters
```text
http.request.method == "POST"
smb2
ftp
