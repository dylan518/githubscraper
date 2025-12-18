class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        int maxWidth = Integer.MIN_VALUE;
        int maxHeight = Integer.MIN_VALUE;
        for(int i = 0; i < sizes.length; i++) {
            if(sizes[i][0] < sizes[i][1]) {
                int tmp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = tmp;
            }
            
            maxWidth = Math.max(sizes[i][0], maxWidth);
            maxHeight = Math.max(sizes[i][1], maxHeight);
        }
        
        answer = maxWidth * maxHeight;
        
        return answer;
    }
}