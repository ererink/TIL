package JAVA.실습;

public class InsertSort {

	public static void main(String[] args) {
		/*
		 * 선택 정렬: 
		 */

        int[] arr = { 64, 25, 12, 22, 11 };
        int n = arr.length;
        
        // 배열의 길이 만큼 반복 
        for (int i = 0; i < n; i++) {
        	int key = arr[i];	// 삽입할 값을 key 변수에 저장 
        	int j = i - 1;
        	
        	while(j >= 0 && arr[j] > key) {
        		arr[j + 1] = arr[j];
        		j--;
        	}
        	arr[j + 1] = key; 	// key값 삽입 
        	
        }
        
        // 정렬 결과 출력
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }


	}

}
