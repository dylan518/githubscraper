package Graph;

import java.util.*;

/* LeetCode :- 621 https://leetcode.com/problems/task-scheduler/ */

/* Go for the brute force approach , Refer the DSA notes */

class task_scheduler
{

    public static int task_scheduler(char [] str , int n)
    {
        int tt = 0;

        // Creating the hashmap for the character to get the frequencies 
        HashMap<Character,Integer> hm = new HashMap<>();
        for(int i = 0 ; i < str.length ; i++)
        {
            hm.put(str[i],hm.getOrDefault(str[i],0)+1);
        }

        // Priority Queue to store that frequiences in the descending order
        PriorityQueue<Map.Entry<Character,Integer>> pq = new PriorityQueue<>((a,b) -> b.getValue() - a.getValue());

        for(Map.Entry<Character,Integer> entry : hm.entrySet())
        {
            pq.add(entry);
        }

        List<Map.Entry<Character,Integer>> temp = new ArrayList<>();
        while(!pq.isEmpty())
        {
            // pop the n element after firts poping , so pop n+1 times
            for(int i = 0 ; i < n+1 ; i++)
            {
                if(!pq.isEmpty())
                {
                    Map.Entry<Character,Integer> polled = pq.poll();
                    polled.setValue(polled.getValue()-1);
                    if(polled.getValue()>0)
                    {
                        temp.add(polled);
                    }
                }
                tt++;

                // if temp is empty it shows that there is no left over tasks to be completed 
                if(temp.isEmpty())
                {
                    break;
                }
            }
            while(!temp.isEmpty())
            {
                pq.add(temp.remove(0));
            }
        }

        return tt;
    }

    public static void main(String[] args) {
        char[] tasks = {'A','A','B','B','C','D'};
        int n = 1;        
        System.out.println(task_scheduler(tasks, n));
    }

}