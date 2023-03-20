package Algo_day08;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class B1697_숨바꼭질_김예린 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int [] arr = new int[100001];
        Queue<Integer> queue = new LinkedList<>();

        queue.add(N);

        while (!queue.isEmpty()){
            int x = queue.poll();
            
            if (x == M){
                System.out.println(arr[M]);
                break;
            }

            // 이동
            for (int i: new int[]{x-1, x+1, x*2}) {
                if (0 <= i && i < 100001 && arr[i] == 0){
                    arr[i] = arr[x] + 1;
                    queue.add(i);
                }
            }
        }

    }
}
