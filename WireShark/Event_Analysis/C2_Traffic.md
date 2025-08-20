# Command & Control (C2) Traffic

## Overview
C2 traffic is used by malware to communicate with a remote server. Detecting it is critical for SOC analysts to stop malware spread and data exfiltration.

## Indicators of Compromise
- Repeated small packets to external IPs at regular intervals
- Encrypted traffic over uncommon ports
- Connections to suspicious or newly registered domains
- Unusual DNS requests (long/randomized domains, TXT record abuse)

## Wireshark Filters
```text
dns || tls
ip.addr == <suspect_ip>
tcp.port != 80 && tcp.port != 443
