@echo off
chcp 65001 >nul
"C:\xampp\mysql\bin\mysql.exe" -u root --default-character-set=utf8mb4 -e "USE aqualavado; SHOW TABLES; SELECT o.id_orden, v.placa, s.nombre AS servicio, o.estado, o.valor FROM ordenes_lavado o INNER JOIN vehiculos v ON v.id_vehiculo = o.id_vehiculo INNER JOIN servicios s ON s.id_servicio = o.id_servicio ORDER BY o.id_orden;"
echo.
pause
