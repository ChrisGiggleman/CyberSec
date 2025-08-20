# Email Protocols (SMTP, IMAP, POP3)

## Normal Behavior
- Outbound email to mail servers (SMTP: 25/465/587)  
- Retrieval by IMAP (143/993) or POP3 (110/995)  
- Encrypted sessions (STARTTLS, SSL/TLS) for authentication and data  

## Suspicious Indicators
- Credentials in plaintext (no TLS)  
- Unusual mass email traffic → spam/malware distribution  
- Large file attachments sent externally (possible data exfiltration)  
- Emails to strange or known malicious domains  

## Wireshark Tips
- Filters:  
  - `smtp` → mail submission/relay  
  - `imap` → mailbox access  
  - `pop` → mailbox retrieval  
- Right-click → Follow TCP Stream to read email contents (if not encrypted)  
- Look for suspicious headers (X-Mailer, From, Return-Path)  
