# Wireshark Filter Cookbook
A collection of practical Wireshark filters for SOC, IR, and pentesting tasks.  

---

## 🔎 Host & IP Based Filters

**Filter by specific IP (src or dst):**  
ip.addr == 192.168.1.10

pgsql
Copy
Edit
*Example:* Investigate suspected compromised workstation  

**Filter by source only:**  
ip.src == 192.168.1.10

pgsql
Copy
Edit
*Example:* Look at what traffic a host is generating  

**Filter by destination only:**  
ip.dst == 192.168.1.10

pgsql
Copy
Edit
*Example:* See inbound connections to a server  

**Exclude internal IP range:**  
!(ip.addr == 192.168.0.0/16)

yaml
Copy
Edit
*Example:* Focus on external communication only  

---

## 🌐 Protocol Filters

**HTTP traffic only:**  
http

markdown
Copy
Edit
*Example:* Inspect web traffic for suspicious requests  

**HTTPS traffic:**  
tcp.port == 443

pgsql
Copy
Edit
*Example:* Identify encrypted sessions (good for volume checks, not content)  

**DNS traffic:**  
dns

markdown
Copy
Edit
*Example:* Investigate potential DNS tunneling or exfiltration  

**FTP traffic:**  
ftp || ftp-data

markdown
Copy
Edit
*Example:* Catch plaintext file transfers  

**SMB / Windows file sharing:**  
smb || smb2

pgsql
Copy
Edit
*Example:* Look for lateral movement or file access  


## 🔐 Threat Hunting Filters

**Detect potential beaconing (same interval connections):**  
ip.addr == <target IP> && tcp

markdown
Copy
Edit
*Then:* Sort by time → look for repeating intervals  

**Suspicious DNS queries (rare TLDs):**  
dns.qry.name contains ".xyz"

markdown
Copy
Edit
*Example:* Catch C2 using weird domains  

**Cleartext credentials (HTTP POST logins):**  
http.request.method == "POST"

markdown
Copy
Edit
*Example:* Spot credential leaks in HTTP  

**Suspicious RDP traffic:**  
tcp.port == 3389

markdown
Copy
Edit
*Example:* Check if RDP is being brute-forced or used externally  

**ICMP tunneling or ping sweeps:**  
icmp

yaml
Copy
Edit
*Example:* Look for abnormal ICMP payloads  

---

## 🛠️ Troubleshooting Filters

**TCP retransmissions & errors:**  
tcp.analysis.retransmission

markdown
Copy
Edit
*Example:* Spot unstable connections  

**Packets with no response (possible dropped traffic):**  
tcp.analysis.lost_segment

markdown
Copy
Edit
*Example:* Find network issues or firewall drops  

**TLS handshake failures:**  
ssl.handshake.failure

yaml
Copy
Edit
*Example:* Debug broken HTTPS sessions  

---

## ⚡ Quick Actions

- Use **Ctrl+F → String** to search inside packet contents (e.g., for `password`).  
- Use **Statistics → Conversations** to pivot by IP, port, or protocol.  
- Export suspicious objects via **File → Export Objects** (HTTP/SMB/DICOM).  
