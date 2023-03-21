package Day9.B1717_집합의표현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1717_집합의표현_김예린 {
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
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int [N + 1];
        // 초기화
        for (int i = 0; i <= N; i++) {
            arr[i] = i;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(bf.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a == 0){
                union(b, c); // 부모 저장
            }
            else if (a == 1) {
                if (find(b)==find(c)){
                    System.out.println("YES");
                }
                else {
                    System.out.println("NO");
                }
            }
        }
    }
}
