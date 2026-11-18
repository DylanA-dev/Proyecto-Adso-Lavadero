@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist build\classes mkdir build\classes
dir /s /b ..\jdbc\src\*.java src\*.java > fuentes.txt
javac -encoding UTF-8 -d build\classes -cp ..\lib\mysql-connector-j-9.4.0.jar @fuentes.txt
if errorlevel 1 (
    del fuentes.txt
    echo Error de compilacion.
    pause
    exit /b 1
)
del fuentes.txt
echo Compilacion de escritorio exitosa.
