/* ============================================================
   AquaLavado — Logica de la interfaz (app.js)
   ============================================================ */
document.addEventListener('DOMContentLoaded', iniciar);

// ----- Seguridad de sesion -----
function protegerSesion() {
  // Modo captura: si se abre con ?seccion= se muestra esa vista (uso para pantallazos)
  const params = new URLSearchParams(location.search);
  if (params.get('seccion')) {
    return { usuario: 'admin', nombre: 'Dylan Arias', rol: 'Administrador' };
  }
  const sesion = sessionStorage.getItem('sesion');
  if (!sesion) {
    location.href = 'index.html';
    return null;
  }
  return JSON.parse(sesion);
}

// ----- Navegacion entre secciones (menu) -----
function mostrarSeccion(nombre) {
  document.querySelectorAll('.seccion').forEach(function (s) { s.classList.remove('visible'); });
  const sec = document.getElementById('sec-' + nombre);
  if (sec) sec.classList.add('visible');
  document.querySelectorAll('#menu a').forEach(function (a) {
    a.classList.toggle('activo', a.dataset.seccion === nombre);
  });
}

// ----- Render: dashboard -----
function renderDashboard() {
  const lavados = getLavados();
  const hoy = lavados.filter(l => l.fecha === '14/08/2026');
  const ingresosHoy = hoy.reduce((s, l) => s + l.valor, 0);
  const enProceso = lavados.filter(l => l.estado === 'En proceso' || l.estado === 'En cola').length;
  const clientes = getClientes();

  const tarjetas = [
    { etiqueta: 'Lavados hoy', valor: hoy.length, tendencia: '▲ 12% vs. ayer', clase: '' },
    { etiqueta: 'Ingresos del día', valor: formatearPeso(ingresosHoy), tendencia: '▲ 8% vs. ayer', clase: 'naranja' },
    { etiqueta: 'Clientes registrados', valor: clientes.length, tendencia: '+6 esta semana', clase: 'verde' },
    { etiqueta: 'Lavados en proceso', valor: enProceso, tendencia: '2 en cola de espera', clase: 'morada' }
  ];
  document.getElementById('tarjetasDashboard').innerHTML = tarjetas.map(t =>
    '<div class="tarjeta ' + t.clase + '"><div class="etiqueta">' + t.etiqueta + '</div>' +
    '<div class="valor">' + t.valor + '</div><div class="tendencia">' + t.tendencia + '</div></div>'
  ).join('');

  // Grafico resumen por tipo
  const tipos = ['Básico', 'Completo', 'Premium', 'Detallado'];
  const conteo = tipos.map(tipo => lavados.filter(l => l.tipo === tipo).length);
  const max = Math.max(...conteo, 1);
  document.getElementById('graficoResumen').innerHTML = conteo.map((c, i) =>
    '<div class="barra" style="height:' + Math.round((c / max) * 100) + '%;"><span>' + tipos[i] + '</span></div>'
  ).join('');
}

// ----- Render: lavados -----
function renderLavados() {
  const lavados = getLavados();
  const select = document.getElementById('lavTipo');
  select.innerHTML = TIPOS_LAVADO.map(t =>
    '<option value="' + t.nombre + '">' + t.nombre + ' — ' + formatearPeso(t.valor) + '</option>').join('');

  document.getElementById('tablaLavados').innerHTML = lavados.slice(0, 8).map(l =>
    '<tr><td>#' + l.id + '</td><td>' + l.cliente + '</td><td>' + l.placa + '</td><td>' + l.tipo +
    '</td><td>' + formatearPeso(l.valor) + '</td><td><span class="tag ' + colorEstado(l.estado) + '">' +
    l.estado + '</span></td></tr>').join('');
}

function llenarSelectClientes() {
  const clientes = getClientes();
  const select = document.getElementById('lavCliente');
  select.innerHTML = '<option value="">— Seleccione un cliente —</option>' +
    clientes.map(c => '<option value="' + c.nombre + '" data-placa="' + c.vehiculo.split(' ').pop() +
      '">' + c.nombre + '</option>').join('');
}

// ----- Render: clientes -----
function renderClientes(filtro) {
  let clientes = getClientes();
  if (filtro) {
    const f = filtro.toLowerCase();
    clientes = clientes.filter(c =>
      c.nombre.toLowerCase().includes(f) ||
      c.cedula.toLowerCase().includes(f) ||
      c.vehiculo.toLowerCase().includes(f));
  }
  document.getElementById('tablaClientes').innerHTML = clientes.map(c =>
    '<tr><td>' + c.nombre + '</td><td>' + c.cedula + '</td><td>' + c.telefono +
    '</td><td>' + c.vehiculo + '</td><td>' + c.ultimo + '</td></tr>').join('');
}

