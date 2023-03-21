package Day9.B1325_효율적인해킹;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class B1325_효율적인해킹_김예린 {
    static int N, M, cnt, max_cnt;
    static ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
    static boolean [] visited;
    static int [] answer;
    static void search(int s){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(s);
        visited[s] = true;
        while (!queue.isEmpty()){
            int x = queue.poll();

            for (int i : arr.get(x)) {
                if (visited[i] == false){
                    cnt++;
                    visited[i] = true;
                    queue.add(i);
                }
            }
        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M  = Integer.parseInt(st.nextToken());
        //arr = new ArrayList[N+1];
        max_cnt = 0;
        answer = new int[N+1];
        StringBuilder sb = new StringBuilder();

        for (int i=0;i<=N;i++){
            arr.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer((bf.readLine())," ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr.get(b).add(a);
        }

        for (int i = 1; i <= N; i++) {
            visited = new boolean[N+1];
            cnt = 0;
            search(i);

            answer[i] = cnt;
            max_cnt = Math.max(cnt, max_cnt);
        }

        for (int i = 1; i <= N; i++) {
            if (answer[i] == max_cnt){
                sb.append(i + " ");
            }
        }
        System.out.println(sb);
    }
}
