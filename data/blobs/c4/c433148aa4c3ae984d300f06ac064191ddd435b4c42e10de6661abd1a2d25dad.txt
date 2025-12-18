package SpringPractice.core.logger;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class LogService {

    private final Mylogger mylogger;

    public void logic(String id){
        mylogger.log("servide id = "+id);
    }
}