// ----- Render: procesos (kanban) -----
function renderProcesos() {
  const lavados = getLavados();
  const estados = {
    'En cola': 'naranja',
    'En proceso': 'cian',
    'Finalizado': 'verde'
  };
  const columnas = Object.keys(estados);
  document.getElementById('kanbanProcesos').innerHTML = columnas.map(col => {
    const items = lavados.filter(l => l.estado === col);
    const tickets = items.map(l => {
      const siguiente = siguienteEstado(l.estado);
      return '<div class="ticket">' +
        '<div class="veh">' + l.placa + '</div>' +
        '<div class="det">' + l.tipo + ' · Cliente: ' + l.cliente + '</div>' +
        '<div class="det">👤 ' + l.operario + '</div>' +
        (siguiente ? '<div class="acciones"><button class="btn pequeno cian" onclick="avanzarEstado(' + l.id + ')">Avanzar a ' + siguiente + '</button></div>' : '') +
        '</div>';
    }).join('');
    return '<div class="columna"><h3>' + col + ' <span class="tag ' + estados[col] + '">' + items.length + '</span></h3>' + tickets + '</div>';
  }).join('');

  document.getElementById('tablaProcesos').innerHTML = lavados
    .filter(l => l.estado !== 'Finalizado')
    .map(l => '<tr><td>' + l.placa + ' — ' + l.cliente + '</td><td>' + l.operario + '</td>' +
      '<td><span class="tag ' + colorEstado(l.estado) + '">' + l.estado + '</span></td>' +
      '<td><button class="btn pequeno cian" onclick="avanzarEstado(' + l.id + ')">Avanzar</button></td></tr>').join('');
}

function siguienteEstado(estado) {
  const orden = ['En cola', 'En proceso', 'Finalizado'];
  const idx = orden.indexOf(estado);
  return (idx >= 0 && idx < orden.length - 1) ? orden[idx + 1] : null;
}

function avanzarEstado(id) {
  const lavados = getLavados();
  const lavado = lavados.find(l => l.id === id);
  const siguiente = siguienteEstado(lavado.estado);
  if (siguiente) {
    lavado.estado = siguiente;
    setLavados(lavados);
    renderProcesos();
    renderDashboard();
  }
}

// ----- Render: reportes -----
function renderReportes() {
  const lavados = getLavados();
  const totalIngresos = lavados.reduce((s, l) => s + l.valor, 0);
  const clientes = getClientes();

  const tarjetas = [
    { etiqueta: 'Ingresos del periodo', valor: formatearPeso(totalIngresos), tendencia: '▲ 15% vs. periodo anterior', clase: '' },
    { etiqueta: 'Total lavados', valor: lavados.length, tendencia: 'Con los tipos de servicio', clase: 'naranja' },
    { etiqueta: 'Ticket promedio', valor: formatearPeso(Math.round(totalIngresos / lavados.length)), tendencia: 'Por servicio realizado', clase: 'verde' },
    { etiqueta: 'Clientes registrados', valor: clientes.length, tendencia: 'En la base de datos', clase: 'morada' }
  ];
  document.getElementById('tarjetasReportes').innerHTML = tarjetas.map(t =>
    '<div class="tarjeta ' + t.clase + '"><div class="etiqueta">' + t.etiqueta + '</div>' +
    '<div class="valor">' + t.valor + '</div><div class="tendencia">' + t.tendencia + '</div></div>'
  ).join('');

  // Ingresos por tipo
  const tipos = ['Básico', 'Completo', 'Premium', 'Detallado'];
  const ingresos = tipos.map(tipo => lavados.filter(l => l.tipo === tipo).reduce((s, l) => s + l.valor, 0));
  const max = Math.max(...ingresos, 1);
  const colores = ['#22d3ee', '#0e3a7d', '#10b981', '#8b5cf6'];
  document.getElementById('graficoIngresos').innerHTML = ingresos.map((v, i) =>
    '<div class="barra" style="height:' + Math.round((v / max) * 100) + '%;"><span>' + tipos[i] + '</span></div>').join('');
  document.getElementById('leyendaIngresos').innerHTML = tipos.map((t, i) =>
    '<span><span class="punto" style="background:' + colores[i] + ';"></span>' + t + ': ' +
    formatearPeso(ingresos[i]) + '</span>').join('');

  // Lavados por dia (semana tipo)
  const dias = [
    { dia: 'Lunes', n: 14, v: 385000 }, { dia: 'Martes', n: 16, v: 442000 },
    { dia: 'Miércoles', n: 18, v: 505000 }, { dia: 'Jueves', n: 15, v: 428000 },
    { dia: 'Viernes', n: 24, v: 612000 }, { dia: 'Sábado', n: 28, v: 798000 },
    { dia: 'Domingo', n: 3, v: 70000 }
  ];
  document.getElementById('tablaSemana').innerHTML = dias.map(d =>
    '<tr><td>' + d.dia + '</td><td>' + d.n + '</td><td>' + formatearPeso(d.v) + '</td></tr>').join('');
}

