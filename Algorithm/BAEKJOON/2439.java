import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    int n = sc.nextInt();
	    sc.close();
	    
	    for(int i=1; i <= n; i++){
	        for(int j=1; j <= n - i; j++){  // 공백과 별의 개수를 n과 맞추기
	            System.out.print(" ");
	        }
	        for(int k=0; k < i; k++){
	            System.out.print("*");
	        }
	        System.out.println();
	    } 
	}
}