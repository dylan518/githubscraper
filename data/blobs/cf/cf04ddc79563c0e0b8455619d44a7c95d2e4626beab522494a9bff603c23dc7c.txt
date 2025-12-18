package com.scaler.dsa.trees;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.TreeMap;

/*
Problem Description
Given a binary tree, return a 2-D array with vertical order traversal of it. 
Go through the example and image for more details.


NOTE: If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.

Problem Constraints
0 <= number of nodes <= 105
Input Format
First and only argument is a pointer to the root node of binary tree, A.

Output Format
Return a 2D array denoting the vertical order traversal of tree as shown.

Input 1:
      6
    /   \
   3     7
  / \     \
 2   5     9
Input 2:
      1
    /   \
   3     7
  /       \
 2         9

Output 1:
 [
    [2],
    [3],
    [6, 5],
    [7],
    [9]
 ]
Output 2:
 [
    [2],
    [3],
    [1],
    [7],
    [9]
 ]
Explanation 1:
 First row represent the vertical line 1 and so on.
 
Output of below will be:
Vertical order traversal is 
	4 
	2 
	1 5 6 
	3 8 
	7 
	9 
	
1. Need to create custom pair object to store the  TreeNode and the level
2. HashMap is used to store the nodes that are in the same vertical level, where key is the level and the value is a list of node values which are in the same level
3. A queue is used to store the nodes at the same horizontal level.
4. After hashMap is formed, we need to just iterate through the map and add values to a ArrayList<ArrayList<Integer>> and return
 */
public class V_VerticalPointsInBinaryTree {

	static class Pair {
		TreeNode t;
		int x;

		Pair(TreeNode t, int x) {
			this.t = t;
			this.x = x;
		}
	}

	static TreeNode root;

	public static void main(String[] args) {
		root = new TreeNode(1);
		root.left = new TreeNode(2);
		root.right = new TreeNode(3);
		root.left.left = new TreeNode(4);
		root.left.right = new TreeNode(5);
		root.right.left = new TreeNode(6);
		root.right.right = new TreeNode(7);
		root.right.left.right = new TreeNode(8);
		root.right.right.right = new TreeNode(9);

		System.out.println(verticalOrderTraversal(root));

		TreeMap<Integer, ArrayList<Integer>> hm = new TreeMap<>();
		verticalOrder(root, 0, hm);

		ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();

		for (Map.Entry<Integer, ArrayList<Integer>> entry : hm.entrySet())
			res.add(entry.getValue());

		System.out.println(res);

		// To print the tree in vertical order from right to left just needs to reverse the key and print
		// TreeMap<Integer, ArrayList<Integer>> hm = new TreeMap<>(Collections.reverseOrder());

	}

	private static void verticalOrder(TreeNode root, int dist, TreeMap<Integer, ArrayList<Integer>> hm) {
		if (root == null)
			return;

		if (hm.containsKey(dist)) {
			ArrayList<Integer> list = hm.get(dist);
			list.add(root.val);
			hm.put(dist, list);
		} else {
			ArrayList<Integer> newlist = new ArrayList<>();
			newlist.add(root.val);
			hm.put(dist, newlist);
		}
		verticalOrder(root.left, dist - 1, hm);
		verticalOrder(root.right, dist + 1, hm);

	}

	public static ArrayList<ArrayList<Integer>> verticalOrderTraversal(TreeNode root) {
		ArrayList<ArrayList<Integer>> ans = new ArrayList<ArrayList<Integer>>();

		ArrayList<Integer> ar = new ArrayList<Integer>();
		if (root == null) {
			return ans;
		}

		TreeMap<Integer, ArrayList<Integer>> tm = new TreeMap<>();
		Queue<Pair> q = new LinkedList<Pair>();
		q.add(new Pair(root, 0));

		while (!q.isEmpty()) {
			Pair p = q.poll();
			int v = p.t.val;
			int x = p.x;
			ar = new ArrayList<Integer>();
			if (tm.containsKey(x)) {
				ar = tm.get(x);
				ar.add(v);
			} else {
				ar.add(v);
			}

			tm.put(x, ar);
			if (p.t.left != null) {
				q.add(new Pair(p.t.left, x - 1));
			}
			if (p.t.right != null) {
				q.add(new Pair(p.t.right, x + 1));
			}
		}
		for (int x : tm.keySet()) {
			ArrayList<Integer> f = tm.get(x);
			ans.add(f);
		}
		return ans;
	}
}
