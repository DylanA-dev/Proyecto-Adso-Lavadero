@echo off
chcp 65001 >nul
cd /d "%~dp0"
call compilar.bat
if errorlevel 1 exit /b 1

set DESTINO=C:\xampp\tomcat\webapps\aqualavado
if exist "%DESTINO%" rmdir /s /q "%DESTINO%"
xcopy "build\web" "%DESTINO%" /E /I /Y >nul
echo Aplicacion desplegada en %DESTINO%
echo Inicie Tomcat con C:\xampp\tomcat\bin\startup.bat
