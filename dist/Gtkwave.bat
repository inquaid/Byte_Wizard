@echo off

REM Check if the script is running with administrative privileges
openfiles >nul 2>&1
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

REM Check if GTKWave is already installed
where gtkwave >nul 2>&1
if '%errorlevel%' EQU '0' (
    echo GTKWave is already installed.
    powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('GTKWAVE is already installed', 'Alert', 'OK', 'Information')"
) else (
    REM Install GTKWave using Chocolatey
    echo Installing GTKWave...
    choco install gtkwave -y --confirm

    REM Verify the installation
    echo Verifying GTKWave installation...
    where gtkwave >nul 2>&1
    if '%errorlevel%' EQU '0' (
        echo GTKWave was successfully installed.
        powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('GTKWAVE installation is successful', 'Alert', 'OK', 'Information')"
    ) else (
        echo GTKWave installation failed.
        powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('Failed to install GTKWAVE', 'Alert', 'OK', 'Information')"
    )
)

REM Pause to keep the window open (optional)
REM pause
