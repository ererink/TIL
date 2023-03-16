package Day6.B2839_설탕배달;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B2839_설탕배달_김예린 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int cnt = 0;

        while (true) {
            if (N % 5 == 0) {
                System.out.println(N / 5 + cnt);
                break;
            } else if (N < 0) {
                System.out.println(-1);
                break;
            }
            N = N - 3;
            cnt++;
        }
    }
}





