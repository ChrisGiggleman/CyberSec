🧪 Mini Lab: Packet Filter Basics
🎯 Objective

Learn how to capture, filter, and analyze network traffic using packet filtering expressions.

🛠️ Lab Setup

System: Linux (Ubuntu/Kali) or Windows with WSL

Tools: tcpdump (pre-installed on most Linux distros)

If missing, install:

sudo apt update && sudo apt install tcpdump -y

🔍 Step-by-Step Exercise
1. Capture all traffic on an interface

Find your interface:

ip a


Start capture (replace eth0 with your interface):

sudo tcpdump -i eth0


👉 You’ll see everything flying through your NIC.

2. Filter by host

Capture only traffic to/from a single host (example: 8.8.8.8):

sudo tcpdump -i eth0 host 8.8.8.8

3. Filter by port

Capture only DNS traffic (port 53):

sudo tcpdump -i eth0 port 53


Capture only HTTP traffic (port 80):

sudo tcpdump -i eth0 port 80

4. Combine filters (AND / OR / NOT)

Only traffic to 8.8.8.8 AND port 53:

sudo tcpdump -i eth0 host 8.8.8.8 and port 53


Capture HTTP OR HTTPS traffic:

sudo tcpdump -i eth0 port 80 or port 443


Exclude SSH traffic:

sudo tcpdump -i eth0 not port 22

5. Save capture to file

Capture traffic and save to a .pcap for later analysis in Wireshark:

sudo tcpdump -i eth0 -w mycapture.pcap


Open later in Wireshark:

wireshark mycapture.pcap

✅ Verification / Challenge Tasks

Run a ping 8.8.8.8 and filter only ICMP traffic.

sudo tcpdump -i eth0 icmp


👉 You should see your echo request/reply.

Browse to a website and capture only HTTP traffic (port 80).
👉 Do you see the raw HTTP GET requests?

Capture traffic and exclude DNS & SSH at the same time.
👉 Which protocols remain?