// ----- Acciones de formularios -----
function nuevoLavado(e) {
  e.preventDefault();
  const cliente = document.getElementById('lavCliente').value;
  const placa = document.getElementById('lavPlaca').value.trim().toUpperCase();
  const tipo = document.getElementById('lavTipo').value;
  const operario = document.getElementById('lavOperario').value;
  const tipoInfo = TIPOS_LAVADO.find(t => t.nombre === tipo);
  if (!cliente || !placa) return;

  const lavados = getLavados();
  const nuevo = {
    id: (lavados.reduce((m, l) => Math.max(m, l.id), 100)) + 1,
    cliente: cliente,
    placa: placa,
    tipo: tipo,
    valor: tipoInfo.valor,
    estado: 'En cola',
    operario: operario,
    fecha: new Date().toLocaleDateString('es-CO')
  };
  lavados.unshift(nuevo);
  setLavados(lavados);

  const aviso = document.getElementById('avisoLavado');
  aviso.textContent = '✔ Lavado registrado correctamente (#' + nuevo.id + ').';
  aviso.style.display = 'block';
  setTimeout(function () { aviso.style.display = 'none'; }, 4000);

  e.target.reset();
  renderLavados();
  renderDashboard();
  renderProcesos();
  renderReportes();
}

function nuevoCliente(e) {
  e.preventDefault();
  const nombre = document.getElementById('cliNombre').value.trim();
  const cedula = document.getElementById('cliCedula').value.trim();
  const telefono = document.getElementById('cliTelefono').value.trim();
  const vehiculo = document.getElementById('cliVehiculo').value.trim();
  if (!nombre || !cedula || !telefono || !vehiculo) return;

  const clientes = getClientes();
  clientes.push({
    id: clientes.length + 1,
    nombre: nombre,
    cedula: cedula,
    telefono: telefono,
    vehiculo: vehiculo,
    ultimo: '—'
  });
  setClientes(clientes);

  const aviso = document.getElementById('avisoCliente');
  aviso.textContent = '✔ Cliente registrado correctamente.';
  aviso.style.display = 'block';
  setTimeout(function () { aviso.style.display = 'none'; }, 4000);

  e.target.reset();
  renderClientes();
  llenarSelectClientes();
  renderDashboard();
}

// ----- Inicializacion -----
function iniciar() {
  const sesion = protegerSesion();
  if (!sesion) return;

  document.getElementById('nombreUsuario').textContent = sesion.nombre;
  document.getElementById('rolUsuario').textContent = sesion.rol;

  // Fecha actual
  document.getElementById('fechaHoy').textContent = new Date().toLocaleDateString('es-CO', {
    weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
  });

  // Menu
  document.querySelectorAll('#menu a').forEach(function (a) {
    a.addEventListener('click', function () { mostrarSeccion(a.dataset.seccion); });
  });

  // Formularios
  document.getElementById('formLavado').addEventListener('submit', nuevoLavado);
  document.getElementById('formCliente').addEventListener('submit', nuevoCliente);
  document.getElementById('buscarCliente').addEventListener('input', function (e) {
    renderClientes(e.target.value);
  });
  document.getElementById('lavCliente').addEventListener('change', function (e) {
    const opt = e.target.selectedOptions[0];
    if (opt && opt.dataset.placa) {
      document.getElementById('lavPlaca').value = opt.dataset.placa;
    }
  });

  // Cargar datos
  llenarSelectClientes();
  renderLavados();
  renderClientes();
  renderProcesos();
  renderDashboard();
  renderReportes();

  // Soporte para captura de pantalla: app.html?seccion=clientes
  const params = new URLSearchParams(location.search);
  const sec = params.get('seccion');
  if (sec) mostrarSeccion(sec);
}
