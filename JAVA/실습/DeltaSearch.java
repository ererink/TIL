package JAVA.실습;

import java.util.LinkedList;
import java.util.Deque;

public class DeltaSearch {

	public static void main(String[] args) {
		int[][] arr = {
			{1, 2, 5, 7, 3, 4},
			{3, 1, 9, 8, 4, 5},
			{6, 2, 4, 6, 2, 8},
			{9, 7, 4, 3, 7, 8},
			{2, 3, 4, 8, 4, 6},
			{4, 6, 2, 3, 7, 8},
		};
		int n = arr.length;	// 행
		int m = arr[0].length; // 열
		int[] dx = {0, 0, 1, -1};
		int[] dy = {1, -1, 0, 0};
		
		Deque<Integer> deque = new LinkedList<>();
		for(int k = 1; k < Math.max(n, m); k++) {
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < m; j++) {
					for(int d = 0; d < 4; d++) {
						int nx = i + dx[d] * k;
						int ny = j + dx[d] * k;
						
						if(nx >= 0 && ny >= 0 && nx < n && ny < m ) {
							if(arr[nx][ny] % 2 == 0){
								deque.add(arr[nx][ny]);
							}
						}
					}
				}
			}
			if(!deque.isEmpty()) {
				System.out.println(k + deque.toString());
				deque.clear();
			}		
		}		

	}

}
