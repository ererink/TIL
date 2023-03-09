package Day1.B11659_구간합구하기;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

import java.util.StringTokenizer;

public class B11659_구간합구하기_김예린 {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(),  " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(bf.readLine());
        int [] arr = new int[N + 1];

        for (int i=1; i <= N; i++){
            arr[i] = arr[i - 1] + Integer.parseInt((st.nextToken()));
        }
        System.out.println(Arrays.toString(arr));


        for (int i = 0; i < M; i++){
            st = new StringTokenizer(bf.readLine());
            int k = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            System.out.println(arr[v] - arr[k-1]);
            }

    }


}
