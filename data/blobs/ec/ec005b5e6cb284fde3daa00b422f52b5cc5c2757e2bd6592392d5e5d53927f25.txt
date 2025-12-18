import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Duplicate {
    public static void main(String[] args) {
        Duplicate obj = new Duplicate();
        int arr[] = {1,1,2,2,3,3,4,4,4,4,5};
        int n = arr.length;
        String ans = obj.result("My Name is      mayur");
        System.out.println(ans);
    }
    // public void duplicateRemove(int arr[],int n){
        //Brute force apporach
        // Set  <Integer> st = new HashSet<>();
        // for(int i = 0;i<n;i++){
        //     st.add(arr[i]);
        // }
        // int index = 0;
        // for(Integer ele:st){
        //     arr[index] = ele;
        //     index++;
        // }

        //optimised using 2 pointers 

        // for(int i = 0,j = 1;j<n;j++){
        //     if(arr[j]!=arr[i]){
        //         arr[i+1] = arr[j];
        //         i++;
        //     }
        // }
        // for(int e: arr){
        //     System.out.print(e);
        // }


        String result(String str){
            String res = "";
            StringTokenizer tokenizer = new StringTokenizer(str," ");
            int strCount = tokenizer.countTokens();
            String []stringArray = new String[strCount];
            for(int i = 0;i<strCount;i++){
                stringArray[i] = tokenizer.nextToken();
                System.out.println(stringArray[i]);
                // res = res + tokenizer.nextToken()+ " ";
                // System.out.println(res);
            }
            for(int i = stringArray.length-1;i>=0;i--){
                res = res + stringArray[i]+" ";
            }



            return res;
        }
        
    }

