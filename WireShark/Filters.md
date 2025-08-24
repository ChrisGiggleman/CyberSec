# 📖 Wireshark Filter Cookbook  

A collection of practical **Wireshark filters** for SOC, IR, and pentesting tasks.  
Each entry includes:  

- **Filter Expression** (copy/paste ready)  
- **Use Case** (when/why to use)  
- **Example Action** (how to apply in an investigation)  

---

## 🔎 Host & IP Based Filters  

### Filter by specific IP (src or dst)  
```wireshark
ip.addr == 192.168.1.10
Use Case: Focus only on one host
Example: Investigate suspected compromised workstation

Filter by source only
wireshark
Copy
Edit
ip.src == 192.168.1.10
Example: Look at what traffic a host is generating

Filter by destination only
wireshark
Copy
Edit
ip.dst == 192.168.1.10
Example: See inbound connections to a server

Exclude internal IP range
wireshark
Copy
Edit
!(ip.addr == 192.168.0.0/16)
Example: Focus on external communication only

🌐 Protocol Filters
HTTP traffic only
wireshark
Copy
Edit
http
Example: Inspect web traffic for suspicious requests

HTTPS traffic
wireshark
Copy
Edit
tcp.port == 443
Example: Identify encrypted sessions (good for volume checks, not content)

DNS traffic
wireshark
Copy
Edit
dns
Example: Investigate potential DNS tunneling or exfiltration

FTP traffic
wireshark
Copy
Edit
ftp || ftp-data
Example: Catch plaintext file transfers

SMB / Windows file sharing
wireshark
Copy
Edit
smb || smb2
Example: Look for lateral movement or file access

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
