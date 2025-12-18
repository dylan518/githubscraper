package com.unschedule_grooming;

public class rev_and_challengecode {
        public static void main(String[] args) {
            String s = "coderbyte";
            String challange="1esf0rzoa8";
            String ans = "";
            String rev = "";

            for (int index = s.length() - 1; index >= 0; index--) {
                rev = rev + s.charAt(index);
            }
            rev=rev+challange;
            System.out.println("Reverse + Challenging code: "+rev);
            char []ch = rev.toCharArray(); // all hello world rev string are converted into character
            int rep = 1; // whn this rep contains 4 then we shld place _ there.
            for (int index = 0; index<ch.length;index++,rep++){
                if(rep%4==0){
                    ch[index]='_';
                    ans = ans+ch[index];
                }
                else{
                    ans=ans+ch[index];
                }
            }
            System.out.println(ans);
        }

    }

