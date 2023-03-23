package Algo_test2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class kb2반_알고리즘2번_김예린 {
    static int N, M, v1, v2;
    static int [][] arr, visited;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        visited = new int[N][M];
        arr = new int[N][M];
        v1 = 0; v2 = 0;

        for (int i = 0; i < N; i++) {
            String line = bf.readLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = line.charAt(j) - '0';
            }
        }

        st = new StringTokenizer(bf.readLine(), " ");
        v2 = Integer.parseInt(st.nextToken()) - 1;
        v1 = Integer.parseInt(st.nextToken()) - 1;

        Queue<Integer[]> queue = new LinkedList<>();
        queue.add(new Integer[]{v1, v2});
        int [] dx = {0, 0, -1, 1};
        int [] dy = {1, -1, 0, 0};

        while (!queue.isEmpty()){
            Integer[] ele = queue.poll();
            int x = ele[0];
            int y = ele[1];

            for (int i = 0; i < 4; i++) {
                Integer nx = x + dx[i];
                Integer ny = y + dy[i];

                if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                    if (arr[nx][ny] == 1 && visited[nx][ny] == 0){
                        visited[nx][ny] = visited[x][y] + 1;
                        arr[nx][ny] = 2;                    // 감염되지 않은 학생 수를 세기 위해 다른 수 할당
                        queue.add(new Integer[]{nx, ny});
                    }
                }
            }
        }
        int max_cnt = 1;
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (max_cnt < visited[i][j]){
                    max_cnt = visited[i][j];
                }
                if (arr[i][j] == 1){
                    cnt++;
                }
            }
        }
        System.out.println(max_cnt + 3);
        System.out.println(cnt);
    }
}
