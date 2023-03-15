package Day5.B1068_트리;


import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class B1068_트리_김예린 {
    static int N, R, root, cnt;
    static ArrayList<Integer> tree [];
    static boolean [] visited;
    static void Search(int node){
        boolean isLeaf = true;
        for (int adj:tree[node]){
            if (visited[adj] == false){
                visited[adj] = true;
                isLeaf = false;
                Search(adj);
            }
        }
        if (isLeaf) {
            cnt++;
        }
    }
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        tree = new ArrayList[N+1];
        visited = new boolean[N];
        cnt = 0;
        for (int i=0; i<N; i++){
            tree[i] = new ArrayList<>();
        }
        for (int i=0; i<N; i++){
            int u = sc.nextInt();
            if (u == -1){
                root = i;
            }
            else {
                tree[u].add(i);
            }

        }

        R = sc.nextInt();

//        for (int i=0; i<N; i++){
//            System.out.println(tree[i]);
//        }

        if (root == R){
            System.out.println(0);
        }
        else {
            visited[R] = true;
            Search(root);

            System.out.println(cnt);
        }

    }
}
