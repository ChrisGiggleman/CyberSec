# 🛡️ Cybersecurity Frameworks Reference

This section provides a quick reference to two widely adopted cybersecurity frameworks:

- **[SANS CIS Controls](./SANS.md)** – Tactical, prioritized security actions.
- **[NIST Cybersecurity Framework (CSF)](./NIST.md)** – Strategic, risk-based approach.

Both are shown side by side for easy comparison, with a visual diagram and links for deeper study.

---

## 📊 Visual Relationship – SANS vs NIST

```mermaid
flowchart LR
    subgraph SANS["SANS CIS Controls"]
        C1["1. Asset Inventory"]
        C2["2. Software Inventory"]
        C3["3. Data Protection"]
        C4["4. Secure Configurations"]
        C5["5-6. Account/Access Mgmt"]
        C7["7. Vulnerability Mgmt"]
        C8["8. Audit Logging"]
        C9["9-10. Email/Malware Protections"]
        C11["11. Data Recovery"]
        C12["12. Network Security"]
        C13["13. Monitoring & Defense"]
        C14["14. Awareness Training"]
        C15["15. Vendor Mgmt"]
        C16["16. Application Security"]
        C17["17. Incident Response"]
        C18["18. Pen Testing"]
    end

    subgraph NIST["NIST Cybersecurity Framework"]
        ID["Identify"]
        PR["Protect"]
        DE["Detect"]
        RS["Respond"]
        RC["Recover"]
    end

    C1 --> ID
    C2 --> ID
    C3 --> PR
    C4 --> PR
    C5 --> PR
    C7 --> ID
    C8 --> DE
    C9 --> PR
    C11 --> RC
    C12 --> PR
    C13 --> DE
    C14 --> PR
    C15 --> ID
    C16 --> PR
    C17 --> RS
    C18 --> DE
📑 Quick Reference Table
SANS CIS Controls (v8)	NIST CSF Functions	Summary
Inventory of Assets	Identify (ID.AM)	Know what devices & systems exist
Inventory of Software	Identify (ID.AM)	Track authorized software
Data Protection	Protect (PR.DS)	Safeguard data everywhere
Secure Configurations	Protect (PR.IP)	Harden systems and software
Account/Access Management	Protect (PR.AC)	Enforce least privilege & MFA
Vulnerability Management	Identify (ID.RA)	Continuously find and fix flaws
Audit Log Management	Detect (DE.CM)	Monitor logs for anomalies
Email & Malware Protections	Protect (PR.PT)	Secure endpoints and comms
Data Recovery	Recover (RC.RP)	Ensure backup and restoration
Network Security & Monitoring	Detect (DE.CM) / Protect (PR.AC)	Control, segment, and monitor
Awareness Training	Protect (PR.AT)	Educate and train users
Vendor Management	Identify (ID.SC)	Manage 3rd party risks
Application Security	Protect (PR.IP)	Secure development practices
Incident Response	Respond (RS.RP)	Plan, test, and respond
Pen Testing	Detect (DE.CM)	Validate defenses through testing

🔗 Official Documentation
📘 SANS CIS Controls v8

📘 NIST Cybersecurity Framework (CSF) 2.0

⚡ Use this as a quick reference during engagements, training, or lab work.
For detailed breakdowns, see: SANS.md | NIST.md
