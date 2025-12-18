package s3;


import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;
import java.io.File;

public class S3ImageUploader {

    public static void main(String[] args) {
        // Replace these with your AWS credentials and S3 bucket information
        String accessKey = "AKIAYS2NVBL2UMNG0";//Add valid accesskey
        String secretKey = "FiA+TQLmH8ZUr9aLAedIu6H6REOQfYDbGJ";//Add valid secretkey
        String region = "ap-south-1";
        String bucketName = "linga-bucket-test";

        // Path to the image file you want to upload
        String filePath = "/Users/linga/Desktop/test-a.png";
        System.setProperty("aws.accessKeyId", accessKey);
        System.setProperty("aws.secretAccessKey", secretKey);

        // Initialize the S3 client
        S3Client s3 = S3Client.builder()
                .region(Region.of(region))
                .credentialsProvider(DefaultCredentialsProvider.create())
                .build();

        // Create a PutObjectRequest
        PutObjectRequest request = PutObjectRequest.builder()
                .bucket(bucketName)
                .key("test-a.png")  // The key is the name of the object in the bucket
                .build();

        // Upload the file
        s3.putObject(request, new File(filePath).toPath());

        // Print a success message
        System.out.println("Image uploaded successfully to S3 bucket: " + bucketName);
    }
}

