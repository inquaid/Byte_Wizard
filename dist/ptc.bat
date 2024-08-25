@echo off
setlocal enabledelayedexpansion

REM Loop from 1 to 1000
for /l %%i in (1,1,100000) do (
    echo %%i
)

endlocal
