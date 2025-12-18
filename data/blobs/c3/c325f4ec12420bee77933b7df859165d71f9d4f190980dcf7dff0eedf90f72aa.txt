public class PersonFactory implements StudentAbstractFactory
{
  private String firstname;
  private String lastname;
  private int age;
  private String course;

  public PersonFactory(String firstname, String lastname,int age, String course)
  {
  this.firstname=firstname;
  this.lastname=lastname;
  this.age=age;
  this.course=course;
  }

   public Student createStudent()
   {
    return new Person(firstname,lastname,age,course);
   }
}