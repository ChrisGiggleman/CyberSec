
---

### 2️⃣ `Brute_Force.md` (Brute Force / Scans)

```markdown
# Brute Force / Scans

## Overview
Attackers often attempt multiple login attempts or scan ports to find vulnerabilities. Detecting these patterns helps prevent account compromise or lateral movement.

## Indicators of Compromise
- Many SYN packets without corresponding ACKs
- Repeated failed login attempts
- Multiple login attempts across multiple hosts or services

## Wireshark Filters
```text
tcp.flags.syn == 1 && tcp.flags.ack == 0
