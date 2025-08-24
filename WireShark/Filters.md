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

🔐 Threat Hunting Filters
Detect potential beaconing (same interval connections)
wireshark
Copy
Edit
ip.addr == <target IP> && tcp
Then: Sort by time → look for repeating intervals

Suspicious DNS queries (rare TLDs)
wireshark
Copy
Edit
dns.qry.name contains ".xyz"
Example: Catch C2 using weird domains

Cleartext credentials (HTTP POST logins)
wireshark
Copy
Edit
http.request.method == "POST"
Example: Spot credential leaks in HTTP

Suspicious RDP traffic
wireshark
Copy
Edit
tcp.port == 3389
Example: Check if RDP is being brute-forced or used externally

ICMP tunneling or ping sweeps
wireshark
Copy
Edit
icmp
Example: Look for abnormal ICMP payloads

🛠️ Troubleshooting Filters
TCP retransmissions & errors
wireshark
Copy
Edit
tcp.analysis.retransmission
Example: Spot unstable connections

Packets with no response (possible dropped traffic)
wireshark
Copy
Edit
tcp.analysis.lost_segment
Example: Find network issues or firewall drops

TLS handshake failures
wireshark
Copy
Edit
ssl.handshake.failure
Example: Debug broken HTTPS sessions

⚡ Quick Actions
Use Ctrl+F → String to search inside packet contents (e.g., for password).

Use Statistics → Conversations to pivot by IP, port, or protocol.

Export suspicious objects via File → Export Objects (HTTP/SMB/DICOM).
