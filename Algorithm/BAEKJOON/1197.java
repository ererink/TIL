package Algo_day10;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
/*
크루스칼 알고리즘
 */
class Edge{
    int start;
    int end;
    int weight;

    Edge(int start, int end, int weight){
        this.start = start;
        this.end = end;
        this.weight = weight;
    }

    @Override
    public String toString(){
        return "[" + this.start + "," + this.end + "," + this.weight + "]";
    }

}
public class B1197_최소스패닝트리_김예린 {

    static int N, M;
    static int [] parent;

    public static int find(int x){
        if (x == parent[x]){
            return x;
        }
        return parent[x] = find(parent[x]);
    }

    public static void union(int x, int y){
        x = find(x);
        y = find(y);
        if (x != y){    // 부모가 같지 않아야 사이클 성립X
            if (x < y){
                parent[y] = x;
            } else {
                parent[x] = y;
            }
        }
    }
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M  = Integer.parseInt(st.nextToken());
        Edge [] edges = new Edge[M];
        parent = new int[N+1];
        Arrays.setAll(parent, i->i);

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(bf.readLine(), " ");
            int u = Integer.parseInt(st.nextToken());
            int v  = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            edges[i] = new Edge(u, v, weight);
        }


        // 가중치 기준 간선 정렬
        Arrays.sort(edges ,  (a,b) -> a.weight - b.weight );
        //System.out.println(Arrays.toString(edges)); => [[1,2,1], [2,3,2], [1,3,3]]

        int cnt = 0;
        for (Edge i : edges) {
            if (find(i.start) != find(i.end)){
                union(i.start, i.end);
                cnt += i.weight;
            }
        }
        System.out.println(cnt);
    }
}
