package Day6.B1931_회의실배정;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class B1931_회의실배정_김예린 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int [][] arr = new int [N][2];

        int temp = 0;
        int cnt = 0;

        for (int i=0; i < N; i++){
            st = new StringTokenizer(bf.readLine(), " ");
            int S = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            arr[i][0] = E;
            arr[i][1] = S;
        }
        Arrays.sort(arr, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if(o1[0] == o2[0]) {
                    return o1[1] - o2[1];   // 종료시간이 같다면 시작시간이 빠른 순서
                }
                return o1[0] - o2[0]; // 종료시간 기준으로 정렬
            }
        });

        for (int i=0; i<N; i++){

            if (arr[i][1] >= temp){
                temp = arr[i][0];
                cnt++;
            }

        }
        System.out.println(cnt);

    }
}

