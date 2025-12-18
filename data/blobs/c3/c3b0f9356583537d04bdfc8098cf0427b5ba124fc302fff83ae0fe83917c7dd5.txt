class Student
  {
    String name;
    int m,r;

Student()
{
}

Student(String n,int a,int b)
{
name=n;
m=a;
r=b;
}
void display()
{
  System.out.println(name);
  System.out.println(m);
  System.out.println(r);
}
}
class Copy
{
public static void main(String ...k)
{
 Student obj1=new Student("Gopal",78,56);
 Student obj2=new Student();
 Student obj3=new Student();
 
 obj2.name=obj1.name;
obj2.m=obj1.m;
obj2.r=obj1.r;

 obj3.name=obj2.name;
obj3.m=obj2.m;
obj3.r=obj2.r;

obj1.display();
obj2.display();
obj3.display();
}
}

