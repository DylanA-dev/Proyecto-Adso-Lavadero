param(
    [string]$Titulo,
    [string]$Salida
)

Add-Type -AssemblyName System.Drawing
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Captura {
    [StructLayout(LayoutKind.Sequential)]
    public struct RECT { public int Left; public int Top; public int Right; public int Bottom; }
    [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr hWnd, out RECT rect);
    [DllImport("user32.dll")] public static extern bool PrintWindow(IntPtr hWnd, IntPtr hdc, uint flags);
}
"@

$proceso = $null
for ($i = 0; $i -lt 40; $i++) {
    $proceso = Get-Process | Where-Object {
        $_.MainWindowHandle -ne 0 -and $_.MainWindowTitle -like "*$Titulo*"
    } | Select-Object -First 1
    if ($proceso) { break }
    Start-Sleep -Milliseconds 250
}
if (-not $proceso) { Write-Error "No se encontró la ventana $Titulo"; exit 1 }

$rect = New-Object Captura+RECT
[Captura]::GetWindowRect($proceso.MainWindowHandle, [ref]$rect) | Out-Null
$ancho = $rect.Right - $rect.Left
$alto = $rect.Bottom - $rect.Top
if ($ancho -le 0 -or $alto -le 0) { Write-Error "Ventana sin tamaño válido"; exit 1 }

$carpeta = Split-Path -Parent $Salida
if (-not (Test-Path $carpeta)) { New-Item -ItemType Directory -Force -Path $carpeta | Out-Null }

$bitmap = New-Object System.Drawing.Bitmap $ancho, $alto
$grafico = [System.Drawing.Graphics]::FromImage($bitmap)
$hdc = $grafico.GetHdc()
$ok = [Captura]::PrintWindow($proceso.MainWindowHandle, $hdc, 2)
$grafico.ReleaseHdc($hdc)
$grafico.Dispose()
$bitmap.Save($Salida, [System.Drawing.Imaging.ImageFormat]::Png)
$bitmap.Dispose()
Write-Output "PrintWindow=$ok -> $Salida ($ancho x $alto)"
