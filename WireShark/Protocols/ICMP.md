# ICMP (Ping Traffic)

## Normal Behavior
- Occasional echo requests and replies for connectivity testing  
- Standard packet sizes (typically <150 bytes)  
- Common in traceroute and network troubleshooting  

## Suspicious Indicators
- **Ping sweeps**: multiple sequential ICMP requests to different hosts  
- Oversized ICMP packets → tunneling or data exfiltration  
- High-frequency ICMP traffic (possible covert channel)  
- ICMP on unusual ports (indicates crafted/malicious packets)  

## Wireshark Tips
- Filter: `icmp`  
- Use **Statistics > Conversations > ICMP** for traffic patterns  
- Look at packet payloads for unusual or encoded data  
