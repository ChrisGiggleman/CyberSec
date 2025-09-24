#!/bin/bash
echo "[*] Running Linux system update..."
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt-get autoremove -y
echo "[+] Linux system updated successfully!"

#Run the followign to provided ability to run
#chmod +x update.sh
#./update.sh
