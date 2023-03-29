package day01;

import java.util.Scanner;

public class Array09 {

	public static void main(String[] args) {
		// 배열의 최고 점수 및 평균 점수 구하기
		
		boolean run = true;
		int studentNum = 0;
		int[] scores = null;
		Scanner sc = new Scanner(System.in);
		
		while(run) {
			System.out.println("--------------------------");
			System.out.println("1.학생수 | 2.점수입력 | 3.점수리스트 | 4.분석 | 5.종료 ");
			System.out.println("--------------------------");
			System.out.println("선택> ");
			
		    int selectNo = sc.nextInt();		// 입력값 
		    
		    if(selectNo == 1) {
		    	studentNum = sc.nextInt();
		    	scores = new int[studentNum];	// 배열 초기화
		    } else if(selectNo == 2) {
		    	for(int i = 0; i < studentNum; i++) {
		    		scores[i] = sc.nextInt();	// 점수 입력값 받아서 배열에 할당 
		    	}
		    } else if(selectNo == 3) {
		    	int n = scores.length;
		    	for(int i = 0; i < n; i++) {
		    		System.out.println(scores[i]);
		    	}
		    } else if(selectNo == 4) {
		    	int n = scores.length;
		    	int max = scores[0];
		    	int sum = 0;
		    	for(int i = 0; i < n; i++) {
		    		if(max < scores[i]) {
		    			max = scores[i];
		    		} 
		    		sum += scores[i];

		    	}	    		
		    	int avg = 0;
		    	avg = sum / n;
		    	System.out.println("최고 점수 : " + max);
		    	System.out.println("평균 점수 : " + avg);
		    	
		    } else if(selectNo == 5) {
		    	run = false;
		    }
		}
		System.out.println("프로그램 종료");
	}

}
