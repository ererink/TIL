package Algo_day08;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class B13023_ABCDE_김예린 {
    static int [] visited;
    static int N, M;
    static ArrayList<Integer> [] arr;
    static boolean flag;
    static void dfs(int V, int cnt){
        if (flag == true){
            return;
        }
        if (cnt == 5){
            flag = true;
            return;
        }
        for (int i : arr[V]) {
            if (visited[i] == 0){
                visited[i] = 1;
                dfs(i,  cnt+1);
                visited[i]= 0;
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new ArrayList[N];
        for (int i=0;i<N;i++){
            arr[i] = new ArrayList<>();
        }
        visited = new int [N];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer((bf.readLine())," ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a].add(b);
            arr[b].add(a);

        }
        for (int i = 0; i < N; i++) {
            visited[i] = 1;
            dfs(i, 1);
            visited[i] = 0;
        }

        if (flag == true){
            System.out.println(1);
        }
        else {
            System.out.println(0);
        }

    }
}
