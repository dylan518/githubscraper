class Solution {
    public int[] minOperations(String boxes) {
        // int n=boxes.length();
        // int[] ans=new int[n];
        // for(int i=0;i<n;i++){
        //     int cnt=0;
        //     for(int j=0;j<n;j++){
        //         if(boxes.charAt(j)=='1'){
        //             cnt+=Math.abs(j-i);
        //         }
        //     }
        //     ans[i]=cnt;
        // }
        // return ans;

        int n=boxes.length();
        int ans[]=new int[n];
        int cumvalue=0;
        int cumsum=0;
        //ye to hmne left to right nikala hai par right to left bhi to check karna hai
        for(int i=0;i<n;i++){
            ans[i]=cumsum;
            cumvalue+=(boxes.charAt(i)=='0'?0:1);
            cumsum+=cumvalue;
        }

        cumsum=0;
        cumvalue=0;
        //right to left bhi cumm sum nikalenge
        for(int i=n-1;i>=0;i--){
            ans[i]+=cumsum;
            cumvalue+=(boxes.charAt(i)=='0'?0:1);
            cumsum+=cumvalue;
        }

        return ans;
    }
}