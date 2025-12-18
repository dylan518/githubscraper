package Assignment3.Iterator;

import java.util.List;

public class ListMovieCollection {
    private List<String> movie;

    public ListMovieCollection(List<String> movies) {
        this.movie = movies;
    }

    public Iterator<String> createListMovie() {
        return new ListMovieIterator(movie);
    }
}
