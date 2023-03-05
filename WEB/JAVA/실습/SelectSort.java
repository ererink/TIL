package day01;

public class SelectSort {

	public static void main(String[] args) {
		/*
		 * 선택 정렬: 맨 앞에 위치한 값과 비교 및 교체하는 방식 
		 */

		// 선택 정렬 예시 
        int[] arr = { 64, 25, 12, 22, 11 };
        int n = arr.length;
        
        // 선택 정렬 수행
        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            
            // 현재 인덱스 i와 가장 작은 값을 가진 인덱스 minIndex를 교환
            int temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;
        }
        
        // 정렬 결과 출력
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }


	}

}
