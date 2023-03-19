package Algorithm;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.LinkedList;
import java.util.StringTokenizer;
public class B2178_미로찾기_김예린 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int [][] arr = new int[N][M];
        int [][] visited = new int[N][M];
        Queue<int[]> queue = new LinkedList<>();

        for (int i = 0; i < N; i++) {
            String line = bf.readLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = line.charAt(j) - '0';
            }
        }

        int [] dx = {0, 0, -1, 1};
        int [] dy = {1, -1, 0, 0};


        queue.add(new int[] {0, 0});
        visited[0][0] = 1;

        while (!queue.isEmpty()){
            int[] ele = queue.poll();
            int x = ele[0];
            int y = ele[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < N && 0<= ny && ny <M){
                    if (arr[nx][ny] == 1 && visited[nx][ny] == 0){
                        visited[nx][ny] = visited[x][y] + 1;
                        queue.add(new int [] {nx, ny});
                    }
                }
            }
        }
        System.out.println(visited[N-1][M-1]);
    }
}
