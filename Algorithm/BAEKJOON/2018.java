package Day1.B2018_수들의합;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B2018_수들의합_김예린 {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());

        int cnt = 1;

        for (int i = 0; i <= N; i++){
            int sum = 0;    // 부분합
            for (int j=i+1; j <= N; j++){

                if (sum == N){
                    cnt ++;
                    break;
                }
                if (sum > N) {
                    break;
                }
                sum += j;
            }

        }
        System.out.println(cnt);
    }
}
