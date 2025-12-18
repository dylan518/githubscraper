package springboot.demo.myApp.iOCandDependencyInjection.constructorInjection;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import springboot.demo.myApp.iOCandDependencyInjection.components.Coach;

@RestController
public class DemoConstructorController {

    private Coach coach1;
    private Coach coach2;

    // if there is only one constructor , then @Autowired is not needed.
    @Autowired
    public DemoConstructorController(@Qualifier("cricketCoach") Coach coach1, @Qualifier("baseBallCoach") Coach coach2) {
        System.out.println("In constructor : " + getClass().getSimpleName());
        this.coach1 = coach1;
        this.coach2 = coach2;
    }

    @GetMapping("/constructor/dailyWorkout1")
    public String getDailyWorkout()
    {
        return "constructor : "+ coach1.getDailyWorkout();
    }

    @GetMapping("/constructor/dailyWorkout2")
    public String getDailyWorkout2()
    {
        return "constructor : "+ coach2.getDailyWorkout();
    }
}
