package JAVA.실습;

public class BubbleSort {

	public static void main(String[] args) {
		/*
		 * 버블 정렬: 맨 앞에 위치한 값과 비교 및 교체하는 방식 
		 */

        int[] arr = { 64, 25, 12, 22, 11 };
        int n = arr.length;
        
        // 배열의 길이 -1 만큼 반복 
        for (int i = 0; i < n - 1; i++) {
        	// 배열의 길이 -1 만큼 반복하되, i번째까지는 이미 정렬되었으므로 제외 
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                	int temp = arr[j];
                	arr[j] = arr[j + 1];
                	arr[j + 1] = temp;
                }
            }
            
        }
        
        // 정렬 결과 출력
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }


	}

}
