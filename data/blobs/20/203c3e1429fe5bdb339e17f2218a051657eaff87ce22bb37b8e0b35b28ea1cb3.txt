package Assignment3.Iterator;

import java.util.ArrayList;
import java.util.List;

public class ListMovieCollection {
    private List<String> movies;

    public ListMovieCollection() {
        this.movies = new ArrayList<>();
    }

    public void addMovie(String movie) {
        movies.add(movie);
    }

    public Iterator<String> createIterator() {
        return new ListMovieIterator(movies);
    }
}
