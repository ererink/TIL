package day01;

public class No4 {

	public static void main(String[] args) {
		int pencils = 534;
		int students = 30;
		
		// 학생 한 명이 가지는 연필 수 
		int pencilPerStudent = pencils / students;
		System.out.println(pencilPerStudent);
		
		// 남은 연필 수
		int pencilsLeft = pencils % students;
		System.out.println(pencilsLeft);

	}

}
