import java.util.ArrayList;
import java.util.List;
// User authentication class
public class UserAuthentication_37 {

	    private List<User_37> userList;

	    public UserAuthentication_37() {
	        userList = new ArrayList<>();
	        initializeUserList();
	    }

	    private void initializeUserList() {
	        // Create users here and add them to the userList
	    	User_37 user1 = new User_37("hilal", "1234");
	    	User_37 user2 = new User_37("arif", "abcd");

	        userList.add(user1);
	        userList.add(user2);
	    }

	    public boolean authenticate(String username, String password) {
	        for (User_37 user : userList) {
	            if (user.getUsername().equals(username) && user.getPassword().equals(password)) {
	                return true;
	            }
	        }
	        return false;
	    }
	}

