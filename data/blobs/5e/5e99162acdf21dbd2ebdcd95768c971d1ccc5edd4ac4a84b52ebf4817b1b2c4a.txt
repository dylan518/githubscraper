public class Book {
 
    private String title;
    private int ageRecommendation;
 
    public Book(String title, int ageRecommendation) {
        this.title = title;
        this.ageRecommendation = ageRecommendation;
    }
 
    public String getTitle() {
        return title;
    }
 
    public int getAgeRecommendation() {
        return ageRecommendation;
    }
 
    @Override
    public String toString() {
        return this.getTitle() + " (recommended for " + this.getAgeRecommendation() + " year-olds or older)";
    }
}
