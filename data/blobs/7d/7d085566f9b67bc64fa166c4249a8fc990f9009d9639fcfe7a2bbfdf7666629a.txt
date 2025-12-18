package manage;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class List_User {
	UserDoc userdoc;
	
	
	public List_User() {
		userdoc=new UserDoc();
	}
	
	 public ArrayList<User> getAllUser(){
		 return userdoc.getAllUser();
	 }
	 //trả về index của người đăng nhập
	 public int indexUser(String nameLogin,String passLogin){
		 ArrayList<User> lst=getAllUser();
		 for(User user:lst)
			 if(user.getNameLogin().equals(nameLogin))
				 if(user.getPassLogin().equals(passLogin))
					 return lst.indexOf(user);
		 return -1;
	}
	 //thêm người dùng
	 public void addUser(User user){
		 userdoc.addUser(user);
	 }
	 //sửa thông tin người dùng
	 public void updateUser(User user) {
		userdoc.updateUser(user);
	}
	 
	 //kiểm tra số điện thoại đủ 10 chữ số hay không và phải có số 0 ở đầu
	 public boolean isNumeric(String str) { 
	        try {
	            if(str.length()!=10 || str.charAt(0)!='0'){
	                return false;
	            }  
	            Double.parseDouble(str);  
	            return true;
	        }catch(NumberFormatException e){  
	            System.out.println("fall in love");
	            return false;  
	        }  
	    }
	 //kiểm tra số điện thoại đã được đăng kí chưa
	 public boolean isExistPhoneNumber(String str) {
		for(User user: userdoc.getAllUser()){
			if(user.getPhonenumber().equals(str))
				return true;
		}
		return false;
	}
	//kiểm tra tên đăng nhập đã được đăng kí chưa
	 public boolean isExistNameLogin(String str) {
		 for(User user: userdoc.getAllUser()){
				if(user.getNameLogin().equals(str))
					return true;
		 }
		 return false;
	}
	

}
