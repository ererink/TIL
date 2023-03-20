package Algo_day08;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class J1828_냉장고_김예린 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int [][] arr = new int[N][2];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer((bf.readLine())," ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[i][0] = b;  // 최고보관온도
            arr[i][1] = a;  // 최저보관온도

        }

        Arrays.sort(arr, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] == o2[0]){
                    return o1[1] - o2[1];
                }
                return o1[0] - o2[0];
            }
        });

        int temp = 0;
        int cnt = 1;

        for (int i = 0; i < N; i++) {
            if (arr[i][1] > temp){
                temp = arr[i][0];
                cnt ++;
            }
        }
        System.out.println(cnt);
    }
}
