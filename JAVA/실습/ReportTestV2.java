package day01;

public class ReportTestV2 {

	public static void main(String[] args) {
		String name = "김예린";
		int kor; 
		int eng; 
		int math;
		int total; 
		double avg; 
		char grade;
		
		kor = 80;
		eng = 90;
		math = 100;
		
		total = kor + eng + math;
		avg = total / 3;
		
		if (avg >= 90) {
			grade = 'A';
			 System.out.println(grade);
		}
		else if(80 <= avg && avg >= 89){
			grade = 'B';
			System.out.println(grade);
		}
		else if(70 <= avg && avg >= 79){
			grade = 'C';
			System.out.println(grade);
		}
		else if(60 <= avg && avg >= 69){
			grade = 'D';
			System.out.println(grade);
		}
		else {
			grade = 'F';
			System.out.println(grade);
		}
	}

}
