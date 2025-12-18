package org.example.manager;

import org.example.data.Post;
import org.example.data.User;

import java.util.ArrayList;
import java.util.List;

public class PostManager {

    private List<Post> postList;
    private static Integer postCnt = 0;
    private final UserManager userManager;
    public PostManager(UserManager userManager){
        this.userManager = userManager;
        this.postList = new ArrayList<>();
    }

    public Post uploadPost(Integer userId,String postContent) throws Exception {
        postCnt++;
        Post newPost = new Post(postCnt,postContent);

        List<User> userList = this.userManager.getUserList();

        for(User user:userList){
            if(user.getUserId() == userId){
                user.setPosts(newPost);
                this.postList.add(newPost);
                return newPost;
            }
        }

        throw new Exception("User with "+userId+" not found");

    }

    public void handleActionOnPost(String actionType,Integer userId,Integer postId) throws Exception {
        for(Post post:this.postList){
            if(post.getPostId() == postId){

                if(actionType.equals("LIKE")){
                    int cnt = post.getLikes();
                    post.setLikes(cnt++);
                    System.out.println("Post Liked..!");
                    break;
                }
                else if(actionType.equals("DISLIKE")){
                    int cnt = post.getDislikes();
                    post.setDislikes(cnt++);
                    System.out.println("Post Disliked..!");
                    break;
                }
                else{
                    throw  new RuntimeException("Please enter a valid post action like LIKE/DISLIKE");
                }

            }
        }
        throw new Exception("No valid post found with ID "+postId);

    }
}
