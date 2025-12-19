@echo off
setlocal enabledelayedexpansion

rem Loop from 1 to 5
for /l %%i in (1, 1, 1000) do (
    echo Loop iteration: %%i
    rem Simulate a delay
    timeout /t 1 >nul
)

echo Loop completed.

