import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import javax.swing.*;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;

public class FileEncryptDecrypt {
    private static final String ALGORITHM = "AES";

    public static void main(String[] args) {
        try {
            // Select file using file chooser
            JFileChooser fileChooser = new JFileChooser();
            fileChooser.setDialogTitle("Select a file to encrypt/decrypt");
            int result = fileChooser.showOpenDialog(null);

            if (result != JFileChooser.APPROVE_OPTION) {
                System.out.println("No file selected");
                return;
            }

            File file = fileChooser.getSelectedFile();
            System.out.println("Selected file: " + file.getAbsolutePath());

            // Ask for password
            System.out.print("Enter password: ");
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            String password = reader.readLine();

            // Ask for operation (encrypt or decrypt)
            System.out.print("Enter 'e' to encrypt or 'd' to decrypt: ");
            String operation = reader.readLine();

            if (operation.equalsIgnoreCase("e")) {
                encryptFile(file, password);
                System.out.println("File encrypted successfully.");
            } else if (operation.equalsIgnoreCase("d")) {
                decryptFile(file, password);
                System.out.println("File decrypted successfully.");
            } else {
                System.out.println("Invalid operation.");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void encryptFile(File file, String password) throws Exception {
        SecretKey secretKey = generateKey(password);
        Cipher cipher = Cipher.getInstance(ALGORITHM);
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);

        byte[] inputBytes = Files.readAllBytes(file.toPath());
        byte[] outputBytes = cipher.doFinal(inputBytes);

        // Write encrypted file
        try (FileOutputStream outputStream = new FileOutputStream(file + ".enc")) {
            outputStream.write(outputBytes);
        }
    }

    private static void decryptFile(File file, String password) throws Exception {
        SecretKey secretKey = generateKey(password);
        Cipher cipher = Cipher.getInstance(ALGORITHM);
        cipher.init(Cipher.DECRYPT_MODE, secretKey);

        byte[] inputBytes = Files.readAllBytes(file.toPath());
        byte[] outputBytes = cipher.doFinal(inputBytes);

        // Write decrypted file
        String originalFileName = file.getName().replace(".enc", "");
        try (FileOutputStream outputStream = new FileOutputStream(originalFileName)) {
            outputStream.write(outputBytes);
        }
    }

    private static SecretKey generateKey(String password) throws NoSuchAlgorithmException {
        byte[] key = new byte[16]; // AES key size is 128 bits
        byte[] passwordBytes = password.getBytes();
        System.arraycopy(passwordBytes, 0, key, 0, Math.min(key.length, passwordBytes.length));
        return new SecretKeySpec(key, ALGORITHM);
    }
}
