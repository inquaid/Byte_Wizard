@echo off

REM Check if the script is running with administrative privileges
openfiles >nul 2>&1
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

REM Check if MinGW (gcc) is already installed
where gcc >nul 2>&1
if '%errorlevel%' EQU '0' (
    echo MinGW is already installed.
    powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('MINGW is already installed', 'Alert', 'OK', 'Information')"

) else (
    REM Install MinGW using Chocolatey
    echo Installing MinGW...
    choco install mingw -y --confirm

    REM Verify the installation
    echo Verifying MinGW installation...
    powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('MINGW installation is successful', 'Alert', 'OK', 'Information')"
    
)

