# TLS / SSL (Encrypted Traffic)

## Normal Behavior
- Client Hello → Server Hello → Certificate exchange  
- Valid certificates from trusted Certificate Authorities  
- Standard ports (443, 8443)  
- Secure cipher suites (AES, TLS 1.2/1.3)  

## Suspicious Indicators
- Self-signed or invalid certificates  
- Expired or mismatched domain certificates  
- Frequent failed handshakes (scanning or misconfigured client)  
- TLS traffic to suspicious/unusual IP addresses (possible malware C2)  
- Encrypted traffic on non-standard ports  

## Wireshark Tips
- Filter: `tls`  
- Inspect **SNI (Server Name Indication)** in Client Hello to see the target domain  
- Export certificates: `File > Export Objects > TLS`  
- If key logs are available (`SSLKEYLOGFILE` env var in browsers), configure in Wireshark:  
  `Edit > Preferences > Protocols > TLS > (Pre-Master-Secret log filename)` to decrypt  
