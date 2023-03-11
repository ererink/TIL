import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int sum = 0;
        int [] arr = new int[1000];     // 나머지와 상응하는 인덱스에 카운트를 세어준다.
        int cnt = 0;

        st = new StringTokenizer(bf.readLine());
        while (N --> 0){
            int inp = Integer.parseInt((st.nextToken()));
            sum += inp;
            sum %= M;
            cnt += arr[sum];    // 이전에 동일한 구간합 나머지가 나왔던 카운트 더해주기
            arr[sum]++;         // 해당 나머지와 상응하는 인덱스에 카운트
            if (sum==0) cnt++;  // 나머지가 0일 경우 카운트
        }
        System.out.println(cnt);
    }
}