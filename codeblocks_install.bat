@echo off

REM Check if the script is running with administrative privileges
openfiles >nul 2>&1
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

REM Check if Code::Blocks is already installed
where codeblocks >nul 2>&1
if '%errorlevel%' EQU '0' (
    echo Code::Blocks is already installed.
) else (
    REM Install Code::Blocks using Chocolatey
    echo Installing Code::Blocks...
    choco install codeblocks -y --confirm

    REM Verify the installation
    echo Verifying Code::Blocks installation...
    where codeblocks >nul 2>&1
    if '%errorlevel%' EQU '0' (
        echo Code::Blocks was successfully installed.
    ) else (
        echo Code::Blocks installation failed.
    )
)

REM Pause to keep the window open (optional)
@REM pause
