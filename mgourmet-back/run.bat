@echo off
setlocal

cd /d "%~dp0"

if not exist ".env" (
    echo Arquivo .env nao encontrado.
    echo Copie .env.example para .env e ajuste as configuracoes antes de iniciar a API.
    exit /b 1
)

if exist ".venv\Scripts\python.exe" (
    set "PYTHON=.venv\Scripts\python.exe"
) else (
    set "PYTHON=python"
)

%PYTHON% -c "import uvicorn" >nul 2>&1
if errorlevel 1 (
    echo Dependencias nao instaladas.
    echo Execute: %PYTHON% -m pip install -e .
    exit /b 1
)

echo Iniciando M Gourmet API em http://localhost:8000
%PYTHON% -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
