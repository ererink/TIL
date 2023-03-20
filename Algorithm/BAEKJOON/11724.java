package Day7.B11724_연결요소의개수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class B11724_연결요소의개수_김예린 {
    static int N, M, cnt;
    static boolean[] visited;
    static int [][] arr;
    static Stack<Integer> check;
    static void dfs(int node) {
        if (visited[node] == true){
            return;
        }

        else {
            visited[node] = true;
            for (int i = 1; i <= N; i++) {
                if (arr[node][i] != 0 && visited[i] == false) {
                    dfs(arr[node][i]);
                }
            }
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[1001][1001];
        visited = new boolean[1001];
        cnt = 0;

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer((bf.readLine())," ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a][b] = b;
            arr[b][a] = a;
        }
        for (int i = 1; i <= N; i++) {
            if (visited[i] == false){
                dfs(i);
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
