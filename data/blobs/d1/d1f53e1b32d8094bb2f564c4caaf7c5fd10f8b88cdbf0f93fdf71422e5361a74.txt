import java.util.*;
import java.util.function.BinaryOperator;
import java.util.function.Function;
import java.util.stream.Collectors;

public class ArrayQuestion {

    public static void main(String[] args) {
        System.out.println(findPairsWithZeroSum(new int[]{4, -3, 5, 1, -4, -1, 3, 2, -2}));
        List<Employee> employees = new ArrayList<>();
        employees.add(new Employee("Alice", "HR", 70000.00));
        employees.add(new Employee("Bob", "Engineering", 85000.00));
        employees.add(new Employee("Charlie", "Engineering", 120000.00));
        employees.add(new Employee("Darren", "HR", 60000.00));
        System.out.println(findHighestPaidEmployeePerDept(employees));
    }

    static List<List<Integer>> findPairsWithZeroSum(int[] arr) {
        Set<Integer> seen = new HashSet<>();
        List<List<Integer>> pairs = new ArrayList<>();
        for (int a : arr) {
            int target = -a;
            if (seen.contains(target)) {
                pairs.add(List.of(a, target));
            }
            seen.add(a);
        }
        return pairs;
    }

    static Map<String, Employee> findHighestPaidEmployeePerDept(List<Employee> employees) {
        return employees.stream().collect(Collectors.toMap(
                e -> e.department, Function.identity(),
                BinaryOperator.maxBy(Comparator.comparing(e -> e.salary))));
    }

}
