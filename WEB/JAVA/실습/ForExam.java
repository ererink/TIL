package day01;

public class ForExam {

	public static void main(String[] args) {
		// 1 ~ 100까지 이중 for문 출력
		for(int i=0; i < 10; i++) {
			for(int j=1; j <= 10; j++) {
				System.out.print(i * 10 + j + " ");
			}
			System.out.println();
		}
	}
}
