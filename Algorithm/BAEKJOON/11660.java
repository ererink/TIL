package Day1.B11659_구간합구하기;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class B11660_구간합구하기2_김예린 {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(),  " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int [][] arr1 = new int[N+1][N+1];

        // 누적합
        for (int i=1; i <= N; i++){
            st = new StringTokenizer(bf.readLine(), " ");
            for (int j=1; j <= N; j++){
                arr1[i][j] = Integer.parseInt((st.nextToken()));
            }
        }
        // System.out.println(Arrays.deepToString(arr1));


        int [][] dp = new int[N+1][N+1];
        for (int x=1; x<=N; x++){
            for (int y=1; y<=N; y++){
                dp[x][y] = dp[x][y-1] + dp[x-1][y] - dp[x-1][y-1] + arr1[x][y];
            }
        }
        for (int i=1; i <= M; i++){
            st = new StringTokenizer(bf.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            //int total = 0;

            //for (int j=x1; j <= x2; j++) {
            //    total += arr1[j][y2] - arr1[j][y1 - 1];

            //}

            int tot = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1];


            System.out.println(tot);
        }

    }
}
