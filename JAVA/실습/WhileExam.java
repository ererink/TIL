package JAVA.실습;

public class WhileExam {

	public static void main(String[] args) {
		// 1 ~ 100까지 10행 10열 이중 while문 
		
		// 초기화
		int i = 1;
		while(i <= 10) { // 10행
			int j = 1;
			while(j <= 10) { // 10열
				System.out.print(((i-1)*10+j) + " ");	//i값을 1 뺀 후 10을 곱한 값에 j를 더하면 각 열에 맞는 값 출
				j++;
			}
			System.out.println();
			i++;
		}

	}

}
