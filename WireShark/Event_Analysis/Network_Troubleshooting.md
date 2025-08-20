
---

### 4️⃣ `Network_Troubleshooting.md`

```markdown
# Network Troubleshooting

## Overview
Wireshark is invaluable for detecting latency, retransmissions, and packet loss that may indicate network issues or attacks.

## Indicators
- TCP retransmissions and duplicate ACKs
- Latency spikes
- ICMP errors (Destination Unreachable, Time Exceeded)

## Wireshark Filters
```text
tcp.analysis.retransmission
icmp
