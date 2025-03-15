# firefox one liner install, irm https://snippets.k3t.xyz/windows/scripts/firefox.ps1
echo "[firefox.ps1] Downloading Mozilla Firefox..."
Start-BitsTransfer -Source "https://download.mozilla.org/?product=firefox-msi-latest-ssl&os=win64&lang=en-US" -Destination $env:TEMP\firefox.msi
echo "[firefox.ps1] Starting installer..."
Start-Process $env:TEMP\firefox.msi /passive