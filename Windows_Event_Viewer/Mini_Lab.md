🧪 Mini Lab: Event Viewer Basics
🎯 Objective

Learn how to navigate Windows Event Viewer, locate key system/security logs, and generate/test events that appear in the logs.

🛠️ Lab Setup

System: Windows 10 or 11 (VM or host is fine)

Tools: Built-in Event Viewer

Permissions: Admin user recommended

🔎 Step 1: Open Event Viewer

Press Win + R → type eventvwr.msc → hit Enter.

Expand the left panel → you’ll see three main categories:

Windows Logs (Application, Security, Setup, System, Forwarded Events)

Applications and Services Logs

Custom Views

👉 For this lab, focus on Windows Logs > Security and Windows Logs > System.

🔎 Step 2: Generate a System Log Event

We’ll create an event by stopping and starting a service:

Open Services (services.msc).

Find Windows Update service (or another non-critical one).

Right-click → Stop → then Start.

📌 Now go back to Event Viewer > Windows Logs > System.

Look for Event ID 7036 → “The [Service Name] entered the stopped/started state.”

🔎 Step 3: Generate a Security Log Event

We’ll trigger a login failure event.

Lock your computer (Win + L) → then type wrong password 2–3 times.

Log back in with the correct password.

Go to Event Viewer > Windows Logs > Security.

📌 Look for:

Event ID 4625 → Failed logon attempt.

Event ID 4624 → Successful logon.

🔎 Step 4: Filtering Logs

Instead of scrolling, let’s filter:

Right-click Security → Filter Current Log…

Enter Event ID 4625 → OK.

Only failed logons will show.

Try also filtering System log for 7036.

🔎 Step 5: Create a Custom View

In the left pane → Custom Views > Create Custom View…

Select Event ID 4625 + 7036 → Save as “Login & Service Events.”

Now you have a custom dashboard for these events.

✅ At the end of this mini lab, you’ve:

Opened Event Viewer.

Generated system and security events.

Used filtering and custom views.
