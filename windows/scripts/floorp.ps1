# firefox one liner install, irm https://snippets.k3t.xyz/windows/scripts/floorp.ps1
echo "[floorp.ps1] Downloading Ablaze Floorp..."
Start-BitsTransfer -Source "https://github.com/Floorp-Projects/Floorp/releases/latest/download/floorp-win64.installer.exe" -Destination $env:TEMP\floorp.exe
echo "[floorp.ps1] Installing Floorp..."
Start-Process $env:TEMP\floorp.exe /silent