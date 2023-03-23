package Algo_test2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class kb2반_알고리즘1번_김예린 {
    static int N, M, cnt, result;
    static ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
    static boolean [] visited;

    static void search(int s){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(s);
        visited[s] = true;
        while (!queue.isEmpty()){
            int x = queue.poll();

            for (int i : arr.get(x)) {
                if (visited[i] == false) {
                    cnt++;
                    visited[i] = true;
                    queue.add(i);
                }
            }
        }
        System.out.println(cnt);

    }
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(bf.readLine());
        M = Integer.parseInt(st.nextToken());
        result = 0;
        visited = new boolean[N+1];


        for (int i=0;i<=N;i++){
            arr.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(bf.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr.get(a).add(b);
        }

        search(1);
    }
}
