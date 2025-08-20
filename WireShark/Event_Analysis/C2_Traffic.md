# Command & Control (C2) Traffic

## Overview
C2 traffic is used by malware to communicate with remote servers for data exfiltration, lateral movement, or command execution. Detecting it is critical for SOC analysts to stop malware spread.

## MITRE ATT&CK Mapping
- **T1071.001** – Application Layer Protocol: Web Protocols  
- **T1071.004** – Application Layer Protocol: DNS  
- **T1090** – Proxy: Network Traffic Through a Proxy  

## Indicators of Compromise (IoCs)
- Repeated small packets at regular intervals to external IPs (beaconing)  
- Encrypted traffic over uncommon ports (e.g., 8443, 9000)  
- Connections to suspicious or newly registered domains  
- Abnormal DNS requests (randomized subdomains, TXT record abuse)  
- Unusual User-Agent strings in HTTP or TLS headers

<img width="1536" height="1024" alt="C2_traffic Wireshark" src="https://github.com/user-attachments/assets/23466396-66d1-4e3d-ab17-59e171bb756a" />


## Advanced Wireshark Filters
```text
# DNS beaconing
dns.qry.name matches "[a-z0-9]{10,}\.com"

# TLS to non-standard ports
tls && tcp.port != 443

# Traffic to suspicious IP
ip.addr == <suspect_ip>

____________________________________


## Analysis Tips
Follow TCP/UDP streams to reconstruct communication

Compare endpoints against threat intelligence feeds

Use time graphs to identify beacon intervals

Check DNS TXT records for potential exfiltration payloads

Example Behavior
Malware contacting abcd1234.maliciousdomain.com every 5 minutes

TLS handshake on port 8443 with unknown certificate



