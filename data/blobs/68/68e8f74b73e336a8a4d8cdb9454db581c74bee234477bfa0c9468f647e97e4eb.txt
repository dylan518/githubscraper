package projects.Personal.DataBreach.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import projects.Personal.DataBreach.exception.CredentialNotFound;
import projects.Personal.DataBreach.model.Credentials;
import projects.Personal.DataBreach.repo.CredentialRepo;

import javax.transaction.Transactional;
import java.util.List;


@Service
@Transactional
public class CredentialService {
    private final CredentialRepo credentialRepo;
    @Autowired
    public CredentialService(CredentialRepo credentialRepo) {
        this.credentialRepo = credentialRepo;
    }


    public Credentials saveCredential(Credentials credential) {
       return credentialRepo.save(credential);
    }

    public List<Credentials> getAllCredentials() {
        return credentialRepo.findAll();
    }

    public Credentials checkCredential(Credentials credential){

        RestTemplate restTemplate = new RestTemplate();
        String url = "https://api.pwnedpasswords.com/range/" + credential.getHashPrefix();
        String response = restTemplate.getForObject(url, String.class);
        if(response.contains(credential.getHashedPassword())){
            credential.setIsCompromised(true);
        }
        return credentialRepo.save(credential);
    }

    public Credentials findCredentialById(Long id){
        return credentialRepo.findCredentialById(id)
                .orElseThrow(() -> new CredentialNotFound("Credential by id " + id +" was not found!"));
    }

    public void deleteCredentialbyId(Long id){
        try{
        credentialRepo.deleteCredentialById(id);}
        catch (Exception e){
            System.out.println("Credential not found");
        }
    }


}
