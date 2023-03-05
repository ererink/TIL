package day01;

public class Array07 {

	public static void main(String[] args) {
		// 배열의 최대값 구하기 
		int [] arr = { 1, 5, 3, 8, 2};
		int n  = arr.length;	// 배열의 길
		int max = arr[0];
		for(int i = 1; i < n; i++) {
			if(max < arr[i]) {
				max = arr[i];
			}
		}
		
		System.out.println("max: " + max);
	}

}