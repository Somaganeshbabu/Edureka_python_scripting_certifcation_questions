package Java_programs;
import java.util.*;
class count_zeros{
    public static void trailing_zeros(int n){
        int count = 0;
        while(n>=5){
            n=n/5;
            count +=n;
        }
        System.out.println(count);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter value to find factorial:-");
        int n= sc.nextInt();
        trailing_zeros(n);
        sc.close();
    }
}