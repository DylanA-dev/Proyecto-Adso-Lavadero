@echo off
chcp 65001 >nul
cd /d "%~dp0"
start "" javaw -cp "build\classes;..\lib\mysql-connector-j-9.4.0.jar" com.aqualavado.escritorio.AplicacionEscritorio
