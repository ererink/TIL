package sample2;

public class MainApp {

	public static void main(String[] args) {
		Employee [] emplo = new Employee[5];

		emplo[0] = new FullTime(10, "유재석", "개그우먼", 0 , "2013-05-01", "무한도전", 8500, 200);
		emplo[1] = new FullTime(20, "박명수", "가수",10, "2013-06-20", "무한도전",7500,100);
		emplo[2] = new FullTime(30, "정준하", "예능인",10 , "2013-06-22", "무한도전",6000,0);
		emplo[3] = new PartTime(40, "노홍철", "예능인",20 , "2014-05-01", "무한도전",20000);
		emplo[4] = new PartTime(50, "하하", "가수",30 , "2014-05-02", "무한도전",25000);
		
		System.out.println("******* EMP 정보 *******");
		for(Employee employee : emplo) {
			System.out.println(employee);
		}

	}

}
