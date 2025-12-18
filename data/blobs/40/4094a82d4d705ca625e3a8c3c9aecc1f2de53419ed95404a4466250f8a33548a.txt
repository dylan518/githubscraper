public class App {
    public static void main(String[] args) throws Exception {
        int ar[] = {805306368,805306368,805306368};
        int ar2[] = {2,2};
        int ar3[] = {3,6,7,11};
    
        App a = new App();
        System.out.println(3==a.minEatingSpeed(ar, 1000000000));
        System.out.println(2==a.minEatingSpeed(ar2, 2));
        System.out.println(4==a.minEatingSpeed(ar3, 8));
    }


        public int minEatingSpeed(int[] piles, int h) {
            int result = Integer.MAX_VALUE;
            int left = 1;
            int right = 1000000000; 
    
            while(left<=right){
                int middle = left + (right-left)/2;
    
                int subResult = checkEatingTime(piles, middle);
    
                if(subResult<0||subResult>h){
                    left = middle  + 1 ;

                }else if (subResult<=h) {
                    right = middle - 1;
                    result = Math.min(result, middle);
                }
            }
    
            return result;
        }
    
        public int checkEatingTime(int[] piles, int speed){
            int result = 0;
    
            for(int i = 0; i < piles.length; i++){
                if(piles[i]%speed==0){
                    result += piles[i]/speed;
                }else{
                    result += (piles[i]/speed)+1;
                }
            }
    
    
            
            return result;
        }
    }

