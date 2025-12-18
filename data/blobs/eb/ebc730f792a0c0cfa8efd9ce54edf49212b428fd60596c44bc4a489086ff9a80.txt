package SummerHomework;

public class Demo28 {
    /*任务28：编写一个应用程序，计算并输出一维数组（9.8，12，45，67，23，1.98，2.55，45）中的最大值、最小值和平均值。*/
    public static void main(String[] args) {
        double[]arr={9.8,12,45,67,23,1.98,2.55,45};
        double max=arr[0];
        double min=arr[0];
        double sum = 0;
        for (int i = 0; i < arr.length; i++) {
           sum+=arr[i];
                if (arr[i]>max) {
                    max = arr[i];
                } if (arr[i]<min){
                    min=arr[i];
            }
        }
        System.out.println(max);
        System.out.println(min);
        System.out.println(sum/arr.length);
    }
}

