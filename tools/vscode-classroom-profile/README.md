# Classroom profiles for live coding on a TV

Two simple VS Code profiles. Font size is **24** (editor, terminal, notebook). No custom color theme — VS Code’s default theme is kept.

| Profile | Use for | Extensions |
|---------|---------|------------|
| **Classroom Folder** | Explorer + `.py` live coding | Python, Pylance, Debugger |
| **Classroom Notebook** | Jupyter `.ipynb` demos | Python stack + Jupyter |

## Install (VS Code must be quit)

```powershell
.\tools\vscode-classroom-profile\install-profile.ps1
```

## Launch

```powershell
# Folder / .py view
.\tools\vscode-classroom-profile\launch-classroom.ps1

# Notebook view
.\tools\vscode-classroom-profile\launch-notebook.ps1
```

Or:

```powershell
code --profile "Classroom Folder" .
code --profile "Classroom Notebook" .
```

## Notes

- Mouse-wheel zoom is on (`Ctrl` + scroll) if you need larger than 24 on a big TV.
- Switch profiles anytime: gear icon → **Profiles**.
