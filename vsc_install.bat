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
    powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('VSCode is already installed', 'Alert', 'OK', 'Information')"

) else (
    REM Install Visual Studio Code using Chocolatey
    echo Installing Visual Studio Code...
    choco install vscode -y --confirm

    REM Verify the installation
    echo Verifying Visual Studio Code installation...
    where code >nul 2>&1
    if '%errorlevel%' EQU '0' (
        echo Visual Studio Code was successfully installed.
        powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('VSCode installation is successful', 'Alert', 'OK', 'Information')"
    ) else (
        echo Visual Studio Code installation failed.
        powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('Failed to install VSCode', 'Alert', 'OK', 'Information')"

    )
)

REM Pause to keep the window open (optional)
@REM pause
