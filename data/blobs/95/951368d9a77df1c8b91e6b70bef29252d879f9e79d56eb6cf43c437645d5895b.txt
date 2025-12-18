public  class Person {
    private int age;
    private String name;



    public Person(int age,String name){
      this.age=age;
      this.name=name;
  }


  public synchronized void incrementAge(){
      age++;
      System.out.println(age);
  }


  public String toString(){
      return "age="+age;
  }



}
