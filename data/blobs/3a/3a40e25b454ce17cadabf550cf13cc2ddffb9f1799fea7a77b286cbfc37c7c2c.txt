//Maximum product subset of an array
    public long findMaxProduct(List<Integer> arr) {
       long product=1;
    int zero=0;
    int neg=0;
    long negMax=Long.MIN_VALUE;
    int MOD = 1000000007;
    if(arr.size()==1){
        return arr.get(0);
    }
    
    for(int i=0;i<arr.size();i++)
    {
        if(arr.get(i)==0)
        {
            zero++;
            continue;
        }
        
        product=(product*arr.get(i))%MOD;
        if(arr.get(i)<0)
        {
            neg++;
            negMax=Math.max(negMax,arr.get(i));
        }
    }
   if(zero==arr.size())
   {
       return 0;
   }
      if(neg%2==1)
      {
        if(neg==1 && zero>0 && zero+neg==arr.size())
        {
        return 0;
        }
    
       product=product/negMax;
   }
 return product;
    }
