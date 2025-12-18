import java.util.ArrayList;
public class CarritoCompra {
    private
        Cliente cliente;
        ArrayList<Stock> productos;
        double total;

    public CarritoCompra(Cliente cliente, ArrayList<Stock> productos, double total) {
        this.cliente = cliente;
        this.productos = productos;
        this.total = total;
    }

    public CarritoCompra() {
        this.cliente = new Cliente();
        this.productos = new ArrayList<Stock>();
        this.total = 0.0;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public ArrayList<Stock> getProductos() {
        return productos;
    }

    public double getTotal() {
        return total;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public void setProductos(ArrayList<Stock> productos) {
        this.productos = productos;
    }

    public void setTotal(double total) {
        this.total = total;
    }

    public void addProducto(Stock producto) {
        this.productos.add(producto);
    }

    public void removeProducto(Stock producto) {
        this.productos.remove(producto);
    }

    public void calcularTotal() {
        double total = 0.0;
        for (Stock producto : this.productos) {
            total += producto.getProducto().getPrecio();
        }
        this.total = total;
    }

    @Override
    public String toString() {
        return "CarritoCompra [cliente=" + cliente + ", productos=" + productos + ", total=" + total + "]";
    }
}
