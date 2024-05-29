package Java_programs;
import java.util.*;

class missing_value{
    public static void findMissing(int arr[], int N) {
        int original_sum = (N*(N+1))/2;
        int actual_sum =0;
        int missing_value;
        for (int i=0; i<arr.length; i++){
            actual_sum +=arr[i];
        }
        missing_value = original_sum-actual_sum;
        System.out.println("missing_number=" + missing_value);

    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("enter N value:- ");
        int N = sc.nextInt();
        int[] my_list = new int[N-1];
        for (int i=0; i<N-1;i++){
            System.out.println("Enter the values one by one (press Enter after each value):");
            my_list[i] = sc.nextInt();
        }
        sc.close();
        findMissing(my_list,N);
    }
}

