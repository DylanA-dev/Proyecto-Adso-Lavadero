const ETIQUETAS = {
  EN_COLA: "En cola",
  EN_PROCESO: "En proceso",
  FINALIZADO: "Finalizado",
  ENTREGADO: "Entregado"
};

/**
 * Etiqueta visual del estado de una orden de lavado.
 */
export default function EstadoOrden({ estado }) {
  return (
    <span className={`estado estado-${estado.toLowerCase()}`}>
      {ETIQUETAS[estado] ?? estado}
    </span>
  );
}
