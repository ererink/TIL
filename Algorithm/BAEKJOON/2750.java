package Day3.B2750_선택정렬;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B2750_선택정렬_김예린 {
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
            for (int j= i + 1; j < N; j++){
                if (min[0] > arr[j]){
                    min[0] = arr[j];
                    min[1] = j;
                }
            }
            int temp = arr[i];
            arr[i] = min[0];
            arr[min[1]] = temp;
        }
        for (int i=0; i<N; i++){
            System.out.println(arr[i]);
        }
    }
}
