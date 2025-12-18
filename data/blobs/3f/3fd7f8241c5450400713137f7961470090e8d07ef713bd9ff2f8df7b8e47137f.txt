package ej7;

public class EncargadoPrestamos implements IAgentePago{
    private IAgentePago next;
    @Override
    public void setNext(IAgentePago agentePago) {
        next = agentePago;
    }
    @Override
    public IAgentePago next() {
        return next;
    }
    @Override
    public void pagarDeuda(int monto) {
        if(SingletonPrestamo.getInstance().getMontoPagado() == SingletonPrestamo.getInstance().getMontoOriginal()) {
            System.out.println("Aqui tiene todos sus documentos, gracias por su confianza!");
        } else {
            System.out.println("Parece que hubo un problema! Revise sus pagos...");
        }
    }

}
