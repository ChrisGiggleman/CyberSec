🐧 Linux File System Hierarchy

The Linux file system follows a structured hierarchy. Each directory serves a specific purpose, helping organize binaries, configuration files, user data, and system processes.

📂 Directory Overview
Directory	Purpose
/	Primary hierarchy and root directory of the entire file system.
/bin	Essential command binaries (e.g., ls, cp, mv).
/boot	System boot loader files (kernel, initrd, GRUB).
/dev	Device files (represent hardware devices like /dev/sda).
/etc	Host-specific configuration files (system-wide settings).
/home	User home directories (e.g., /home/alice).
/lib	Shared library modules needed by system binaries.
/media	Removable media (e.g., CD-ROM, USB).
/mnt	Temporary mount point for filesystems.
/opt	Add-on application packages (third-party software).
/proc	Virtual filesystem with kernel & process information.
/root	Home directory for root (superuser).
/run	Runtime data (process IDs, sockets, temporary files).
/sbin	System binaries (admin commands, e.g., iptables, reboot).
/srv	Site-specific data served by the system (web, FTP).
/sys	Virtual filesystem for kernel/system info.
/tmp	Temporary files (deleted on reboot).
/usr	User programs and data (read-only, includes /usr/bin, /usr/lib).
/var	Variable files (logs, mail, spool, cache).
