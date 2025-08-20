# HTTP (Web Traffic)

## Normal Behavior
- `GET` and `POST` requests to known domains  
- Standard ports (80, 8080, 443 before TLS handshake)  
- Expected User-Agent headers (e.g., Chrome, Edge, Firefox)  

## Suspicious Indicators
- Credentials in plaintext (`POST` with `username`/`password`)  
- Unusual User-Agent strings (e.g., `curl/`, `python-requests/`) → may indicate recon or automation  
- File transfers with uncommon extensions (`.exe`, `.dll`, `.ps1`)  
- HTTP traffic on non-standard ports  

## Wireshark Tips
- Filter: `http`  
- Right-click → Follow → HTTP Stream (reconstruct conversations)  
- Inspect headers (Host, Cookie, User-Agent) for anomalies  
