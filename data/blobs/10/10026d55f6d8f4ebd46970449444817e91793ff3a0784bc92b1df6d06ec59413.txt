class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> kidsWithExtra = new ArrayList<>();
        int maxCandies = 0;

        for (int candie : candies) {
            if (maxCandies < candie) {
                maxCandies = candie;
            }
        }

        for (int candie : candies) {
            if ((candie + extraCandies) >= maxCandies) {
                kidsWithExtra.add(true);
            } else {
                kidsWithExtra.add(false);
            }
        }

        return kidsWithExtra;
    }
}