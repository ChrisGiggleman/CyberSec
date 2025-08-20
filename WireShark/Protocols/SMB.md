# SMB (Server Message Block – Windows File Sharing)

## Normal Behavior
- File sharing across local network  
- Authentication via NTLM or Kerberos  
- Typical usage within corporate networks  

## Suspicious Indicators
- Anonymous logon attempts (`Guest`)  
- Repeated failed logons → brute force attempts  
- File access to administrative shares (`C$`, `ADMIN$`)  
- Sudden access across many hosts (worm or lateral movement)  
- Large/suspicious file transfers between endpoints  

## Wireshark Tips
- Filter: `smb || smb2`  
- Inspect **Tree Connect** and **Session Setup** messages for login attempts  
- Check **File > Export Objects > SMB** for extracted files  
