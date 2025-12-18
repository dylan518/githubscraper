import java.util.Scanner;
import java.util.Locale;

public class Pokerito {

  public static void main(String[] args) {
    
    Scanner scan = new Scanner(System.in).useLocale(Locale.ENGLISH);
    
    System.out.println("Let's play Pokerito. Type anything when you're ready.");
    String start = scan.nextLine();
    
    System.out.println("It's like Poker, but a lot simpler.");
    System.out.println("- There are two players, you and the computer.");
    System.out.println("- The dealer will give each player one card.");
    System.out.println("- Then, the dealer will draw five cards (the river)");
    System.out.println("- The player with the most river matches wins!");
    System.out.println("- If the matches are equal, everyone's a winner!");
    System.out.println("- Ready? Type yes if you are.");
    String start2 = scan.nextLine();

    if(start2.equals("yes")) {

      String userCard = RandomCard();
      String computerCard = RandomCard();

      System.out.println(" Here's your card:");
      System.out.println(userCard);
      // System.out.println("\n");
      System.out.println(" Here's the computer's card:");
      System.out.println(computerCard);
  
      int userScore = 0;
      int computerScore = 0;


      System.out.println("Now, the dealer will draw five cards. Press enter to continue.");
      for(int i = 1; i <= 5; i++) {
        String draw = RandomCard();
        System.out.print("Card " + i + "\n");
        System.out.print(draw);
        
        if(userCard.equals(draw)) {
          userScore++;
        }
        if(computerCard.equals(draw)) {
          computerScore++;
        }
  
      }
  
      System.out.println("Your number of match : " + userScore);
      System.out.println("Computer number of match : " + computerScore);
  
      if(userScore > computerScore) {
        System.out.println("You win !");
      } else if (userScore < computerScore) {
        System.out.println("The computer wins");
      } else {
        System.out.println("everyone wins !");
      }
      
    } else {
      System.exit(0);
    }
    
  }

  
  public static String RandomCard() {
    
    double randomNum = Math.random()*13;
    randomNum += 1;
    
    switch((int)randomNum) {
      case 1: return 
      "   _____\n"+
      "  |A _  |\n"+ 
      "  | ( ) |\n"+
      "  |(_'_)|\n"+
      "  |  |  |\n"+
      "  |____A|\n"
      ; 
      case 2:
      return
      "   _____\n"+              
      "  |2    |\n"+ 
      "  |  o  |\n"+
      "  |     |\n"+
      "  |  o  |\n"+
      "  |____2|\n"
      ;        
      case 3: 
      return
        "   _____\n" +
        "  |3    |\n"+
        "  | o o |\n"+
        "  |     |\n"+
        "  |  o  |\n"+
        "  |____3|\n"
      ; 
      case 4: 
      return
        "   _____\n" +
        "  |4    |\n"+
        "  | o o |\n"+
        "  |     |\n"+
        "  | o o |\n"+
        "  |____4|\n"
      ; 
      case 5: 
      return
        "   _____ \n" +
        "  |5    |\n" +
        "  | o o |\n" +
        "  |  o  |\n" +
        "  | o o |\n" +
        "  |____5|\n"
      ; 
      case 6: 
      return
        "   _____ \n" +
        "  |6    |\n" +
        "  | o o |\n" +
        "  | o o |\n" +
        "  | o o |\n" +
        "  |____6|\n"
      ; 
      case 7: 
      return
        "   _____ \n" +
        "  |7    |\n" +
        "  | o o |\n" +
        "  |o o o|\n" +
        "  | o o |\n" +
        "  |____7|\n"
      ; 
      case 8: 
      return
        "   _____ \n" +
        "  |8    |\n" +
        "  |o o o|\n" +
        "  | o o |\n" +
        "  |o o o|\n" +
        "  |____8|\n"
      ; 
      case 9:
      return
        "   _____ \n" +
        "  |9    |\n" +
        "  |o o o|\n" +
        "  |o o o|\n" +
        "  |o o o|\n" +
        "  |____9|\n"
      ; 
      case 10: 
      return
        "   _____ \n" +
        "  |10  o|\n" +
        "  |o o o|\n" +
        "  |o o o|\n" +
        "  |o o o|\n" +
        "  |___10|\n"
      ; 
      case 11: 
      return
        "   _____\n" +
        "  |J  ww|\n"+ 
        "  | o {)|\n"+ 
        "  |o o% |\n"+ 
        "  | | % |\n"+ 
        "  |__%%[|\n"
      ; 
      case 12:
      return
        "   _____\n" +
        "  |Q  ww|\n"+ 
        "  | o {(|\n"+ 
        "  |o o%%|\n"+ 
        "  | |%%%|\n"+ 
        "  |_%%%O|\n"
      ; 
      case 13:
      return 
      "   _____\n" +
      "  |K  WW|\n"+ 
      "  | o {)|\n"+ 
      "  |o o%%|\n"+ 
      "  | |%%%|\n"+ 
      "  |_%%%>|\n";
      default: return "This does not get called";   
    }
    
  }

}