package Day2.B1158_요세푸스문제;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class B1158_요세푸스문제_김예린 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        Queue<Integer> que = new ArrayDeque<>();

        // 1부터 N까지 수열
        for (int i=1; i<=N; i++){
            que.add(i);
        }
        System.out.print("<");

        while (que.size() != 0){
            for (int i=0; i < K - 1; i++){
                que.add(que.poll());
            }
            System.out.print(que.poll());

            if (que.size() > 0){
                System.out.print(", ");
            }
        }
        System.out.println(">");
    }
}
