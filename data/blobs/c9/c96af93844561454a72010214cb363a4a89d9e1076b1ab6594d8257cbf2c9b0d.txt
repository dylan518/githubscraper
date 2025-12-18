package com.java.beginnerLevel.array.mixed;

public class IMBD {
    public static void main(String[] args) {
        String actorName="SANDEEP";
        int yearBorn=2007;
        int ageOfActor=2023-yearBorn;

        String[] movieTitles={
                "THE SUN OF THRONE","TRUE COLOUR","THE SOUND OF MAGIC",
                "CRASH LANDING ON YOU","I AM NOT A ROBOT","THE DOOM AT YOUR SERVICE"
        };
        float[] movieRating={
          9.5F,7.5F,8.0F,
                9.0F,8.5F,7.0F
        };
        System.out.println("actor`s name: "+actorName);
        System.out.println("birth year"+yearBorn);
        System.out.println("age"+ageOfActor);

        System.out.println("movie:");

        for (int i = 0; i < movieRating.length; i++) {
            System.out.println(movieTitles[i]+"-"+getRating(movieRating[i]));

        }
    }
    static String getRating(float rating){
        if (rating<=7.0){
            return "bad";
        }else if (rating<=7.5){
            return "average";
        }else if (rating<=8.5){
            return "good";
        } else if (rating<=9.0) {
            return "very good";
        }else {
            return "amazing";
        }
    }
}
