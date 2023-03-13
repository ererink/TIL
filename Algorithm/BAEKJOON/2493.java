package Day2.B2493_탑;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class B2493_탑_김예린 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        Stack <int[]> stack = new Stack<>();

        st = new StringTokenizer(bf.readLine(), " ");
        for (int i = 1; i <= N; i++){   // 차례대로 입력값 받기
            int h = Integer.parseInt(st.nextToken());

            while (!stack.isEmpty()){
                if (stack.peek()[1] >= h){   // 현재 값과 스택에 있는 값 비교
                    System.out.print(stack.peek()[0] + " ");
                    break;
                }
                stack.pop();        // 큰 수를 만날 때 까지 계속 pop
            }
            if (stack.isEmpty()){
                System.out.print("0 ");     // 왼쪽에 있는 큰수를 계속해서 만나지 못할 경우 0 출력
            }
            stack.push(new int[] {i, h});   // 한 쌍의 리스트로 push [[6, 0], [9, 0], ...]
        }
    }
}
