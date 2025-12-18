package Workshop3;

public class Person
{
  private char gender;
  private Name name;
  private Job job;
  private Pet pet;

  //creating 3 args constructor
  public Person(char gender, Name name, Job job, Pet pet)
  {
    this.gender = gender;
    this.name = name.copy();
    this.job  = job.copy();
    this.pet = pet;
  }
  public Name getName()
  {
    return name.copy();
  }
  public String getFullName()
  {
    return name.getFullName();

  }
  public boolean isFemale()
  {
    if(gender == 'F' || gender == 'f')
    {
      return true;
    }
    else
    {
      return false;
    }
  }
  public boolean isMale()
  {
    if (gender == 'M' || gender == 'm')
    {
      return true;
    }
    else
    {
      return false;
    }
  }
  public String toString()
  {
    return "Gender: " + gender + " Name: " + name + " Job: " + job;
  }

  public boolean equals(Object obj)
  {
    if(!(obj instanceof Person))
    {
      return false;
    }

    Person other = (Person)obj;
    return gender == other.gender && name.equals(other.name) && job.equals(other.job);
  }
  //getPersonPosition method
  public String getPersonPosition()
  {
    return job.getPosition();
  }
  public String getPersonCompany()
  {
    return job.getCompany();
  }
  public double getSalary()
  {
    return job.getSalary();
  }
}
