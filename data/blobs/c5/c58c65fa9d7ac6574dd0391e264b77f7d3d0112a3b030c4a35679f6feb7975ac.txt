class Solution {
    public int getArea(int height,int breadth){
        return (height*breadth);
    }
    public int maxArea(int[] height) {
        int low=0,high=height.length-1;
        int maxArea=Integer.MIN_VALUE;
        
        while(low<high){
            //calculate the area 
            int area=getArea(Math.min(height[low],height[high]),high-low);
            maxArea=Math.max(area,maxArea);
            
            //now move pointer to try and find a larger area
            if(height[low]<=height[high]){
                low++;
            }
            else{
                high--;
            }
            
        }
        return maxArea;
    }
}