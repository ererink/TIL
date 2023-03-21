package Day8.B9663_NQueen;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B9663_NQueen_김예린 {
    static int N, cnt;
    static int [] board;
    static boolean flag;
    static void dfs(int x){ // 현재 열
        if (x == N){
            cnt++;
            return;
        }
        for (int i = 0; i < N; i++) {   // 탐색할 열
            for (int j = 0; j < x; j++) {   // 처음 ~ 현재위치 탐색 (이전 행)
                if(i == board[j] || Math.abs(x - j) == Math.abs(i - board[j])) {  // 상하좌우 || 대각선 탐색
                    flag = true;
                }
            }
            if (flag == false){
                board[x] = i; // 두기
                dfs(x + 1);
            }
            flag = false;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        board = new int[N];

        dfs(0);
        System.out.println(cnt);
    }
}
