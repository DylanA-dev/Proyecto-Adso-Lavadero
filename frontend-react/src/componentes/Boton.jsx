/**
 * Botón reutilizable con estado de bloqueo.
 */
export default function Boton({
  children,
  tipo = "button",
  variante = "normal",
  bloqueado = false,
  alHacerClic
}) {
  return (
    <button
      type={tipo}
      className={`boton boton-${variante}`}
      disabled={bloqueado}
      onClick={alHacerClic}
    >
      {children}
    </button>
  );
}
