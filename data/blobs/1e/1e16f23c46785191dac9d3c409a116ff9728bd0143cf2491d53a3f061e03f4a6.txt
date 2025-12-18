package Controller;
import Model.FilmList;
import Model.User;

public class UserController {
	User user;
	FilmListController filmListController;
	
	public UserController(String userName, String filmListName) {
		this.user = new User(userName);
        this.filmListController = new FilmListController(filmListName);
	}

    public void createFilmList(String NameOfList) {
    	FilmList newFilmList = new FilmList(NameOfList);
    	user.getFilmLists().add(newFilmList);
    }
    
	public void removeFilmList(String NameOfList) {	
		int index = 0;
    	
    	for (FilmList filmList : user.getFilmLists()) {
    		if(filmList.getNameOfList().equalsIgnoreCase(NameOfList)) {
    			break;
    		}else {
    			if(user.getFilmLists().size() < index) {
    				break;
    			}else {
    	    		index++;
    			}
    		}
    	}
    	user.getFilmLists().remove(index);
    }
}
