@echo off
set FLASK_APP=app.py
set FLASK_ENV=development
"C:\Python312\python.exe" "%~dp0app.py"
if errorlevel 1 (
    echo Error running Flask application
    pause
    exit /b 1
)