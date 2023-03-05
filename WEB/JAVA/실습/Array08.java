package day01;

public class Array08 {

	public static void main(String[] args) {
		// 배열의 전체 항목의 합과 평균값 구하기 
		int [][] arr = {
			{95, 86},
			{83, 92, 96},
			{78, 83, 93, 87, 88},
		};
		
		int sum = 0;
		double avg = 0.0;
		int n = arr.length;	// 
		int cnt = 0;
		for(int i = 0; i < n; i++) {
			int m = arr[i].length;
			for(int j = 0; j < m; j++) {
				sum += arr[i][j];
			}
			cnt += m;
		}
		avg = sum / cnt;
		System.out.println("sum : " + sum);
		System.out.println("avg : " + avg);
	}

}