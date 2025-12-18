package data.Models;

import data.repository.CommentRepository;
import data.repository.CommentRepositoryImpl;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;

import static org.junit.jupiter.api.Assertions.*;

class CommentRepositoryImplTest {
    private Comment comment;
    private CommentRepository commentRepository;

    @BeforeEach
public void doThis(){
        commentRepository = new CommentRepositoryImpl();
        comment =new Comment();
        comment.setId(2);
        comment.setComment("dbdb");
        comment.setArticleId(3);
        comment.setUserId(8);
    }
    @Test
    public void saveOneComment_CountCommentIsOneTest(){
        Comment comment =new Comment();
        commentRepository.saveComment(comment);
        assertEquals(1,commentRepository.countComment());
    }
   @Test
   public void CountComment(){
        commentRepository.countComment();
        assertEquals(0,commentRepository.countComment());
   }
   @Test
    public void findComment(){
        commentRepository.findComment(comment);
        assertEquals(0,commentRepository.countComment());
   }
   @Test
    public void deleteComment(){
       Comment comment =new Comment();
       commentRepository.saveComment(comment);
        assertEquals(1,commentRepository.countComment());
        commentRepository.deleteComment(comment);
        assertEquals(0,commentRepository.countComment());
   }

}