package tylermaxwell;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/daikichi")
public class MainController {
	
	@RequestMapping("")
	public String index() {
		return "Welcome";
	}

	@RequestMapping("/today")
	public String today() {
		return "Today you will find luck in all your endeavors!";
	}
	
	@RequestMapping("/tomorrow")
	public String tomorrow() {
		return "Tomorrow, an opportunity will arise, so be sure to be open to new ideas!";
	}
	
	@RequestMapping("/travel/{location}")
	public String travel(@PathVariable("location") String location) {
		return String.format("Congratulations! You will soon travel to %s", location.toUpperCase());
	}
	
	@RequestMapping("/lotto/{number}")
	public String lotto(@PathVariable("number") Integer number) {
		String even = "You will take a grand journey in the near future, but be weary of tempting offers.";
		String odd = "You have enjoyed the fruits of your labor but now is a great time to spend time with family and friends.";
		return number % 2 == 0 ? even : odd ;
	}
}
