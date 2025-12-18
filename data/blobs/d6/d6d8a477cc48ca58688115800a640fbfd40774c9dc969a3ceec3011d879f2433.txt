package SectionA;

public class NonFiction extends Book implements Categorizeable{
    private String subject;

    public NonFiction(String title, String author, String ISBN, Status ava_status, String subject) {
        super(title, author, ISBN, ava_status);
        this.subject = subject;
    }

    public void showDetails() {
        System.out.println("Title:  \n"+getTitle()+"Author  "+getAuthor()+"ISBN" +getISBN()+"Status  "+ getAva_status());
    }

    public void displayCategoryDetails() {
        System.out.println("subject:  " + subject);
    }

    @Override
    public String toString() {
        return "NonFiction{" +
                "subject='" + subject + '\'' +
                '}';
    }
}
