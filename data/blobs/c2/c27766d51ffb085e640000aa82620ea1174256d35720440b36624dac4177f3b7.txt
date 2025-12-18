package leetcode;

import java.util.*;

public class PushDominoes {
	 public String pushDominoes(String dominoes) {
		 	char[] input = dominoes.toCharArray();
		 	int left = 0; 
		 	for(int i = 1; i < input.length;i++) {
		 		if(i ==11 ) {
		 			i = 11;
		 		}
		 		if(input[i] == 'L') {
		 			if(input[left] == 'R') {
		 				int num = (i + 1-left)/2;
		 				for(int j = 0; j < num;j++) {
		 					input[left + j] = 'R';
		 				}
		 				
		 				for(int j = 0; j < num;j++) {
		 					input[i - j] = 'L';
		 				}			
			 		}
		 			else  {
		 				for(int j = 0; j < i - left+1;j++) {
		 					input[i - j] = 'L';
		 				}
                        
		 			}
		 			 left = i;
		 		}
		 		else if(input[i] == 'R') {  
		 			if(input[left] == 'R') {
		 				for(int j = left; j < i;j++) {
		 					input[j] = 'R';
		 				}
		 			}
		 			left = i;
		 		}	 			 		
		 	}
             
		 	if(input[left] == 'R') {
            
		 		for(int i = left; i < input.length;i++) {
		 			input[i] = 'R';
			 	}
		 	}
		 	System.out.print(new String(input));
		 	return new String(input);
	    }
		 	
	    public static void main(String[] args) {
	    	PushDominoes cd =new PushDominoes();
	    	cd.pushDominoes("RRRRRRL...");
	    }
}
