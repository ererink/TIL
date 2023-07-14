import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in); 
    int a = sc.nextInt();
    int b = sc.nextInt();
    int result = a * b;
    for(int i=0; i<3; i++){
          int num = b % 10;
          System.out.println(a * num);
          b /= 10;
        }
    System.out.println(result);
  }
}