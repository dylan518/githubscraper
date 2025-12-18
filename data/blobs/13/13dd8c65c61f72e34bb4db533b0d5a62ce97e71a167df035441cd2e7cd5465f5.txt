
public class FreePractice36 {
	public static void main(String[] args) {
		int bigNum = -2147483647;
		int minNum = 2147483647;
		for(int i = 0; i < 10; i++ ) {
			int num = Integer.parseInt(args[i]);
			if( num > bigNum) {
				bigNum = num;
				if ( num < minNum) {
					minNum = num;
				}
			}else if( num < minNum) {
				minNum = num;
			}
		}
		
		System.out.println(args.length + "回入力されたの数字の内最大の値は" + bigNum + "です。");
		System.out.println(args.length + "回入力されたの数字の内最小の値は" + minNum + "です。");
	}

}
