@echo off

REM Check if the script is running with administrative privileges
openfiles >nul 2>&1
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

REM Check if Visual Studio Code is already installed
where code >nul 2>&1
if '%errorlevel%' EQU '0' (
    echo Visual Studio Code is already installed.
) else (
    REM Install Visual Studio Code using Chocolatey
    echo Installing Visual Studio Code...
    choco install vscode -y --confirm

    REM Verify the installation
    echo Verifying Visual Studio Code installation...
    where code >nul 2>&1
    if '%errorlevel%' EQU '0' (
        echo Visual Studio Code was successfully installed.
    ) else (
        echo Visual Studio Code installation failed.
    )
)

REM Pause to keep the window open (optional)
@REM pause
