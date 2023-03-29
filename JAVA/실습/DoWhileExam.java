package JAVA.실습;

public class DoWhileExam {

	public static void main(String[] args) {
		// 1 ~ 100까지 10행 10열 이중 do while문 
		int i = 1; // 초기화
		do {
			int j = 1;
			do {
				System.out.print(((i-1)*10+j) + " ");
				j++;
			}while(j <= 10);
			System.out.println();
			i++;
		}while(i <= 10);

	}

}
