package edu.escuelaing.co.app.framework.api;

import java.util.HashMap;

public class Routes {

    private HashMap<String, ApiController> rutas = new HashMap<String, ApiController>();
    private static Routes _instance = new Routes();

    private Routes() {
    }

    public static Routes getInstance() {
        return _instance;
    }

    public void addRoute(String key, ApiController res) {
        rutas.put(key, res);
    }

    public ApiController getRoute(String key) {
        return rutas.get(key);
    }

    public boolean exists(String key) {
        return rutas.containsKey(key);
    }

}
