import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;

public class ExamImpl extends UnicastRemoteObject implements Exam {

  private static final long serialVersionUID = 1L;
  private String examId;
  private String exameName;
  private Map<String, Student> registeredStudents;

  protected ExamImpl(String examId, String examName) throws RemoteException {
    super();
    this.examId = examId;
    this.exameName = examName;
    this.registeredStudents = new HashMap<>();
  }

  @Override
  public String getExamId() throws RemoteException {
    return this.examId;
  }

  @Override
  public String getExameName() throws RemoteException {
    return this.exameName;
  }

  @Override
  public void register(Student student) throws RemoteException {
    this.registeredStudents.put(student.getIndexNumber(), student);
  }

  @Override
  public int getRegisteredStudentCount() throws RemoteException {
    return registeredStudents.size();
  }

}
