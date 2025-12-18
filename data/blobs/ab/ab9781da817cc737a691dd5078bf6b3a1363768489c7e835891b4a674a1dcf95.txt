package com._07UsoDemoSingletonPrototype;

/**
 *
 * @author Roberto Garrido Trillo
 */
public class Secretario implements IEmpleados {

   public Secretario (ICreacionInformes informeNuevo)
   {
      this.informeNuevo = informeNuevo;
   }

   @Override
   public String getInforme ()
   {
      return "Informe creado por el Secretario: " + informeNuevo.getinforme();
   }

   // Creacion de campo tipo CreacionInforme (interface)
   private ICreacionInformes informeNuevo;
}
