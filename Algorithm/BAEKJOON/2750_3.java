package Day3.B2750_삽입정렬;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B2750_삽입정렬_김예린 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int [] arr = new int[N];

        for (int i=0; i <N; i++){
            st = new StringTokenizer(bf.readLine());
            int inp = Integer.parseInt(st.nextToken());
            arr[i] = inp;
        }

        int [] min = new int[2];
        for (int i=0; i < N; i++){
            min[0] = arr[i];
            min[1] = i;
            for (int j=0; j < i; j++){     // i까지 탐색
                if (arr[j] > arr[i]){
                    // 작은값이 들어갈 위치 저장
                    min[0] = arr[i];
                    min[1] = j;
                    // 나머지값 뒤로 이동
                    for (int k=i-1; k>=j; k--){
                        arr[k+1] = arr[k];
                    }
                    arr[min[1]] = min[0];
                }
            }
        }
        for (int i=0; i<N; i++){
            System.out.println(arr[i]);
        }
    }
}
