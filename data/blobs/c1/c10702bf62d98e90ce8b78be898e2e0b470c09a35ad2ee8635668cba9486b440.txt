import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

public class Base64Decoder {

    public static void main(String[] args) throws Exception {
        // Base64 encoded data to decrypt
        String encodedData = "YsOOZIwt7sk402QuoF4A9siwF43b78B4qBtuKR4v/VE=";

        // Base64 encoded secret key
        String encodedKey = "isutcsamuelisutc";

        // Decode the Base64 encoded data and key
        byte[] decodedData = Base64.getDecoder().decode(encodedData);
        byte[] decodedKey = encodedKey.getBytes("UTF-8");

        // Create a secret key from the decoded key
        SecretKeySpec secretKey = new SecretKeySpec(decodedKey, "AES");

        // Initialize the cipher for decryption
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher.init(Cipher.DECRYPT_MODE, secretKey);

        // Decrypt the data
        byte[] decryptedData = cipher.doFinal(decodedData);

        // Convert the decrypted data to a string
        String decryptedString = new String(decryptedData);

        // Print the decrypted string to the console
        System.out.println(decryptedString);
    }
}
