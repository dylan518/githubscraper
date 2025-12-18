package RMI;

import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class MathServer {

    public static void main(String[] args) throws RemoteException {

        MathService mathService = new MathServiceImpl();

        Registry registry = LocateRegistry.createRegistry(1099);
        registry.rebind("MathService", mathService);

        System.out.println("MathService is registered and ready !!");
    }
}
