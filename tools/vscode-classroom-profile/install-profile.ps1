# Installs two simple classroom profiles into VS Code:
#   - Classroom Folder   (Explorer + .py live coding)
#   - Classroom Notebook (Jupyter .ipynb)
# Font size is 24+ everywhere. No custom color theme (keeps VS Code default).
# Quit VS Code (File > Exit) before running for a reliable save.

$ErrorActionPreference = "Stop"

$profilesRoot = Join-Path $env:APPDATA "Code\User\profiles"
$storagePath = Join-Path $env:APPDATA "Code\User\globalStorage\storage.json"
$repoProfileDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$extRoot = Join-Path $env:USERPROFILE ".vscode\extensions"

$codeRunning = @(Get-Process -Name "Code" -ErrorAction SilentlyContinue)
if ($codeRunning.Count -gt 0) {
    Write-Warning "VS Code is running ($($codeRunning.Count) processes). Quit VS Code completely, then re-run this script."
}

function Get-PythonInterpreter {
    $defaultSettingsPath = Join-Path $env:APPDATA "Code\User\settings.json"
    if (Test-Path $defaultSettingsPath) {
        $defaultSettings = Get-Content -Raw $defaultSettingsPath | ConvertFrom-Json
        if ($defaultSettings.'python.defaultInterpreterPath') {
            return $defaultSettings.'python.defaultInterpreterPath'
        }
    }
    return $null
}

function New-ExtensionsJson([string[]]$ExtensionIds) {
    $entries = New-Object System.Collections.Generic.List[object]
    foreach ($id in $ExtensionIds) {
        $dir = Get-ChildItem $extRoot -Directory -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -like "$id-*" } |
            Sort-Object Name -Descending |
            Select-Object -First 1
        if (-not $dir) {
            Write-Warning "Extension not found: $id"
            continue
        }
        $rel = $dir.Name
        $fsPath = $dir.FullName
        $unixPath = "/" + ($fsPath -replace "\\", "/")
        $version = $rel.Substring($id.Length + 1)
        $location = [ordered]@{}
        $location['$mid'] = 1
        $location['fsPath'] = $fsPath
        $location['path'] = $unixPath
        $location['scheme'] = "file"
        $entries.Add([ordered]@{
            identifier       = @{ id = $id }
            version          = $version
            location         = $location
            relativeLocation = $rel
        }) | Out-Null
    }
    if ($entries.Count -eq 0) {
        throw "No matching extensions found under $extRoot"
    }
    return ($entries | ConvertTo-Json -Depth 10)
}

function Install-ClassroomProfile {
    param(
        [string]$ProfileId,
        [string]$ProfileName,
        [string]$Icon,
        [string]$SettingsFile,
        [string[]]$ExtensionIds,
        [string]$KeybindingsJson = "[]"
    )

    $profileDir = Join-Path $profilesRoot $ProfileId
    New-Item -ItemType Directory -Force -Path $profileDir | Out-Null
    New-Item -ItemType Directory -Force -Path (Join-Path $profileDir "snippets") | Out-Null
    New-Item -ItemType Directory -Force -Path (Join-Path $profileDir "globalStorage") | Out-Null

    $settingsObj = Get-Content -Raw (Join-Path $repoProfileDir $SettingsFile) | ConvertFrom-Json
    $py = Get-PythonInterpreter
    if ($py) {
        $settingsObj | Add-Member -NotePropertyName 'python.defaultInterpreterPath' -NotePropertyValue $py -Force
    }

    [System.IO.File]::WriteAllText((Join-Path $profileDir "settings.json"), ($settingsObj | ConvertTo-Json -Depth 20))
    [System.IO.File]::WriteAllText((Join-Path $profileDir "keybindings.json"), $KeybindingsJson)
    [System.IO.File]::WriteAllText((Join-Path $profileDir "extensions.json"), (New-ExtensionsJson $ExtensionIds))

    return [pscustomobject]@{
        location = $ProfileId
        name     = $ProfileName
        icon     = $Icon
    }
}

$folderKeys = @'
[
  {
    "key": "f5",
    "command": "python.execInTerminal",
    "when": "editorTextFocus && editorLangId == 'python' && !inDebugMode"
  }
]
'@

$notebookKeys = @'
[
  {
    "key": "ctrl+enter",
    "command": "notebook.cell.execute",
    "when": "notebookEditorFocused"
  },
  {
    "key": "shift+enter",
    "command": "notebook.cell.executeAndSelectBelow",
    "when": "notebookEditorFocused"
  }
]
'@

$folderExt = @(
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-python.debugpy"
)

$notebookExt = @(
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-python.debugpy",
    "ms-toolsai.jupyter",
    "ms-toolsai.jupyter-keymap",
    "ms-toolsai.jupyter-renderers",
    "ms-toolsai.vscode-jupyter-cell-tags",
    "ms-toolsai.vscode-jupyter-slideshow"
)

$folderMeta = Install-ClassroomProfile -ProfileId "classroomfolder" -ProfileName "Classroom Folder" -Icon "folder" -SettingsFile "settings-folder.json" -ExtensionIds $folderExt -KeybindingsJson $folderKeys.Trim()
$notebookMeta = Install-ClassroomProfile -ProfileId "classroomnotebook" -ProfileName "Classroom Notebook" -Icon "notebook" -SettingsFile "settings-notebook.json" -ExtensionIds $notebookExt -KeybindingsJson $notebookKeys.Trim()

if (-not (Test-Path $storagePath)) {
    throw "VS Code storage.json not found at $storagePath"
}

$backup = "$storagePath.bak-classroom-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
Copy-Item $storagePath $backup
Write-Host "Backup: $backup"

$storage = Get-Content -Raw $storagePath | ConvertFrom-Json
$profiles = @($storage.userDataProfiles | Where-Object {
    $_.location -notin @("classroomtv", "classroomfolder", "classroomnotebook") -and
    $_.name -notin @("Classroom TV", "Classroom Folder", "Classroom Notebook")
})
$profiles += $folderMeta
$profiles += $notebookMeta
$storage.userDataProfiles = $profiles

# Prefer Folder profile for this course workspace
$wsKey = "file:///e%3A/repos/2026-27_PythonProgrammingCourse"
$storage.profileAssociations.workspaces | Add-Member -NotePropertyName $wsKey -NotePropertyValue "classroomfolder" -Force

[System.IO.File]::WriteAllText($storagePath, ($storage | ConvertTo-Json -Depth 100))

# Keep readable default settings.json in sync with folder view
Copy-Item (Join-Path $repoProfileDir "settings-folder.json") (Join-Path $repoProfileDir "settings.json") -Force

Write-Host ""
Write-Host "Installed profiles:"
Write-Host "  - Classroom Folder   (Explorer + .py)     -> code --profile `"Classroom Folder`" ."
Write-Host "  - Classroom Notebook (Jupyter .ipynb)     -> code --profile `"Classroom Notebook`" ."
Write-Host ""
$check = Get-Content -Raw $storagePath | ConvertFrom-Json
$check.userDataProfiles | Where-Object { $_.name -like "Classroom*" } | ForEach-Object {
    Write-Host ("OK {0} [{1}]" -f $_.name, $_.location)
}
