# DNS (Domain Name System)

## Normal Behavior
- Queries to known domains  
- Low volume of TXT records  
- Queries on port 53 (UDP)  

## Suspicious Indicators
- High volume of DNS queries (beaconing / C2)  
- Long/randomized domains (DGA malware)  
- TXT record abuse (data exfiltration)  
- DNS over non-standard ports  

## Wireshark Tips
- Filter: `dns`  
- Use Statistics → Conversations (UDP) to spot heavy DNS talkers  
- Look at Info column for suspicious domains  
