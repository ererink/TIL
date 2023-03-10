package Day2.B2164_카드2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class B2164_카드2_김예린 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());

        Queue<Integer> que = new ArrayDeque<>();
        for (int i=1; i<=N; i++){
            que.add(i);
        }
        while (que.size() != 1){
            que.poll();
            int front = que.poll();
            que.add(front);

        }
        int answer = que.poll();
        System.out.println(answer);
    }
}
