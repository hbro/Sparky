python -m venv (Join-Path $PSScriptRoot ".venv")
.venv\Scripts\pip install -r (Join-Path $PSScriptRoot "requirements.txt")
.venv\Scripts\python -m pip install --upgrade pip