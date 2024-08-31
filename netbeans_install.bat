@echo off

REM Check if the script is running with administrative privileges
openfiles >nul 2>&1
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

REM Check if NetBeans is already installed
where netbeans >nul 2>&1
if '%errorlevel%' EQU '0' (
    echo NetBeans is already installed.
    powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('NetBeans is already installed', 'Alert', 'OK', 'Information')"
) else (
    REM Install NetBeans using Chocolatey
    echo Installing NetBeans...
    choco install netbeans -y --confirm

    REM Verify the installation
    echo Verifying NetBeans installation...
    where netbeans >nul 2>&1
    if '%errorlevel%' EQU '0' (
        echo NetBeans was successfully installed.
        powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('NetBeans installation is successful', 'Alert', 'OK', 'Information')"
    ) else (
        echo NetBeans installation failed.
rem        powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('Failed to install NetBeans', 'Alert', 'OK', 'Information')"

    )
)

REM Pause to keep the window open (optional)
@REM pause
