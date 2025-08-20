---

### 2️⃣ `Brute_Force.md` (Brute Force / Scans)

```markdown
# Brute Force / Scans

## Overview
Attackers perform repeated login attempts or scan ports to identify weaknesses. Detecting patterns helps prevent account compromise or lateral movement.

## MITRE ATT&CK Mapping
- **T1110.001** – Brute Force: Password Spraying  
- **T1046** – Network Service Scanning  
- **T1021** – Remote Services Lateral Movement  

## Indicators of Compromise
- Multiple SYN packets without ACKs  
- Repeated failed login attempts across hosts/services  
- Sequential port scans to a host/subnet  

## Advanced Wireshark Filters
```text
# SYN scans
tcp.flags.syn == 1 && tcp.flags.ack == 0

# Failed login attempts (example SMB)
smb2 && smb2.nt_status == 0xC000006D

_________________________________________

## Analysis Tips
Use Statistics > Conversations to identify top talkers

Combine network captures with authentication logs for correlation

Identify patterns: single IP hitting multiple hosts or ports

## Example Behavior
Single IP sending SYN packets to ports 22, 80, 443 on multiple hosts within 30 seconds

Repeated SMB session failures on administrative shares (C$)
