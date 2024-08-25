@echo off

REM Check if the script is running with administrative privileges
openfiles >nul 2>&1
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

REM Check if Python is already installed
where python >nul 2>&1
if '%errorlevel%' EQU '0' (
    echo Python is already installed.
) else (
    REM Install Python using Chocolatey
    echo Installing Python...
    choco install python -y --confirm

    REM Verify the installation
    echo Verifying Python installation...
    where python >nul 2>&1
    if '%errorlevel%' EQU '0' (
        echo Python was successfully installed.
    ) else (
        echo Python installation failed.
    )
)

REM Pause to keep the window open (optional)
@REM pause
