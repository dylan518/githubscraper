import java.util.*;

public class beekeeper {

    private static boolean isVowel(char c){
        if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u' || c=='y')
            return true;
        return false;
    }

    private static void algo(ArrayList<String> list){
        HashMap<Integer, String> map = new HashMap<>();
        for(String str:list){
            int count = 0;
            for(int i=1;i<str.length();i++){
                if(isVowel(str.charAt(i)) && isVowel(str.charAt(i-1)) && str.charAt(i)==str.charAt(i-1)){
                    count++;
                }
            }
            map.put(count,str);
        }
        String ret = "";
        int min = 9999;
        for(int x:map.keySet()){
            if(x<min)
                ret = map.get(x);
        }
        System.out.println(ret);
    }
    
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextLine()){
            int x = Integer.parseInt(sc.nextLine());
            ArrayList<String> list = new ArrayList<>();
            for(int i=0;i<x;i++){
                list.add(sc.nextLine());
            }
            algo(list);
        }
        sc.close();
    }
}