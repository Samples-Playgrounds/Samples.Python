#!/usr/local/bin/pwsh

$LIBRARY = "ebooklib"
Write-Host $LIBRARY
Write-Host "start"

Get-Location

# Deactivate venv if active
if ($env:VIRTUAL_ENV) { & deactivate }

Remove-Item -Path ".venv" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "__pycache__" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "*.pyc" -Force -ErrorAction SilentlyContinue

python -m venv .venv
& .\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install EbookLib beautifulsoup4 timer codetiming

pip freeze | Out-File -FilePath requirements.txt

python main.py

Get-Location
Write-Host "stop"
Write-Host $LIBRARY