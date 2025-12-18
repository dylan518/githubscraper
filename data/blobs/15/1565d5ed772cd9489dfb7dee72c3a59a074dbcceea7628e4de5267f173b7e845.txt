package GenericArray;

/**
 * @author wangzhen
 * @creatTime 2022/2/3 12:46 下午
 * @description 内部使用Object[]，只是转型位置变化，好处是不太可能忘记数组的运行时类型
 */
public class GenericArray2<T> {
    private Object[] array;
    public GenericArray2(int size) {
        array = new Object[size];
    }
    public void put(int index, T item) {
        array[index] = item;
    }
    @SuppressWarnings("unchecked")
    public T get(int index) {
        return (T)array[index];
    }
    @SuppressWarnings("unchecked")
    public T[] rep() {
        return (T[])array;
    }

    public static void main(String[] args) {
        GenericArray2<Integer> genericArray2 = new GenericArray2<Integer>(5);
        for (int i = 0; i < 5; i++) {
            genericArray2.put(i, i);
        }
        for (int i = 0; i < 5; i++) {
            System.out.println(genericArray2.get(i) + " ");
        }
        try {
            Integer[] integers = genericArray2.rep();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
