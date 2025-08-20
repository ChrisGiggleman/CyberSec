# Wireshark Filters

## Display Filters (Most Used)
- `ip.addr == 192.168.1.10` → Show traffic to/from an IP
- `tcp.port == 80` → Show HTTP traffic
- `udp.port == 53` → Show DNS traffic
- `http` → Show HTTP traffic only
- `dns` → Show DNS queries/responses
- `ssl || tls` → Show TLS/SSL traffic
- `tcp.flags.syn == 1 && tcp.flags.ack == 0` → Show SYN packets (possible scans)
- `icmp` → Show ping traffic

## Capture Filters (Before Capture)
- `host 192.168.1.1` → Capture only traffic to/from host
- `net 192.168.1.0/24` → Capture subnet traffic
- `port 443` → Capture HTTPS traffic
- `tcp` → Capture TCP only
- `udp` → Capture UDP only
