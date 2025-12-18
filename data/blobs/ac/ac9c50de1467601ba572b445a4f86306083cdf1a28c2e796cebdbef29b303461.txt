package days10;

import java.io.IOException;
import java.util.Arrays;
import java.util.Iterator;
import java.util.Scanner;

/**
 * @author JUNYONG_HOME
 * @date 2024. 7. 14. - 오후 4:06:18
 * @subject
 * @content1. 
 * 
 * 버블정렬하는 메서드 선언 ( bubbleSort ) 
 * (조건: 내림차순 정렬(desc) )
2. 이진 검색하는 메서드 선언 ( binarySearch )
3. int [] m = { ... }
   0의 갯수
   1의 갯수
   :
   9의 갯수
   출력
4. 30명 3반 학생의 이름,국,영,수,총,평,등,전교등수를 입력 및 출력하는 코딩.
5. int [] m = {1,2,3}
   정수 4를 m 배열에 추가하는 코딩을 하세요.
 */

public class Test2 {
	static String [][] names =new String[3][3];
	static int [][] kors = new int[3][3];
	static int [][] engs = new int[3][3];
	static int [][] mats = new int[3][3];
	static int [][] tots = new int[3][3];
	static int [][] ranks = new int[3][3];
	static int [] ranksAll = new int[9];
	static double [][] avgs = new double[3][3];
	static String name;
	static int kor,eng,mat,tot,countBan = 0,countMem=0;
	static double avg;
	static char con = 'y';
	static Scanner sc = new Scanner(System.in);
	static double [] avgAll = new double [9];

	public static void main(String[] args) throws IOException {

		int [] bub = {3,5,6,2,8,0,9,10,1}; //버블 정렬로 내림차순으로 배열해보자 (큰놈 왼쪽으로) 요소:9개
		bubbleSort(bub);


		//이진검색(반으로 쪼개면서 검색 - 검색대상 안나오면 top, bottom값을 조정하여 범위를 좁힘, 정렬되어 있어야함)
		int [] binary = {1,2,3,6,10,40,45,57,88,90,103,203,206,490}; 
		System.out.println(Arrays.toString(binary));
		System.out.println("찾고싶은 값 ? ");
		int search = sc.nextInt();

		if (binarySearch(binary,search) != -1) {
			System.out.printf("인덱스 %d에 있습니다\n",binarySearch(binary,search));
		}else if (binarySearch(binary,search) ==-1) {
			System.out.println("없습니다");
		}


		//각 숫자의 갯수
		int [] nums = {0,0,0,0,0,1,1,2,2,2,3,5,5,5,5,5,5,5};
		numsCount(nums);

		//5. int [] m = {1,2,3}
		//   정수 4를 m 배열에 추가하는 코딩을 하세요.
		int [] m = {1,2,3};
		int [] temp = new int[4];
		for (int i = 0; i < m.length; i++) {
			temp[i] = m[i]; 
		}
		temp[3] = 4;
		m = temp;
		System.out.println();
		System.out.println(Arrays.toString(m));


		//30명 3반 학생의 이름,국,영,수,총,평,등,전교등수를 입력 및 출력하는 코딩.
		studentInput();
		studentOutput(names,kors,engs,mats,tots,avgs,ranks,ranksAll);



	}//main

	private static void studentOutput(String[][] names, int[][] kors, int[][] engs, int[][] mats, int[][] tots,
			double[][] avgs, int[][] ranks, int[] ranksAll) {
		int k =0;
		for (int i = 0; i < 3; i++) {//반 순회
			for (int j = 0 ; j < 3; j++) {
				System.out.printf("%d반 %d번 : %s 국어:%d 영어:%d 수학:%d 총점:%d 평균:%.2f  반에서 %d등 전교%d등\n",
						i+1,j+1,names[i][j],kors[i][j],engs[i][j],mats[i][j],tots[i][j],avgs[i][j],ranks[i][j],ranksAll[k]);
				k++;
			}//for j
		}

	}

