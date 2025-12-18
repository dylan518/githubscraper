package rental;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Map<String,String> userCredentials=new HashMap<>();
		Scanner sc=new Scanner(System.in);
		userCredentials.put("Admin","Admin123");
		System.out.println("Enter the username");
		String userName=sc.next();
		System.out.println("Enter the password");
		String passWord=sc.next();
		
		
		if (userCredentials.containsKey(userName)&& userCredentials.get(userName).equals(passWord)) {
			List<Camera> cameraList = new ArrayList<>();
			Wallet account=new Wallet();
			
			startOver(cameraList,account);
			}
		else {
			System.out.println("Enter Valid User Details");
		}
		
	}
	public static void startOver(List<Camera> inputCameraList,Wallet inputAccount) {
		Scanner sc=new Scanner(System.in);
		List <Camera> cameraList=new ArrayList<Camera>();
		Wallet account=new Wallet();
		if(inputCameraList.size()!=0) {
			cameraList = inputCameraList;
		}else {
			Camera details=new Camera(1,"Canon","1200D",150.0,"Available");
			cameraList.add(details);
			details=new Camera(2,"Canon","1300D",180.0,"Available");
			cameraList.add(details);
			details=new Camera(3,"Samsung","DS123",100.0,"Available");
			cameraList.add(details);
			details=new Camera(4,"Sony","Dos",150.0,"Available");
			cameraList.add(details);
			details=new Camera(5,"LG","10D",280.0,"Available");
			cameraList.add(details);
			details=new Camera(6,"Nikon","Dslr25",280.0,"Available");
			cameraList.add(details);
		}
		if(inputAccount.getWalletamt()!=0) {
			account=inputAccount;
		}else {
			account.setWalletamt(10000);
		}
		
		
		System.out.println(" 1.MY CAMERA\n 2.RENT A CAMERA \n 3.VIEW ALL CAMERAS \n 4.MY WALLET \n 5.EXIT\n");
		int options=sc.nextInt();
		switch(options){
		case 1:
			optionOne(cameraList,account);
			break;
		case 2:
			RentCamera rent=new RentCamera();
			rent.DisplayALLCameras(cameraList,account);
			break;
		case 3:
			View display=new View();
			display.viewAllCameras(cameraList);
			startOver(cameraList,account);
		case 4:
			WalletOperations walletOperations=new WalletOperations();
			walletOperations.operations(account,cameraList);
			startOver(cameraList,account);
			break;
		case 5:
			System.out.println("THANKS FOR VISITING PLEASE COME AGAIN");
			break;
		}
		
	
	}
	public static void optionOne(List<Camera> cameraList,Wallet account) {
		Scanner sc=new Scanner(System.in);
		System.out.println(" 1.ADD\n 2.REMOVE\n 3.VIEW MY CAMERAS\n 4.GO TO PREVIOUS MENU");
		int Moptions=sc.nextInt();
		MyCamera operations=new MyCamera();
		switch(Moptions) {
		case 1:
			operations.addCamera(cameraList);
			break;
		case 2:
			operations.removeCamera(cameraList);
			break;
		case 3:
			operations.viewAllCameras(cameraList);
			break;
		case 4:
			startOver(cameraList,account);
		}
		System.out.println("1.Goto Main Menu\n2.Goto Previous Menu");
		int menuIndicator=sc.nextInt();
		if(menuIndicator==1) {
			startOver(cameraList,account);
		}
		else {
			optionOne(cameraList,account);
		}
	}

}
