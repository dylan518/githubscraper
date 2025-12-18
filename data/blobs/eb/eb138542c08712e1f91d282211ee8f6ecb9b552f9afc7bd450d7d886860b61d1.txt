package work3;

//TASK 2

public class ArrayComparator {
    public static <T> boolean compareArr(T[] array1, T[] array2) {
        if (array1.length != array2.length) {
            return false;
        }

        for (int i = 0; i < array1.length; i++) {
            if (!array1[i].equals(array2[i])) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Integer[] intArr1 = {1, 2, 3};
        Integer[] intArr2 = {1, 2, 3};
        Integer[] intArr3 = {1, 2, 5};

        String[] strArr1 = {"синий", "красный", "зелёный"};
        String[] strArr2 = {"синий", "красный", "зелёный"};
        String[] strArr3 = {"синий", "красный", "розовый"};

        boolean intArrEqual = compareArr(intArr1, intArr2);
        boolean strArrEqual = compareArr(strArr1, strArr2);
        boolean intArrNot = compareArr(intArr1, intArr3);
        boolean strArrNot = compareArr(strArr1, strArr3);

        System.out.println("intArr1 и intArr2 равны: " + intArrEqual);
        System.out.println("intArr1 и intArr3 равны: " + intArrNot);
        System.out.println("strArr1 и strArr2 равны: " + strArrEqual);
        System.out.println("strArr1 и strArr3 равны: " + strArrNot);
    }
}
