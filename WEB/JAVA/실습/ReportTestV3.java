package day01;

public class ReportTestV3 {

	public static void main(String[] args) {
		String name;
		int kor;
		int eng;
		int math;
		int total;
		double avg;
		char grade;

		name = "김예린";
		kor = 80;
		eng = 90;
		math = 100;

		total = kor + eng + math;
		avg = total / 3;

		switch ((int) avg / 10) {
			case 10:
			case 9:
				grade = 'A';
				break;
			case 8:
				grade = 'B';
				break;
			case 7:
				grade = 'C';
				break;
			case 6:
				grade = 'D';
				break;
			default:
				grade = 'F';
				break;
		}

		System.out.println(grade);
	}
}

