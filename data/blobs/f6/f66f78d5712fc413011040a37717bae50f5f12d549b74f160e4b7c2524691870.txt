class Solution {
    public List<Integer> findDuplicates(int[] arr) {
        int i=0;
        while(i<arr.length)
        {
            int correct=arr[i]-1;
            if(arr[i]!=arr[correct])
            {
                swap(arr,i,correct);
            }
            else{
                i++;
            }


        }
        List <Integer> ans=new ArrayList<Integer>();
        for(int j=0;j<arr.length;j++)
        {
            if(arr[j]!=j+1)
            {
                ans.add(arr[j]);
            }
        }
        return ans;
    }
    void swap(int arr[],int i,int j)
    {
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;        
    }
}
