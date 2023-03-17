package Algo_day07;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1991_트리순회_김예린 {
    static int N;
    static int leaf = -19;
    static int [][] tree;


    // 전위 순회
    static void preOrder(int x) {
        // -19를 마주친 경우
        if (x == -19) return;   // 더 이상 갈 곳이 없음

        System.out.print((char) (x + 65));
        preOrder(tree[x][0]);   // 왼쪽자식
        preOrder(tree[x][1]);   // 오른쪽자식
    }

    // 중위 순회
    static void inOrder(int x){
        if (x == -19) return;   // 더 이상 갈 곳이 없음

        inOrder(tree[x][0]);   // 왼쪽자식

        System.out.print((char) (x + 65));

        inOrder(tree[x][1]);   // 오른쪽자식
    }

    // 후위 순회
    static void postOrder(int x){
        if (x == -19) return;   // 더 이상 갈 곳이 없음

        postOrder(tree[x][0]);   // 왼쪽자식
        postOrder(tree[x][1]);   // 오른쪽자식

        System.out.print((char) (x + 65));

    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        tree = new int[N][2];

        for (int i=0; i<N; i++){
            st = new StringTokenizer((bf.readLine())," ");
            int parent = st.nextToken().charAt(0) - 'A';
            int child1 = st.nextToken().charAt(0) - 'A';
            int child2 = st.nextToken().charAt(0) - 'A';
            tree[parent][0] = child1;
            tree[parent][1] = child2;
        }

        preOrder(0);
        System.out.println();
        inOrder(0);
        System.out.println();
        postOrder(0);
        System.out.println();
    }


}
