📝 Event Viewer Quick Reference Cheat Sheet
📂 Key Event Viewer Logs

Application → Events from installed apps/programs.

System → OS-related logs (drivers, services, updates, boot issues).

Security → Authentication, logon attempts, resource access (important for audits).

Setup → Windows setup and installation events.

Forwarded Events → Logs forwarded from other computers.

🔎 Common Security Event IDs

4624 → Successful logon.

4625 → Failed logon.

4634 → Logoff.

4648 → Logon attempt with explicit credentials.

4672 → Special privileges assigned (e.g., Admin login).

4720 → New user account created.

4722 → Account enabled.

4725 → Account disabled.

4726 → Account deleted.

4740 → Account locked out.

⚡ Quick Navigation Tips

Open Event Viewer → Win + R → type eventvwr.msc → Enter.

Expand Windows Logs → select Application, System, or Security.

Use Filter Current Log… (right-click log → filter by Event ID).

Use Find… (Ctrl + F) to quickly search specific events.

Export logs → Right-click log → Save All Events As…

🛠️ Useful Filters for Security Monitoring

Failed logons → Filter by 4625.

Account changes → Filter by 4720–4726.

Privilege escalations → Filter by 4672.

Lockouts → Filter by 4740.
