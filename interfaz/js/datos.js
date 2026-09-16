/* ============================================================
   AquaLavado — Modulo de datos
   Persistencia en localStorage con datos semilla de ejemplo.
   ============================================================ */
const CLAVE_LAVADOS = 'aqualavado_lavados';
const CLAVE_CLIENTES = 'aqualavado_clientes';

const LAVADOS_SEMILLA = [
  { id: 124, cliente: 'Carlos Muñoz', placa: 'ABC123', tipo: 'Premium', valor: 45000, estado: 'Finalizado', operario: 'Juan P.', fecha: '14/08/2026' },
  { id: 125, cliente: 'María Gómez', placa: 'XYZ789', tipo: 'Completo', valor: 32000, estado: 'En proceso', operario: 'Juan P.', fecha: '14/08/2026' },
  { id: 126, cliente: 'Julián Ríos', placa: 'QWE456', tipo: 'Básico', valor: 18000, estado: 'En cola', operario: 'Camilo R.', fecha: '14/08/2026' },
  { id: 127, cliente: 'Luisa Torres', placa: 'RTY741', tipo: 'Detallado', valor: 60000, estado: 'En cola', operario: 'Camilo R.', fecha: '14/08/2026' },
  { id: 128, cliente: 'Andrés Salazar', placa: 'FGH852', tipo: 'Completo', valor: 32000, estado: 'Finalizado', operario: 'Juan P.', fecha: '13/08/2026' },
  { id: 129, cliente: 'Sara Peña', placa: 'JKL963', tipo: 'Premium', valor: 45000, estado: 'Finalizado', operario: 'Camilo R.', fecha: '13/08/2026' },
  { id: 130, cliente: 'Óscar Rojas', placa: 'MNB321', tipo: 'Básico', valor: 18000, estado: 'Finalizado', operario: 'Juan P.', fecha: '13/08/2026' },
];

const CLIENTES_SEMILLA = [
  { id: 1, nombre: 'Carlos Muñoz', cedula: '1114523887', telefono: '3105552241', vehiculo: 'Renault ABC123', ultimo: '14/08/2026' },
  { id: 2, nombre: 'María Gómez', cedula: '1098774120', telefono: '3127748890', vehiculo: 'Mazda XYZ789', ultimo: '14/08/2026' },
  { id: 3, nombre: 'Julián Ríos', cedula: '1005221456', telefono: '3152209965', vehiculo: 'Chevrolet QWE456', ultimo: '13/08/2026' },
  { id: 4, nombre: 'Luisa Torres', cedula: '1132908335', telefono: '3168834451', vehiculo: 'Kia RTY741', ultimo: '12/08/2026' },
  { id: 5, nombre: 'Andrés Salazar', cedula: '1145667209', telefono: '3114471108', vehiculo: 'Nissan FGH852', ultimo: '11/08/2026' },
  { id: 6, nombre: 'Sara Peña', cedula: '1082150033', telefono: '3172208845', vehiculo: 'Toyota JKL963', ultimo: '10/08/2026' },
];

const TIPOS_LAVADO = [
  { nombre: 'Básico', valor: 18000 },
  { nombre: 'Completo', valor: 32000 },
  { nombre: 'Premium', valor: 45000 },
  { nombre: 'Detallado', valor: 60000 },
];

function cargarDatos(clave, semilla) {
  const datos = localStorage.getItem(clave);
  if (datos) {
    try { return JSON.parse(datos); } catch (e) { /* ignorar */ }
  }
  localStorage.setItem(clave, JSON.stringify(semilla));
  return JSON.parse(JSON.stringify(semilla));
}

function guardarDatos(clave, datos) {
  localStorage.setItem(clave, JSON.stringify(datos));
}

function getLavados() { return cargarDatos(CLAVE_LAVADOS, LAVADOS_SEMILLA); }
function setLavados(datos) { guardarDatos(CLAVE_LAVADOS, datos); }
function getClientes() { return cargarDatos(CLAVE_CLIENTES, CLIENTES_SEMILLA); }
function setClientes(datos) { guardarDatos(CLAVE_CLIENTES, datos); }

function formatearPeso(valor) {
  return '$' + Number(valor).toLocaleString('es-CO');
}

function colorEstado(estado) {
  const mapa = {
    'Finalizado': 'verde',
    'En proceso': 'cian',
    'En cola': 'naranja',
    'Pendiente': 'azul'
  };
  return mapa[estado] || 'azul';
}
