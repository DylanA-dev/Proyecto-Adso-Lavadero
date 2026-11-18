@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist build\classes mkdir build\classes
dir /s /b src\*.java > archivos.txt
javac -encoding UTF-8 -d build\classes -cp ..\lib\mysql-connector-j-9.4.0.jar @archivos.txt
del archivos.txt
if errorlevel 1 (
    echo Error de compilacion.
    pause
    exit /b 1
)
echo Compilacion exitosa.
