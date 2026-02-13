#!/usr/local/bin/pwsh

# Clear screen
Clear-Host

# Get directories and save to file
Get-ChildItem -Directory -Name | Out-File -FilePath list.md

$EXTRACTORS = @(
    "ebooklib",
    "epub2txt",
    "kreuzberg",
    "marker"
    # "MarkItDown",
    # "textract",
    # "tika-python"
)

foreach ($EXTRACTOR in $EXTRACTORS) {
    if ($EXTRACTOR.StartsWith("#")) {
        Write-Host "......................................................................"
        Write-Host "$EXTRACTOR skipped"
        continue
    }

    Write-Host "$EXTRACTOR  start"
    #Push-Location $EXTRACTOR
    cd $EXTRACTOR
    Test-Path ./test.ps1
    pwsh ./test.ps1
    Write-Host "$EXTRACTOR  end"
    #Pop-Location
    cd ..
}

Write-Host "==========="
1..10 | ForEach-Object {
    [Console]::Beep()
    say "I'm done"
}

# Key conversions:
# 
# sys_term_clean_screen_and_buffer → Clear-Host
# ls -d1 */ → Get-ChildItem -Directory -Name
# Array syntax changed to PowerShell format
# cd → Push-Location / Pop-Location (safer for scripts)
# source ./test.sh → & .\test.ps1
# if [[ ... ]] → if (...)
# seq 1 10 → 1..10
# echo -en "\007" → [Console]::Beep()