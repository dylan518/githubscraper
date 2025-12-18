package application;

import entities.Comment;
import entities.Post;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) throws ParseException {

        Comment c1 = new Comment("Have a nice trip!");
        Comment c2 = new Comment("Wow, thats is awesome!");
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        Post p1 = new Post(12,
                sdf.parse("21/06/2018 13:05:44"), "Traveling to new zealand",
                "I'm going to visit this wonderful country!");

        p1.addComment(c1);
        p1.addComment(c2);
        System.out.println(p1);

    }
}
