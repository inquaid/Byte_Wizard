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
) else (
    REM Install NetBeans using Chocolatey
    echo Installing NetBeans...
    choco install netbeans -y --confirm

    REM Verify the installation
    echo Verifying NetBeans installation...
    where netbeans >nul 2>&1
    if '%errorlevel%' EQU '0' (
        echo NetBeans was successfully installed.
    ) else (
        echo NetBeans installation failed.
    )
)

REM Pause to keep the window open (optional)
@REM pause
