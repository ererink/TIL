import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static int N;
    static ArrayList<Integer> tree [];
    static int [] parent;
    static boolean [] visited;
    static void Search(int node){
        for (int nextNode : tree[node]){
            if (visited[nextNode]) continue;
            visited[nextNode] = true;
            Search(nextNode);
            parent[nextNode] = node;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        tree = new ArrayList[N + 1];
        parent = new int[N + 1];
        visited = new boolean[N+1];
        for (int i=0; i < tree.length; i++){
            tree[i] = new ArrayList<>();
        }
        for (int i = 0; i < N-1; i++){
            int u = sc.nextInt();
            int v = sc.nextInt();
            tree[u].add(v);
            tree[v].add(u);
        }
        visited[1] = true;
        Search(1);
        for (int i=2; i<N+1; i++){
            System.out.println(parent[i]);
        }
    }
}