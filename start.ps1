$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$backend = Join-Path $root "backend"
$frontend = Join-Path $root "frontend"
$logs = Join-Path $root "logs"

New-Item -ItemType Directory -Force -Path $logs | Out-Null

$backendPython = Join-Path $backend "venv\Scripts\python.exe"
if (-not (Test-Path $backendPython)) {
  throw "Backend venv not found. Run: python -m venv backend\venv"
}

$backendOut = Join-Path $logs "backend.out.log"
$backendErr = Join-Path $logs "backend.err.log"
$frontendOut = Join-Path $logs "frontend.out.log"
$frontendErr = Join-Path $logs "frontend.err.log"

$backendProcess = Start-Process `
  -FilePath $backendPython `
  -ArgumentList "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" `
  -WorkingDirectory $backend `
  -RedirectStandardOutput $backendOut `
  -RedirectStandardError $backendErr `
  -WindowStyle Hidden `
  -PassThru

$frontendProcess = Start-Process `
  -FilePath "npm.cmd" `
  -ArgumentList "run", "dev", "--", "-H", "0.0.0.0" `
  -WorkingDirectory $frontend `
  -RedirectStandardOutput $frontendOut `
  -RedirectStandardError $frontendErr `
  -WindowStyle Hidden `
  -PassThru

@"
CareerCompass AI is starting.

Frontend: http://localhost:3000
Backend:  http://localhost:8000/api/health

Backend PID:  $($backendProcess.Id)
Frontend PID: $($frontendProcess.Id)

Logs:
$backendOut
$backendErr
$frontendOut
$frontendErr
"@
