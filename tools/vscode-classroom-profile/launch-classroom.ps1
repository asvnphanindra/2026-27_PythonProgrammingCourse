# Opens this course folder with the Classroom Folder profile (.py + Explorer).
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
Write-Host "Launching Classroom Folder in $repoRoot"
& $codeExe --profile "Classroom Folder" $repoRoot
