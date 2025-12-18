import java.util.*;
import java.util.stream.Collectors;

public class SocialMediaAnalyticsTool {
    private Set<SocialMediaPost> posts;

    public SocialMediaAnalyticsTool() {
        this.posts = new HashSet<>();
    }

    public boolean addPost(SocialMediaPost post) {
        if (post != null) {
            return posts.add(post);
        } else {
            System.out.println("Cannot add a null post.");
            return false;
        }
    }

    public int getTotalLikes() {
        return posts.stream().mapToInt(SocialMediaPost::getNumLikes).sum();
    }

    public int getTotalComments() {
        return posts.stream().mapToInt(SocialMediaPost::getNumComments).sum();
    }

    public int getTotalShares() {
        return posts.stream().mapToInt(SocialMediaPost::getNumShares).sum();
    }

    public Map<String, Integer> getTopUsersByLikes(int topN) {
        if (topN <= 0 || topN > posts.size()) {
            System.out.println("Invalid topN value. Returning an empty map.");
            return Collections.emptyMap();
        }

        Map<String, Integer> topUsers = new LinkedHashMap<>();
        List<SocialMediaPost> sortedPosts = posts.stream()
                .sorted(Comparator.comparingInt(SocialMediaPost::getNumLikes).reversed())
                .limit(topN)
                .collect(Collectors.toList());

        for (SocialMediaPost post : sortedPosts) {
            topUsers.put(post.getUsername(), post.getNumLikes());
        }

        return topUsers;
    }
}
