
/**
 * Write a description of class Dropout here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Dropout extends Student
{// instance variables
    private int numOfRemainingModules;
    private int numOfMonthsAttended;
    private String dateOfDropout;
    private int remainingAmount;
    private boolean hasPaid;

    public Dropout(int enrollmentID,String dateOfBirth, String courseName, String studentName,String dateOfEnrollement,
    int courseDuration, int tuitionFee, int numOfRemainingModules, int numOfMonthsAttended,int reaminingAmount, String dateOfDropout )//initialize instance variableand from student class
    {    //used super keyword to call from student class in constructor
        super(dateOfBirth, studentName, courseDuration, tuitionFee);
        setEnrollmentID(enrollmentID); 
        setCourseName(courseName);
        setDateOfEnrollement(dateOfEnrollement);
        this.numOfRemainingModules=numOfRemainingModules;
        this.numOfMonthsAttended=numOfMonthsAttended;
        this.dateOfDropout=dateOfDropout;
        this.remainingAmount=0;
        this.hasPaid=false;
    }
    //accessor method
    public int getNumOfRemainingModules(){
        return numOfRemainingModules;
    }

    public int getNumOfMonthsAttended(){
        return numOfMonthsAttended;
    }

    public String getDateOfDropout(){
        return dateOfDropout;
    }

    public int getRemainingAmount(){
        return remainingAmount;
    }

    public boolean getHasPaid(){
        return hasPaid;
    }

    // creating billspayable method
    public void billsPayable(){
        remainingAmount=(super.getCourseDuration() -numOfMonthsAttended)*super.getTuitionFee();
        if(this.hasPaid=true){
        System.out.println("Bills has paid");}
    }
    // creating removestudent method
    public void removeStudent(){
        if (hasPaid==true){

            super.setEnrollmentID(0);
            super.setDateOfBirth("");
            super.setCourseName("");
            super.setStudentName("");
            super.setDateOfEnrollement("");
            super.setCourseDuration(0);
            super.setTuitionFee(0);

            this.numOfRemainingModules=0;
            this.numOfMonthsAttended=0;
            this.dateOfDropout="";
            this.remainingAmount=0;
            this.hasPaid=false;
        }else{
            System.out.println("All bills not cleared");
        }
    }

    public void display(){
        super.display();
        System.out.println("Number of remaining modules is : "+numOfRemainingModules);
        System.out.println("Total number of months attended is : "+numOfMonthsAttended);
        System.out.println("Date Of Dropout is : "+dateOfDropout);
        System.out.println("Remaining amount is : "+remainingAmount);
    }
}