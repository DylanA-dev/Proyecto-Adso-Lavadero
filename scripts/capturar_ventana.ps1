param(
    [string]$Titulo,
    [string]$Salida,
    [int]$Espera = 2000
)

Add-Type -AssemblyName System.Drawing
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Ventana {
    [StructLayout(LayoutKind.Sequential)]
    public struct RECT { public int Left; public int Top; public int Right; public int Bottom; }
    [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr hWnd, out RECT rect);
    [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr hWnd);
    [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr hWnd, int comando);
}
"@

$proceso = $null
for ($i = 0; $i -lt 60; $i++) {
    $proceso = Get-Process | Where-Object {
        $_.MainWindowHandle -ne 0 -and $_.MainWindowTitle -like "*$Titulo*"
    } | Select-Object -First 1
    if ($proceso) { break }
    Start-Sleep -Milliseconds 250
}
if (-not $proceso) { Write-Error "No se encontró la ventana $Titulo"; exit 1 }

[Ventana]::ShowWindow($proceso.MainWindowHandle, 9) | Out-Null
[Ventana]::SetForegroundWindow($proceso.MainWindowHandle) | Out-Null
Start-Sleep -Milliseconds $Espera

$rect = New-Object Ventana+RECT
[Ventana]::GetWindowRect($proceso.MainWindowHandle, [ref]$rect) | Out-Null
$ancho = $rect.Right - $rect.Left
$alto = $rect.Bottom - $rect.Top
if ($ancho -le 0 -or $alto -le 0) { Write-Error "Ventana sin tamaño válido ($ancho x $alto)"; exit 1 }

$carpeta = Split-Path -Parent $Salida
if (-not (Test-Path $carpeta)) { New-Item -ItemType Directory -Force -Path $carpeta | Out-Null }

$bitmap = New-Object System.Drawing.Bitmap $ancho, $alto
$grafico = [System.Drawing.Graphics]::FromImage($bitmap)
$grafico.CopyFromScreen($rect.Left, $rect.Top, 0, 0, $bitmap.Size)
$bitmap.Save($Salida, [System.Drawing.Imaging.ImageFormat]::Png)
$grafico.Dispose()
$bitmap.Dispose()
Write-Output "Captura guardada en $Salida ($ancho x $alto)"
