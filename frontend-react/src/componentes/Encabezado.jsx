/**
 * Encabezado de cada sección de la aplicación.
 */
export default function Encabezado({ titulo, descripcion }) {
  return (
    <header className="cabecera">
      <h1>{titulo}</h1>
      <p>{descripcion}</p>
    </header>
  );
}
