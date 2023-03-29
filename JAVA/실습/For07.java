package JAVA.실습;

import java.util.Scanner;

public class For07 {

	public static void main(String[] args) {
		// 예금/출금/조회/종료 기능 제공 코드 작성
		boolean run = true;
		int balance = 0;
		Scanner sc = new Scanner(System.in); 	// 입력값 
		
		while(run) {
			System.out.println("--------------------------");
			System.out.println("1.예금 | 2.출금 | 3.잔고 | 4.종료");
			System.out.println("--------------------------");
			System.out.println("선택>");
			
			int selec = sc.nextInt();	// 선택 
			
			if(selec == 1) {
			    int deposit = sc.nextInt();	// 예금액 입력 
			    balance += deposit;
			    System.out.println("예금액>" + balance);
			} else if (selec == 2) {
				int withdraw = sc.nextInt(); // 출금액 입력 
				if (balance < withdraw) {
					System.out.println("잔고가 부족합니다.");
				} else {
					balance -= withdraw;
					System.out.println("출금이 완료되었습니다.");
				}
			} else if (selec == 3) {
				System.out.println("잔고>" + balance);
			} else if (selec == 4) {
				run = false;
			} else {
				System.out.println("잘못된 입력입니다. 다시 선택해주세요.");
			}
			
		}
		System.out.println("프로그램 종료");
		sc.close();
	}

}
