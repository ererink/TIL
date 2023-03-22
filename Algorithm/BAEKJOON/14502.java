package Day9.B14502_연구소;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class B14502_연구소_김예린 {
    static int N, M, wall, cnt, answer;
    static int [][] arr, visited;
    static ArrayList<Integer[]> safe = new ArrayList<>();
    static ArrayList<Integer[]> virus = new ArrayList<>();

    static Integer [] dx = {0, 0, -1, 1};
    static Integer [] dy = {1, -1, 0, 0};
    static int infect(){
        Queue<Integer[]> queue = new LinkedList<>();
        visited = new int[N][M];
        cnt = 0;

        for (Integer[] vir : virus) {
            queue.add(vir);
            cnt++;
        }
        while (!queue.isEmpty()){
            Integer[] x = queue.poll();

            for (int i = 0; i < 4; i++) {
                Integer nx = x[0] + dx[i];
                Integer ny = x[1] + dy[i];

                if (0 <= nx && nx < N && 0<= ny && ny < M){
                    if (arr[nx][ny] == 0 && visited[nx][ny] == 0){
                        visited[nx][ny] = 2;
                        queue.add(new Integer[]{nx, ny});
                        cnt++;
                    }

                }
            }
        }
        // 전체 영역 - 입력값으로 받은 벽 - 새로운 벽 - 바이러스 수 ㄴ
        return N*M - wall - 3 - cnt;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        answer = 0;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(bf.readLine(), " ");
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        wall = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                // 바이러스 찾기
                if (arr[i][j] == 2){
                    virus.add(new Integer[]{i, j});
                }
                // 벽 찾기
                else if (arr[i][j] == 1){
                    wall++;
                }
                // 안전영역 찾기
                else if (arr[i][j] == 0){
                    safe.add(new Integer[]{i, j});
                }
            }
        }

        // 3개 벽 세우기
        for (int i = 0; i < safe.size()-2; i++) {
            arr[safe.get(i)[0]][safe.get(i)[1]] = 1;
            for (int j = i+1; j < safe.size()-1; j++) {
                arr[safe.get(j)[0]][safe.get(j)[1]] = 1;
                for (int k = j+1; k < safe.size(); k++) {
                    arr[safe.get(k)[0]][safe.get(k)[1]] = 1;
                    // 바이러스 증식
                    answer = Math.max(infect(),answer);
                    // 벽 복귀
                    arr[safe.get(k)[0]][safe.get(k)[1]] = 0;
                }
                arr[safe.get(j)[0]][safe.get(j)[1]] = 0;
            }
            arr[safe.get(i)[0]][safe.get(i)[1]] = 0;
        }


        System.out.println(answer);

    }
}
