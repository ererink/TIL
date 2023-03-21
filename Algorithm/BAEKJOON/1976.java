package Day9.B1976_여행가자;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1976_여행가자_김예린 {
    static int N, M;
    static int [] arr;

    static int find(int x){
        if (arr[x] == x){
            return x;
        }
        else {
            // 부모로 이동
            return arr[x]=find(arr[x]);
        }
    }
    static void union(int x, int y){
        int a = find(x);
        int b = find(y);
        if (a < b){
            arr[b] = a;
        }
        else {
            arr[a] = b;
        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(bf.readLine());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N+1];
        // 초기화
        for (int i = 0; i <= N; i++) {
            arr[i] = i;
        }

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(bf.readLine(), " ");
            for (int j = 0; j < N; j++) {
                int a = Integer.parseInt(st.nextToken());
                if (a == 1){
                    union(i + 1, j + 1);
                }
            }
        }
        int answer[] = new int[M];
        st = new StringTokenizer(bf.readLine(), " ");
        int temp = arr[Integer.parseInt(st.nextToken())];
        for (int i = 1; i < M; i++) {
            int city = Integer.parseInt(st.nextToken());
            if (temp != arr[city]){
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }
}
