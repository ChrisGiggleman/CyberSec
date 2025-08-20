# Wireshark Event Analysis

This guide contains examples and playbooks for using Wireshark in a SOC or pentesting context.

---

## 1. Detecting Malicious C2 Traffic
**Indicators:**
- Repeated small packets to external IPs on non-standard ports
- Unusual DNS queries (long/randomized domains)
- Encrypted traffic to uncommon endpoints

**Filters:**
```text
dns || tls
ip.addr == <suspect_ip>
tcp.port != 80 && tcp.port != 443
