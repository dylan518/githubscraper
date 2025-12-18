public class SelectionSort {
    public static void main(String[] args) {
        int a[] = {11, 3, 1, 7, 5, 17, 2, 6};



        for (int i = 0; i <a.length-1; i++) {
            int minIndex = i;

            for (int j = i + 1; j < a.length; j++) {

                if (a[minIndex] > a[j]) {//11>3->3,11>1-1,

                    minIndex = j;//3,1

                }

            }
            int temp = 0;
            temp = a[i];
            a[i] = a[minIndex];
            a[minIndex] = temp;
        }
        for (int k = 0; k <= a.length-1; k++) {
            System.out.println(a[k]);
        }


    }
}