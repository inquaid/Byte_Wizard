@echo off

REM Check if the script is running with administrative privileges
openfiles >nul 2>&1
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

REM Check if Icarus Verilog (iverilog) is already installed
where iverilog >nul 2>&1
if '%errorlevel%' EQU '0' (
    echo Icarus Verilog is already installed.
    powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('Iverilog is already installed', 'Alert', 'OK', 'Information')"

) else (
    REM Install Icarus Verilog using Chocolatey
    echo Installing Icarus Verilog...
    choco install iverilog -y --confirm

    REM Verify the installation
    echo Verifying Icarus Verilog installation...
    where iverilog >nul 2>&1
    if '%errorlevel%' EQU '0' (
        echo Icarus Verilog was successfully installed.
        powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('Iverilog installation is successful', 'Alert', 'OK', 'Information')"

    ) else (
        echo Icarus Verilog installation failed.
        powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('Failed to install Iverilog', 'Alert', 'OK', 'Information')"

    )
)

REM Pause to keep the window open (optional)
@REM pause
