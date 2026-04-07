#!/bin/bash
echo "[*] Checking container privileges..."
if find /dev -name "sd*" 2>/dev/null | grep -q sd; then
echo "[+] Host devices found - PRIVILEGED!"
else
echo "[-] No host devices detected"
fi
echo "[*] Checking capabilities..."
cat /proc/self/status | grep CapEff
echo "[+] Attack complete!"
