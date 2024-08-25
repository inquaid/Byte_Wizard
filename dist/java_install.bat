@echo off

REM Check if the script is running with administrative privileges
openfiles >nul 2>&1
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

REM Check if Java is already installed
where java >nul 2>&1
if '%errorlevel%' EQU '0' (
    echo Java is already installed.
) else (
    REM Install Java using Chocolatey
    echo Installing Java...
    choco install openjdk -y --confirm

    REM Verify the installation
    echo Verifying Java installation...
    where java >nul 2>&1
    if '%errorlevel%' EQU '0' (
        echo Java was successfully installed.
    ) else (
        echo Java installation failed.
    )
)

REM Pause to keep the window open (optional)
@REM pause
