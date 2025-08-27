# 📝 Event Viewer Quick Reference Cheat Sheet

---

## 📂 Key Event Viewer Logs
| Log Name           | Description |
|--------------------|-------------|
| **Application**    | Events from installed apps/programs. |
| **System**         | OS-related logs (drivers, services, updates, boot issues). |
| **Security**       | Authentication, logon attempts, resource access (important for audits). |
| **Setup**          | Windows setup and installation events. |
| **Forwarded Events** | Logs forwarded from other computers. |

---

## 🔎 Common Security Event IDs
| Event ID | Meaning | Extra Notes |
|----------|----------|-------------|
| **4624** | Successful logon | 🔑 Common Codes: 2 (local), 3 (network), 5 (service), 10 (RDP) |
| **4625** | Failed logon | Check source workstation & account. |
| **4634** | Logoff | User session ended. |
| **4648** | Logon attempt with explicit credentials | Possible lateral movement. |
| **4672** | Special privileges assigned | e.g., Admin login. |
| **4720** | New user account created | Watch for suspicious accounts. |
| **4722** | Account enabled | Could indicate persistence. |
| **4725** | Account disabled | Security/hardening event. |
| **4726** | Account deleted | Check who deleted it. |
| **4740** | Account locked out | Brute force attempts or password issues. |

---

## ⚡ Quick Navigation Tips
Open Event Viewer → Win + R → eventvwr.msc
Expand "Windows Logs" → Application, System, or Security
Right-click log → Filter Current Log… (filter by Event ID)
Use Ctrl + F to search quickly
Export logs → Right-click log → "Save All Events As…"


---

## 🛠️ Useful Filters for Security Monitoring
✅ **Failed logons** → Filter by `4625`  
✅ **Account changes** → Filter by `4720–4726`  
✅ **Privilege escalations** → Filter by `4672`  
✅ **Lockouts** → Filter by `4740`  

---

✨ With this layout:
- Tables make logs & event IDs easier to scan.
- Code blocks (` ``` `) make commands/navigation steps pop out.
- ✅ / 🔑 icons help highlight **important actions/events**.

---

👉 Do you want me to also make a **graph-style diagram (Mermaid.js)** that can be rendered directly in GitHub (like a flowchart of event IDs)? That would really visualize the workflow of logons, failures, lockouts, etc.
