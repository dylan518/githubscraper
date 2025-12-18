package FirstAPI.FirstAPI.firstAPI01;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

/* scrivi un'applicazione Spring Boot con le dipendenze necessarie che abbia:
a NameControllerdove si esegue la mappatura name per:
rispondere con il proprio nome a una GET richiesta
rispondi con il tuo nome invertito (es. da Johna nhoJ, usando StringBuilder) a una POST richiesta
testare l'endpoint API con Postman, eseguendo a GET e una POSTrichiesta
*/

@RestController
public class NameController {



    @GetMapping("/name")
    public String getName() {
        return "Stella";
    }

    @PostMapping("/name")
    public ResponseEntity<String> getInvertedName(@RequestParam String name) {
        StringBuilder invertedNameBuilder = new StringBuilder(name).reverse();
        String invertedName = invertedNameBuilder.toString();
        return new ResponseEntity<>(invertedName, HttpStatus.OK);
    }

}
