package iterator;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Board {

    private final List<Post> posts = new ArrayList<>();

    public void addPost(String title) {
        posts.add(new Post(title, LocalDateTime.now()));
    }

    // @Getter
    public List<Post> getPosts() {
        return posts;
    }

    public Iterator<Post> getDefaultIterator() {
        return posts.iterator();
    }

    public Iterator<Post> getRecentPostIterator() {
        return new RecentPostIterator(posts);
    }
}
