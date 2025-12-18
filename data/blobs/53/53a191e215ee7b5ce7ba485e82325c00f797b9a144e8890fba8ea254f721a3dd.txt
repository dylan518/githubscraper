package geeksforgeeks.Medium_Level;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

// https://www.geeksforgeeks.org/problems/maximum-meetings-in-one-room/1
public class MaximumMeetingsInOneRoom {
    public static ArrayList<Integer> maxMeetings(int N, int[] S, int[] F) {
        // code here
        int[][] arr = new int[N][3];
        for(int i=0; i<N; i++){
            arr[i][0] = S[i];
            arr[i][1] = F[i];
            arr[i][2] = i+1;
        }

        Arrays.sort(arr,(a, b)->a[1]==b[1]?a[0]-b[0]:a[1]-b[1]);
        ArrayList<Integer> list = new ArrayList<>();
        int fin = -1;

        for(int i=0; i<N; i++){
            if(fin<arr[i][0]){
                fin = arr[i][1];
                list.add(arr[i][2]);
            }
        }

        Collections.sort(list);
        return list;
    }
}

/*
There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i]) where S[i] is the start time of meeting i and F[i] is the finish time of meeting i. The task is to find the maximum number of meetings that can be accommodated in the meeting room. You can accommodate a meeting if the start time of the meeting is strictly greater than the finish time of the previous meeting. Print all meeting numbers.

Note: If two meetings can be chosen for the same slot then choose meeting with smaller index in the given array.

Example 1:

Input:
N = 6
S = {1,3,0,5,8,5}
F = {2,4,6,7,9,9}
Output:
{1,2,4,5}
Explanation:
We can attend the 1st meeting from (1 to 2), then the 2nd meeting from (3 to 4), then the 4th meeting from (5 to 7), and the last meeting we can attend is the 5th from (8 to 9). It can be shown that this is the maximum number of meetings we can attend.
Example 2:

Input:
N = 1
S = {3}
F = {7}
Output:
{1}
Explanation:
Since there is only one meeting, we can attend the meeting.
Your Task:

You don't need to read input or print anything. Your task is to complete the function maxMeetings() which takes the arrays S, F, and its size N as inputs and returns the meeting numbers we can attend in sorted order.

Expected Time Complexity: O(N*log(N))
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 105
0 <= S[i] <= F[i] <= 109
Sum of N over all test cases doesn't exceeds 106
 */