package Day7.B1260_DFS와BFS;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class B1260_DFS와BFS_김예린 {
    static int N, M, V;
    static int [][] arr;
    static boolean [] visited1, visited2;
    static Queue<Integer> queue;
    static void dfs(int V){
        visited1[V] = true;
        System.out.print(V + " ");

        for (int i = 1; i <= N; i++) {
            if (arr[V][i] != 0 && visited1[i] == false){
                dfs(arr[V][i]);
            }
        }
    }

    static void bfs(int V){
        queue = new LinkedList<Integer>();
        queue.add(V);
        visited2[V] = true;
        System.out.print(V + " ");

        while (!queue.isEmpty()){
            int x = queue.poll();

            for (int i = 1; i < arr.length; i++) {
                if (arr[x][i] != 0 && visited2[i] == false){
                    queue.add(arr[x][i]);
                    visited2[i] = true;
                    System.out.print(arr[x][i] + " ");
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M  = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());
        arr = new int [1001][1001];
        visited1 = new boolean[1001];
        visited2 = new boolean[1001];

        for (int i=0; i<M; i++){
            st = new StringTokenizer((bf.readLine())," ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a][b] = b;
            arr[b][a] = a;
        }


        dfs(V);
        System.out.println();
        bfs(V);
    }
}
