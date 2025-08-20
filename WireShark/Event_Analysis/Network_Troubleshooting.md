
---

### 4️⃣ `Network_Troubleshooting.md`

```markdown
# Network Troubleshooting

## Overview
Wireshark helps detect latency, retransmissions, and packet loss that may indicate network misconfigurations or attacks.

## MITRE ATT&CK Mapping
- **T1040** – Network Sniffing (for context in troubleshooting/monitoring)  
- **T1070.004** – Indicator Removal on Host: File Deletion (for correlated analysis)  

## Indicators
- TCP retransmissions and duplicate ACKs  
- Latency spikes or delays  
- ICMP errors (Destination Unreachable, Time Exceeded)  
- Out-of-order packets  

## Advanced Wireshark Filters
```text
# Retransmissions
tcp.analysis.retransmission

# Duplicate ACKs
tcp.analysis.duplicate_ack

# ICMP errors
icmp.type == 3 || icmp.type == 11

______________________________________________________________

## Analysis Tips
Use Statistics > IO Graphs to visualize spikes and anomalies

Identify hosts causing retransmissions or packet loss

Compare traffic against baseline network performance

Correlate with firewall, router, or endpoint logs

## Example Behavior
Multiple TCP retransmissions from a server during peak hours

ICMP Type 3 (Destination Unreachable) spikes from misconfigured subnet
