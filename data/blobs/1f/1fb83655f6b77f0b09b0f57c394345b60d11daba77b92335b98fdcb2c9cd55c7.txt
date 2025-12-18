package connect_hub.UserManagement;

import java.io.IOException;
import org.json.JSONArray;
import org.json.JSONObject;
import java.io.FileWriter;
import java.io.BufferedWriter;
import java.util.ArrayList;

public class LogOut extends UserDetails {

        private PutUsers putUsers = new PutUsers();

    public LogOut(String email) throws IOException {
        super(null, email, null, null, null, null,null,null);
    }

    public String checkLogOutCredentials(String email) throws IOException {
        ArrayList<UserDetails>usersArray = ReadUsers.readUsersFromFile("users.json");
        boolean userFound = false;

        for (int i = 0; i < usersArray.size(); i++) {
            UserDetails user = usersArray.get(i);
            String storedEmail = user.getEmail();

            if (email.equals(storedEmail)) {
   //             if (userJson.optString("status").equalsIgnoreCase("Online")) {
                   user.setStatus("Offline");
                    userFound = true;
                    break;
       //         } else {
        //            return "User already offline";
       //         }
            }
        }
        if (userFound) {
            putUsers.writeUserToJson(this);
            return "Logout successful"; 
        } else {
            return "invalidEmail";
        }
    }

    private void saveUsersToFile(JSONArray usersArray) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("users.json"))) {
            writer.write(usersArray.toString(4)); 
        }
    }
}
