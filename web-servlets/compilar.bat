@echo off
chcp 65001 >nul
cd /d "%~dp0"

set TOMCAT=C:\xampp\tomcat
set SALIDA=build\web

if exist %SALIDA% rmdir /s /q %SALIDA%
mkdir %SALIDA%\WEB-INF\classes
mkdir %SALIDA%\WEB-INF\lib
xcopy web\* %SALIDA%\ /E /I /Y >nul

dir /s /b ..\jdbc\src\*.java src\*.java > fuentes.txt
javac --release 17 -encoding UTF-8 -d %SALIDA%\WEB-INF\classes -cp "%TOMCAT%\lib\servlet-api.jar" @fuentes.txt
if errorlevel 1 (
    del fuentes.txt
    echo Error de compilacion.
    exit /b 1
)
del fuentes.txt
copy ..\lib\mysql-connector-j-9.4.0.jar %SALIDA%\WEB-INF\lib\ >nul
echo Compilacion web exitosa.
