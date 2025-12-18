package project5;

import java.util.Scanner;

public class FreeBooks {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

               /**
                 * Online Book Merchant offers premium customers 1 free book with every purchase of 5 or more books
                 * and offers 2 free books with every purchase of 8 or more books.
                 * It offers regular customers 1 free book with every purchase of 7 or more books
                 * and offers 2 free books with every purchase of 12 or more books.
                 *
                 * Write a program to calculate number of free books.
                 *
                 *  sample output:
                 * Are you a premium customer?
                 * true
                 * How many books for purchase?
                 * 9
                 * You qualify for 2 free books
                 *
                 */

                int freeBooks, numberOfBooksPurchased;
                boolean isPremiumCustomer;
                Scanner scanner = new Scanner(System.in);
              //  BookShop bookShop = new BookShop();


                System.out.println("Are you a premium customer? True/False");
                isPremiumCustomer = scanner.nextBoolean();

                System.out.println("How many books for purchase?");
                numberOfBooksPurchased = scanner.nextInt();

             //   freeBooks = bookShop.countFreeBooks(isPremiumCustomer, numberOfBooksPurchased);
              //  System.out.println("You qualify for " + freeBooks + " free books");
                //TODO write your code here
            }

            public int countFreeBooks(boolean isPremiumCustomer, int numberOfBooks) {
                int freeBooks;
                int numberOfBooksPurchased = 0;
                if (isPremiumCustomer = true) {
                    if (numberOfBooksPurchased >= 5 && numberOfBooksPurchased < 8) {
                        freeBooks = 1;
                    } else if (numberOfBooksPurchased > 8) {
                        freeBooks = 2;
                    } else {
                        freeBooks = 0;
                    }
                } else {
                    if (numberOfBooksPurchased >= 7 && numberOfBooksPurchased < 12) {
                        freeBooks = 1;
                    } else if (numberOfBooksPurchased >= 12) {
                        freeBooks = 2;
                    } else {
                        freeBooks = 0;
                    }
                }
                return freeBooks;
            }

        }



      //  System.out.println ("Are you a premium customer?");
     //   boolean isPremiumCustomer = sc.nextBoolean();
     //   System.out.println("How many books for purchase?");
     //   int numberOfBooksPurchased = sc.nextInt();
      //  int freeBooks = countFreeBooks (isPremiumCustomer, numberOfBooksPurchased);
      //  int BookShop = sc.nextInt();
//}

 //   public int countFreeBooks(boolean isPremiumCustomer, int numberOfBooks) {
   //     int freeBooks = 0;
        //TODO implement method
  //      if (isPremiumCustomer) {
   //         if (numberOfBooks >= 8) {
    //            freeBooks = 2;
     //           System.out.println("You qualify for " + freeBooks + "free books");
    //        } else if(numberOfBooks >=5) {
      //          freeBooks = 1;
     //           System.out.println("You get " + freeBooks + "free books" );
      //      }else{
      //          System.out.println("Invalid input");
     //       }
     //   }else {
       //     if(numberOfBooks>=12){
        //        freeBooks = 2;
         //       System.out.println("You qualify for " + freeBooks + "free books");
        //    }else if(numberOfBooks>=7){
        //        freeBooks = 2;
        //        System.out.println("You qualify for " + freeBooks + "free books");

         //   }
      //  }
    //    return freeBooks;
  //  }
//}
