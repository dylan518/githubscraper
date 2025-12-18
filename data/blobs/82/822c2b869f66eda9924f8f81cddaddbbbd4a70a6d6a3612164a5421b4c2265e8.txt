package edu.uade.tpo.gestora.criterios;

import edu.uade.tpo.Consorcio;
import edu.uade.tpo.UnidadFuncional;
import edu.uade.tpo.pagos.Pago;
import edu.uade.tpo.utils.LogUtil;

// Puede ser singleton
public class PagoCompletoYGenerarFuturosFondosDeReserva extends CriterioPago {

  @Override
  public void divisionExpensas(Consorcio consorcio) {
    double gasto = calcularGasto(consorcio.getPeriodoActivo());

    for (UnidadFuncional uf: consorcio.getUnidadesFuncionales()) {
      double porcentaje = uf.getPocentajeDePago();

      double montoExpensa = gasto * porcentaje;
      double agregadoParaFondo = montoExpensa * 0.1;
      new LogUtil().logMessage("el monto a pagar por %s es $%.2f", uf.getId(), montoExpensa);
      new LogUtil().logMessage("el monto a pagar para agregar al fondo de reserva es $%.2f", agregadoParaFondo);

      Pago pago = new Pago(montoExpensa + agregadoParaFondo);

      consorcio.getCuentaBancaria().agregarSaldo(agregadoParaFondo);

      uf.agregarPago(pago);
      notificar(uf, pago);
    }
  }
}
