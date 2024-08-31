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
    powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('Python is already installed', 'Alert', 'OK', 'Information')"

) else (
    REM Install Python using Chocolatey
    echo Installing Python...
    choco install python -y --confirm

    REM Verify the installation
    echo Verifying Python installation...
    where python >nul 2>&1
    if '%errorlevel%' EQU '0' (
        echo Python was successfully installed.
        powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('Python installation is successful', 'Alert', 'OK', 'Information')"
    ) else (
        echo Python installation failed.
rem        powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('Failed to install Python', 'Alert', 'OK', 'Information')"

    )
)

REM Pause to keep the window open (optional)
@REM pause
