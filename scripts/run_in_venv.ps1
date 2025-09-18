param(
    [string]$Cmd = "python"
)
Push-Location "$PSScriptRoot\..\"
. "..\\.venv\\Scripts\\Activate.ps1"
& $Cmd
Pop-Location
