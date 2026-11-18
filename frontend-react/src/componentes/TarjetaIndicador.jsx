/**
 * Tarjeta de indicador del panel principal.
 */
export default function TarjetaIndicador({ etiqueta, valor, detalle }) {
  return (
    <article className="tarjeta">
      <span className="etiqueta">{etiqueta}</span>
      <strong>{valor}</strong>
      <small>{detalle}</small>
    </article>
  );
}
