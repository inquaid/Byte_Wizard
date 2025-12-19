@echo off

REM Check if the script is running with administrative privileges
openfiles >nul 2>&1
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

REM Check if Chocolatey is already installed
where choco >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Chocolatey is already installed.
    powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('Chocolatey is already installed', 'Alert', 'OK', 'Information')"
    exit /b 0
)

REM Set up Chocolatey installation
set "chocoInstallUrl=https://community.chocolatey.org/install.ps1"

REM Download and run the installation script
powershell -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('%chocoInstallUrl%'))"

REM Verify installation
@REM choco --version
powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('Choco installation is successful', 'Alert', 'OK', 'Information')"
@REM pause
