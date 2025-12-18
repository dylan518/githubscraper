public class Fantastic extends Movies{

    private String genre;
    private String achievements;


    public Fantastic(String name, String genre, String achievements) {
        super(name);
        this.genre = genre;
        this.achievements = achievements;
    }

    @Override
    public void print() {
        System.out.println(" Жанр фантастики: " + genre +
                "\n Достижения фильма " + achievements);

    }
}
