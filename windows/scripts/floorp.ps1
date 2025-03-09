# firefox one liner install, irm https://snippets.k3t.xyz/windows/scripts/floorp.ps1
echo "Downloading Floorp..."
Start-BitsTransfer -Source "https://github.com/Floorp-Projects/Floorp/releases/latest/download/floorp-win64.installer.exe" -Destination $env:TEMP\floorp.exe
Start-Process $env:TEMP\floorp.exe