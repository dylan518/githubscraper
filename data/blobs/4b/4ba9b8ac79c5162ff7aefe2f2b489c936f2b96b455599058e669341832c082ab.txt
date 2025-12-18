package class6.wildcardgeneric;

import class6.generic.DataType;

public class WildCardGenericDataTypeMainTest {
    public static void main(String[] args) {
        DataType<Integer> integerDataType = new DataType<>(10);
        System.out.println("Integer Value : "+integerDataType.getDatatype());

        DataType<String> stringDataType = new DataType<>("Ban");
        System.out.println(stringDataType.getDatatype());
    }
}