	private static void studentInput() throws IOException {


		do {
			System.out.printf("\n%d반 %d번 학생 이름, 국어, 영어, 수학 입력 ? ",countBan+1,countMem+1);
			names[countBan][countMem] =sc.next();
			kors[countBan][countMem] = sc.nextInt();
			engs[countBan][countMem] = sc.nextInt();
			mats[countBan][countMem] = sc.nextInt();
			tots[countBan][countMem] =kors[countBan][countMem] + engs[countBan][countMem] + mats[countBan][countMem] ;
			avgs[countBan][countMem] = tots[countBan][countMem]/3;
			ranks[countBan][countMem] = 1;

			if (countMem ==2) {
				countMem=0;
				countBan++;
			} else countMem++;

			System.out.println("계속 입력 ? (Y/N) ");
			con = (char) System.in.read();
			System.in.skip(System.in.available());

		} while (Character.toUpperCase(con)=='Y');

		rankProcess(avgs,ranks);
		rankProcessAll(avgs,ranks,avgAll,ranksAll);



	}

	private static void rankProcessAll(double[][] avgs, int[][] ranks, double[] avgAll, int[]ranksAll) {
		
		int k = 0; // 1차원 배열의 인덱스
		for (int i = 0; i < 3; i++) {// 평균값을 1차원 배열에 순서대로 넣기
			for (int j = 0; j < 3; j++) {
				avgAll[k] = avgs[i][j];
				k++;
			}
		}//for i
		
		for (int i = 0; i < ranksAll.length; i++) {//모든 전교 랭킹 1등으로 초기화
			ranksAll[i] =1;
		}
		
		for (int i = 0; i < ranksAll.length; i++) { //등수 정하려는애 고름
			for (int j = 0; j < ranksAll.length; j++) {//비교해서 등수 정하기
				if (avgAll[i] < avgAll[j]) {
					ranksAll[i] ++;
				}
			}
		}
		
	
//		Arrays.sort(avgAll);//맨 뒤가 랭킹 1등
//		System.out.println(Arrays.toString(avgAll));
//		
		
		
		


	}

	private static void rankProcess(double[][] avgs, int[][] ranks) {
		for (int i = 0; i < 3; i++) {//반 별로 순회하기
			for (int j = 0; j < 3; j++) { //등수 매길 아이 선정
				for (int j2 = j+1; j2 <3; j2++) {
					if (avgs[i][j] < avgs[i][j2]) {
						ranks[i][j]++;
					}
				}//forj2
			}//for j
		}//for i

	}

	private static void numsCount(int[] nums) {
		int [] count = new int [6];
		for (int i = 0; i < nums.length; i++) {
			count[nums[i]]++;
		}//for i
		for (int i = 0; i < count.length; i++) {
			System.out.printf("%d: %d개 ",i,count[i] );
		}

	}

	private static int binarySearch(int[] binary, int search) {
		//		int index = -1; //찾는 값 인덱스 , 검색 실패시 -1(인덱스로는 불가능한 수) 반환 위해 -1설정
		int top = binary.length-1; //마지막 인덱스
		int bot = 0; //첫 인덱스값
		int mid;
		while (top>=bot) {
			mid = (top+bot)/2;
			if (binary[mid]==search) return mid;
			else if (binary[mid] < search) bot =mid + 1;
			else if (binary[mid] > search) top =mid - 1;
		}

		return -1;	

	}

	private static void bubbleSort(int[] bub) {
		int temp =0;
		for (int i = 0; i < 9; i++) { //회차 
			for (int j = 0; j <= 7-i; j++) {// i=0일때 j(하나씩 비교)=8번 (0~7=8)
				if (bub[j+1] > bub[j]) { //j+1에 들어있는게 더 크다면 왼쪽으로 보냄
					temp = bub[j+1];
					bub[j+1] =bub[j]; //인덱스 번호 높은데 낮은 값 받음 (내림차순)
					bub[j] = temp;
				}//if
			}//for j
		}//for i 
		System.out.println(Arrays.toString(bub));

	}

}//class
