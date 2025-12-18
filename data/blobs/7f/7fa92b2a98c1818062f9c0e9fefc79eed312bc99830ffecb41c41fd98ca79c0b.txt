package nesteArray;

public class Ex08 {
	
	static void show(int[][] arr) {
		for(int i = 0; i < arr.length; i++) {
			for(int j = 0; j < arr.length; j++) {
				System.out.printf("%2d ", arr[i][j]);
			}
			System.out.println();
		}
		System.out.println();
	}
	
	public static void main(String[] args) {
		
		int[][] arr = new int[5][5];
		int num;
		show(arr);
		
		num = 1;
		for(int i = 0; i < arr.length; i++) {
			for(int j = 0; j < arr.length; j++) {
				arr[i][j] = num++;
			}
		}
		show(arr);
		
		
		num = 1;
		for(int i = 0; i < arr.length; i++) {
			for(int j = 0; j < arr.length; j++) {
				arr[j][i] = num++; // 증가를 세로로하고 show메소드(함수)에 따라 가로로 출력
			}
		}
		show(arr);
		
		num = 1;
		for(int i = 0; i < arr.length; i++) {
			for(int j = 0; j < arr.length; j++) {
				if(i % 2 == 0) {
					arr[i][j] = num++;					
				}
				else {						// j : 0, 1, 2, 3, 4
					arr[i][4 - j] = num++;	// i : 4, 3, 2, 1, 0 
				}
			}
		}
		show(arr);
		
		num = 1;
		int x = 0,y = 0; // x: 가로  y: 세로
		for(int i = 0; i < arr.length; i++) { 		// 세로
 			for(int j = 0; j < arr.length; j++) {	// 가로
				 System.out.printf("%d, %d : %d\n", y, x, num++);
				 if( i % 2 == 0) y += 1;
				 else			 y -= 1;
			}
 			
		}
		y -=1;
		x += 1;
		
//		show(arr);
		
		// 직접 숫자를 증가하는게 아니라, 그 인덱스의 자리를 지정해주고 num++로 증가시켜서 모양을 만든다
		arr[0][0] = num++;	// x값이 짝수이면
		arr[1][0] = num++;	// y값은 0부터 1씩 증가하여 4까지
		arr[2][0] = num++;
		arr[3][0] = num++;
		arr[4][0] = num++;
		
		arr[4][1] = num++;	// x값이 홀수이면
		arr[3][1] = num++;	// y값은 4부터 1씩 감소하여 0까지
		arr[2][1] = num++;
		arr[1][1] = num++;
		arr[0][1] = num++;
		
		arr[0][2] = num++;	// for(int i = 0; i < 5; i++) { 0, 1, 2, 3, 4
		arr[1][2] = num++;	//	  for(int j = 0; j < 5; j++) { 0, 1, 2, 3, 4
		arr[2][2] = num++;	// i가 짝수이면 j를 그대로 0부터 4씩 4까지 증가
		arr[3][2] = num++;	// i가 홀수이면 j는 4부터 0까지 감소하는 형식이 되어야 한다
		arr[4][2] = num++;
		
		// 다시 초기화
		arr = new int[5][5];
		
		// i,j는 숫자에 관여하는게 아니라 index의 자리를 지정해 주는 것이다
		for(int i = 0; i < 5; i++) {
			for(int  j = 0; j < 5; j++) {
				if( i %  2 == 0) {
					arr[j][i] = num++;
				}
				else {
					arr[4 - j][i] = num++;
				}
			}
		}
		
		
		
		
	}
}
