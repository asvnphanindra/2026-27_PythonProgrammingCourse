# Opens this course folder with the Classroom Notebook profile (Jupyter).
$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$codeCmd = Get-Command code -ErrorAction SilentlyContinue
if (-not $codeCmd) {
    $fallback = Join-Path $env:LOCALAPPDATA "Programs\Microsoft VS Code\bin\code.cmd"
    if (-not (Test-Path $fallback)) { Write-Error "VS Code 'code' CLI not found." }
    $codeExe = $fallback
} else {
    $codeExe = $codeCmd.Source
}
Write-Host "Launching Classroom Notebook in $repoRoot"
& $codeExe --profile "Classroom Notebook" $repoRoot
