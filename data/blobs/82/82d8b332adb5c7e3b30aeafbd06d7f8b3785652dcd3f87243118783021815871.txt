import java.util.*;

public class Main {
    public static void main(String[] args) {
//        Set<Integer> set = new HashSet<>();              //1
//        Set<Integer> linked = new LinkedHashSet<>();    //2
//        Set<Integer>  integers =  new TreeSet<>();      //3
//

//        Set<Integer> set = new HashSet<>();
//        for (int i = 0; i < 100; i++) {
//            set.add(i);
//        }
//        for (Integer integer : set) {                   //foreach мн чыгаруу
//            if (integer == 50) {
//                System.out.println(integer);
//            }
//        }
//
//        Iterator<Integer> iterator = set.iterator();     //итератор мн чыгаруу
//        while (iterator.hasNext()) {
//            int san = iterator.next();
//            if (san == 50) {
//                System.out.println(iterator.next());
//            }
//        }


        //ArrayList ке айландыруу
//        ArrayList<Integer> arrayList = new ArrayList<>(set);  //параметрине сетти беруу
//        arrayList.addAll(set);                                  // addAll методу мн кошуп чыгаруу
//        arrayList.add(arrayList.get(50));


        // сорттун туру bubble sort
        /*
        int[] array = {2,3,54,676,2,2344,-3,0};
        for (int i : puzzleSort(array)) {
            System.out.println(i);
        }

    }
    //сорттун бир туру bubble sort
    public static   int[] puzzleSort(int[] array){
        int san ;

        for (int i = 0; i < array.length; i++) {
            for (int j = i+1; j < array.length; j++) {
                if (array[i]> array[j]){
                    san= array[i];
                    array[i] = array[j];
                    array[j] = san;
                }
            }
        } return array;
    }

         */

        Student student1 = new Student("Aidai","Java","java-back",5);
        Student student2 = new Student("Ruslan","Java","java-back",4);
        Student student3 = new Student("Nurjigit","Java","java-back",6);
        Student student4 = new Student("Begimai","Java","java-back",7);
        Student student5 = new Student("Nurtegin","Java","java-back",8);
        Student student6 = new Student("Maral","Java","java-back",9);
        Student student7 = new Student("Aleriza","Java","java-back",11);
        Student student8 = new Student("Aizirek","Java","java-back",14);
        Student student9 = new Student("Timur","Java","java-back",2);
        Student student10 = new Student("Bakyt","Java","java-back",1);

            TreeSet<Student> studentTreeSet = new TreeSet<>();
            studentTreeSet.add(student1);
            studentTreeSet.add(student2);
            studentTreeSet.add(student3);
            studentTreeSet.add(student4);
            studentTreeSet.add(student5);
            studentTreeSet.add(student6);
            studentTreeSet.add(student7);
            studentTreeSet.add(student8);
            studentTreeSet.add(student9);
            studentTreeSet.add(student10);


        for (Student student : studentTreeSet) {
            System.out.println(student);
        }

        System.out.println("Before remove students");
        System.out.println(" ");

        Iterator<Student> iterator = studentTreeSet.iterator();
        while (iterator.hasNext()){
            if (iterator.next().getGrade()<3){
                iterator.remove();
            }
        }
        for (Student student : studentTreeSet) {
            System.out.println(student);
        }









    }


}