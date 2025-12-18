package com.light.code.leetcode.backtracking;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * @author light
 * @Description 分割回文串
 *
 * 给你一个字符串s,请你将 s分割成一些子串，使每个子串都是回文串 。返回 s 所有可能的分割方案。
 *
 * 回文串 是正着读和反着读都一样的字符串。
 * @create 2023-08-28 17:07
 */
public class PartitionTest {
	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		String s=input.nextLine();
		System.out.println(partition(s));
	}

	public static List<List<String>> res=new ArrayList<>();
	public static List<String> path=new ArrayList<>();

	public static List<List<String>> partition(String s) {
		backtracking(s,0);
		return  res;
	}

	private static void backtracking(String s, int startIndex) {
		//终止条件
		if(startIndex>=s.length()){
			//收获结果
			res.add(new ArrayList<>(path));
			return;
		}

		for (int i = startIndex; i <s.length() ; i++) {
			//判断是否回文，如果是，则加入到path中
			if(isPalindrome(s,startIndex,i)){
				String str=s.substring(startIndex,i+1);
				path.add(str);
			}else {
				continue;
			}
			backtracking(s,i+1);
			//回溯
			path.remove(path.size()-1);
		}
	}

	private static boolean isPalindrome(String s, int left, int right) {
		for (int i = left,j=right; i <j ; i++,j--) {
			if(s.charAt(i)!=s.charAt(j)){
				return false;
			}
		}
		return true;
	}
}
