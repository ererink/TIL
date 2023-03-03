import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    while(sc.hasNextInt()){     // 정수일 경우 true 반환, 정수 이외일 경우 예외를 던지고 반복문 종료
	        int A = sc.nextInt();
	        int B = sc.nextInt();
	        System.out.println(A+B);
	        
	    }
        sc.close();
	    
	}
}