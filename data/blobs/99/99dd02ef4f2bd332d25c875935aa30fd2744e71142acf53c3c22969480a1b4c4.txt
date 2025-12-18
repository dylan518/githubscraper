package main;

import java.util.ArrayList;
import java.util.List;

public class Data {
    private List<Integer> results = new ArrayList<>();

    public void save(int result) {
        results.add(result);
    }

    public List<Integer> getResults() {
        return results;
    }
}

