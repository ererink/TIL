package Day6.B11047_동전0;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class B11047_동전0_김예린 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(),  " ");
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        Integer [] arr = new Integer[N];

        for (int i=0; i<N ; i++){
            st = new StringTokenizer(bf.readLine());
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int total = 0;
        int cnt = 0;
        Arrays.sort(arr, Collections.reverseOrder());

        for (int i=0; i<N ; i++){
            if (arr[i] > K) {
                continue;
            }
            total += K / arr[i];
            K %= arr[i];

            if (K == 0){
                break;
            }
        }
        System.out.println(total);
    }
}
