# 🕸️ Common Web Server Directories & Web Shell Detection

This repository documents:
- Common default web server directories where malicious actors may attempt to upload or place web shells.  
- Indicators of compromise such as suspicious file names.  
- Useful CLI commands to detect and investigate potential shells.  

It can be used as a **reference for penetration testing, incident response, and threat hunting**.

---

## 📂 Common Directories by Web Server

### Apache
- **Default Document Root (most Linux distros):**
/var/www/html/

diff
Copy code
- Other possible paths:
/usr/local/apache2/htdocs/
/srv/www/htdocs/

markdown
Copy code

### Nginx
- **Default Document Root (many Linux setups):**
/usr/share/nginx/html/

diff
Copy code
- Other possible paths:
/etc/nginx/html/
/var/www/nginx-default/

yaml
Copy code

---

## ⚠️ Suspicious or Random File Names

Attackers often try to **blend in or evade detection** by using unusual file names.  

- Be on the lookout for files that **don’t match standard application naming conventions**.  
- Monitor files with executable extensions such as:
.php, .jsp, .asp, .aspx, .pl

markdown
Copy code
- Watch for **double extensions** used to disguise malicious files:
image.jpg.php
upload.png.asp

diff
Copy code
- Malicious files are frequently hidden in:
/uploads/
/media/
/backup/
/tmp/

yaml
Copy code

---

## 🔎 Helpful Commands

These CLI commands are useful for hunting down suspicious or malicious files.  

### Find Recently Modified Files
Search `/var/www` for `.php` files created or modified between two specific dates:  

```bash
find /var/www -type f -name "*.php" -newerct "2025-07-01" ! -newerct "2025-08-01"
Example output:

bash
Copy code
/var/www/html/uploads/awebshell.php    # Web shell created between July–Aug 2025
Grep for Suspicious Functions
Search recursively for dangerous PHP functions such as eval( inside the WordPress wp-content directory:

bash
Copy code
grep -r "eval(" wp-content
Example output:

bash
Copy code
/wp-content/uploads/awebshell2.php : eval(b64_dd($['cmd']));
# Web shell containing suspicious eval() function
💡 Expand searches by looking for other dangerous functions:
base64_decode(, system(, exec(, shell_exec(, passthru(, assert(

📌 Notes
Always cross-reference with server configuration files (e.g., httpd.conf, nginx.conf) to confirm the true document root.

Attackers may also use hidden files (e.g., .shell.php) or bury shells deep within nested directories.

Automated detection tools like ClamAV, LMD (Linux Malware Detect), or WAF logs can complement manual searches.
