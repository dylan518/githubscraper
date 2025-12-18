package org.example;


import java.util.*;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) {

        /*
//        int[] arr = new int[]{1,1,0,0,1,1,0,1,1};
        int[] arr = new int[]{0,1};

        int n=arr.length;
        int[] sumArr = new int[n];

        Map<Integer,Integer> m2= new HashMap<>();

        m2.put(0,-1);
        int ans =0;

        int sum=0;
        for(int i=0;i<=n-1;i++){

            if(arr[i]==0){
                sum+=1;
            }else{
                sum-=1;
            }
            sumArr[i]=sum;

            if(m2.containsKey(sum)){
                int idx = m2.get(sum);
                int len = i-idx;
                if(len>ans){
                    ans=len;
                }
            }else{
                m2.put(sum,i);
            }

        }

        System.out.println(Arrays.toString(arr));
        System.out.println(Arrays.toString(sumArr));
        System.out.println(ans);

        int tempMaxDiff=0;
        int iIndex=0;
        int jIndex=0;
        int maxDiff=0;
        int j=n;
        Map<Integer,Integer> m1 = new HashMap<>();

//        for(int i=0;i<n;i++){
//            for(int k=n-1;k>i;k--){
//                System.out.println(i+","+k);
//                if(sumArr[i]==sumArr[k]){
//                    //m1.put(i,k);
//                    tempMaxDiff = k-i;
//                    System.out.println(i+"th,"+sumArr[i]+" | "+k+"th,"+sumArr[k]+" | "+tempMaxDiff);
//                    if(maxDiff<tempMaxDiff){
//                        maxDiff=tempMaxDiff;
//                        iIndex=i;
//                        jIndex=k;
//                        //System.out.println("maxDiff-"+maxDiff+",i-"+i+",j-"+j);
//                    }
//                }
//            }
//        }
//        System.out.println("maxDiff-"+maxDiff+",i-"+iIndex+",k-"+jIndex);
        //System.out.println(m1);

//

//
//        int ans=0;
//        for(int i=0;i<sumArr.length-2;i++){
//
//            int pivot=sumArr[i];
//            int count=0;
//
//            for(int j=n-1;j>i+1;j--){
//
//                System.out.println("i="+i+",j="+j+",pivot="
//                        +pivot+",sumArr[j]="+sumArr[j]);
//                if(j==n-1){count=0;System.out.println("trip\n");}
//                if(pivot==sumArr[j]){
//                    System.out.println("trip\n");
//                    break;
//                }
//
//
//            }
//            //System.out.println(count);//[1, 2, 1, 0, 1, 2, 1, 2, 3]
//            ans = Math.max(ans,count);
//
//        }
//
//
//        System.out.println("ans="+(ans+1));



//
//
//        int[] arr = new int[]{-7, 1, 5, 2, -4, 3, 0};
//
//        int totalSum=0;
//        for(int i:arr){
//            totalSum = totalSum + i;
//        }
//
//        int[] leftArrSum = new int[arr.length];
//        int leftSideSum=0;
//        for (int i=0;i<arr.length-1;i++){
//            leftSideSum=leftSideSum+arr[i];
//            leftArrSum[i]=leftSideSum-arr[i];
//        }
//
//        for (int j=0;j<arr.length-1;j++){
//            if(leftArrSum[j]==totalSum-arr[j]-leftArrSum[j]){
//                System.out.println(j);
//                break;
//            }
//        }

//        for (int i:leftArrSum){
//            System.out.print(i+",");
//        }
//        System.out.println("\n");
//        for (int i:rightArrSum){
//            System.out.print(i+",");
//        }

//        int i=0;
//        int j=0;
//        while( i< leftArrSum.length-1 &&  j< rightArrSum.length-1){
//
//            if(leftArrSum[i] == rightArrSum[j]){
//                System.out.println(i);
//            }
//            i++;
//            j++;
//    }
*/


//        Employee e11 = new Employee("abc",101);
//        Employee e22 = new Employee("abc",101);

//        HashSet<Employee> h1 = new HashSet<>();
//        h1.add(e11);
//        h1.add(e22);

//        System.out.println(h1.size());

        HashSet<Integer> h2 = new HashSet<>();
        h2.add(1);
        h2.add(1);

        System.out.println(h2.size());


        Employee e1 = new Employee();
        e1.setName("ateeb");
        e1.setSalary(100);

        Employee e2 = new Employee();
        e2.setName("arif");
        e2.setSalary(200);

        Employee e3 = new Employee();
        e3.setName("akib");
        e3.setSalary(300);

        Employee e4 = new Employee();
        e4.setName("shobhit");
        e4.setSalary(400);

        List<Employee> l1 = new ArrayList<>();
        l1.add(e1);
        l1.add(e2);
        l1.add(e3);
        l1.add(e4);

        l1.stream().filter(x->x.getSalary()>200)
                .map(x->x.getName()).forEach(System.out::println);

//        l1.stream()
//                .sorted((x1,x2)->
//                        (x1.getSalary()<x2.getSalary())? 1:(x1.getSalary()<x2.getSalary())? 0:-1)
//                .forEach(System.out::println);


//        Map<?, ?> m = l1.stream()
//                .collect(Collectors.partitioningBy(x -> x.getSalary() > 200));
//
//        System.out.println(m);

    }
}

class Employee{

    String name;
    int salary;

    @Override
    public String toString() {
        return "Employee{" +
                "name='" + name + '\'' +
                ", salary=" + salary +
                '}';
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }
}
