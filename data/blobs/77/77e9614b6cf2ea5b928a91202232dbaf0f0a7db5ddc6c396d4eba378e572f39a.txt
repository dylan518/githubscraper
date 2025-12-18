public class AdventDay {
    private int[] winningNums;
    private int[] scratchNums;
    private int pointsPerLine;
    private int totalPoints;

    AdventDay(int[] list1, int[] list2){
        winningNums = list1;
        scratchNums = list2;
        pointsPerLine = 0;
        totalPoints = 0;
    }

    public int pointWorth(){
        for (int number : scratchNums){
            for (int winning : winningNums){
                if (number == winning && pointsPerLine == 0) {
                    pointsPerLine = 1;
                } else if (number == winning){
                    pointsPerLine *= 2;
                }
            }
            totalPoints += pointsPerLine;
            pointsPerLine = 0;
        }

        return totalPoints;
    }
}
