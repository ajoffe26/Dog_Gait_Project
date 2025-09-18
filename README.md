# Dog Gait Project — Quick Start

Use the project's virtual environment so your imports (torch, cv2, mediapipe) resolve correctly.

1) Activate (PowerShell):

```
cd 'c:/Users/andre/Downloads/Dog_Gait_Project'
.\.venv\Scripts\Activate.ps1
python verify_setup.py
```

2) Or run with the venv Python directly:

```
c:/Users/andre/Downloads/Dog_Gait_Project/.venv/Scripts/python.exe verify_setup.py
```

3) Helper scripts:

PowerShell helper - runs a command inside the venv:

```
./scripts/run_in_venv.ps1 -Cmd "python verify_setup.py"
```

Windows cmd helper:

```
scripts\run_in_venv.bat python verify_setup.py
```

4) VS Code: The workspace is configured to use the venv interpreter at `.venv\Scripts\python.exe`. If VS Code still shows a different interpreter, select it via Command Palette: `Python: Select Interpreter`.
