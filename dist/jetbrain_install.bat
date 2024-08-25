@echo off

REM Check if the script is running with administrative privileges
openfiles >nul 2>&1
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

REM Check if JetBrains Toolbox is already installed
where toolbox >nul 2>&1
if '%errorlevel%' EQU '0' (
    echo JetBrains Toolbox is already installed.
) else (
    REM Install JetBrains Toolbox using Chocolatey
    echo Installing JetBrains Toolbox...
    choco install jetbrainstoolbox -y --confirm

    REM Verify the installation
    echo Verifying JetBrains Toolbox installation...
    where toolbox >nul 2>&1
    if '%errorlevel%' EQU '0' (
        echo JetBrains Toolbox was successfully installed.
    ) else (
        echo JetBrains Toolbox installation failed.
    )
)

REM Pause to keep the window open (optional)
@REM pause
