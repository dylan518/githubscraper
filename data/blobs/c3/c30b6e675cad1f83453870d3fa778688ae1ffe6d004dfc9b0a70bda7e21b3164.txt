import java.util.*;

public class Minefield {

	//point class to keep a block
	private static class Point {
		//coordinates
		protected int x;
		protected int y;
		//constructor
		Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	//method to find path
	public static void pathAlice(boolean [][] mat) {

		//to store the safety path for totoshka
		ArrayList<Point> path = new ArrayList<>();
		//to store the safety path for alice
		ArrayList<Point> path_alice = new ArrayList<>();
		boolean done = false;

		int n = mat.length;//#rows
		int m = mat[0].length;//#columns

		//for each column in the first row
		for(int col=0; col<m && !done; col++) {

			/*tries to find the entry point*/

			if(mat[0][col] == false) continue; //continue to check next block
			//entry block for totoshka
			int x = col;
			int y = 0;
			//alice not entered yet
			int aliceX = -2;
			int aliceY = -2;
			//mark entry block of totshka
			path.add(new Point(x,y));

			//runs until finds the safety path
			while(!done) {

				/*check every adjacent blocks'*/
				/*if it doesnt have a bomb and it is not the previous block they comes through*/
				/*then totshka move to that block*/
				/*alice moves to the previous block totoshka passed*/
				if(x+1<m && mat[y][x+1] && !(aliceY==y && aliceX==x+1)) {
					aliceY=y;
					aliceX=x;
					x++;
				} else if(x-1>=0 && mat[y][x-1] && !(aliceY==y && aliceX==x-1)) {
					aliceY=y;
					aliceX=x;
					x--;
				} else if(y+1<m && mat[y+1][x] && !(aliceY==y+1 && aliceX==x)) {
					aliceY=y;
					aliceX=x;
					y++;
				} else if(x-1>=0 && y+1<m && mat[y+1][x-1] && !(aliceY==y+1 && aliceX==x-1)) {
					aliceY=x;
					aliceY=y;
					x--;
					y++;
				} else if(x+1<n && y+1<m && mat[y+1][x+1] && !(aliceY==y+1 && aliceX==x+1)) {
					aliceX=x;
					aliceY=y;
					x++;
					y++;

				//if there is no block to move on (path comes to end)
				//go backward
				}else{

					//if no blocks in the path
					if(path.size()==0) break;

					//make block to false, to indicate path is over
					mat[y][x] = false;

					/*move alice and totoshka backward*/
					if(path_alice.size()==0){
						aliceX = -2;
						aliceY = -2;
					}else{
						aliceX = path_alice.get(path_alice.size()-1).x;
						aliceY = path_alice.get(path_alice.size()-1).y;
						path_alice.remove(path_alice.size()-1);
					}

					x = path.get(path.size()-1).x;
					y = path.get(path.size()-1).y;

					//remove that block from the path
					path.remove(path.size()-1);
					continue;
				}

				/*if successfully moved*/
				//add new blocks to paths
				path.add(new Point(x,y));
				path_alice.add(new Point(aliceX,aliceY));

				//if totoshko reach the other side, they are done
				if(y==n-1) done = true; 
			}
		}

		//print the totoshka's path
		for(Point p: path) {
			System.out.println(p.y + " "+ p.x);
		}


	}

	public static void main(String[] args) {

		//Testing
		boolean testMatrix[][] = {
			{true, false, false, true, false},
			{true, false, true, false, false},
			{true, false, false, true, false},
			{true, false, false, true, false},
			{false, false, true, false, false}
		};

		pathAlice(testMatrix);
	}

}