import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    while(true){
	        int A = sc.nextInt();
	        int B = sc.nextInt();
	        
	        if(A==0 && B==0){
	            sc.close(); // 입력값 받기 종료
	            break;
	        }
            System.out.println(A+B);
	    }
	}
}