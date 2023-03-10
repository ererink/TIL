package Day2.B1874_스택수열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class B1874_스택수열_김예린 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        Stack<Integer> stack = new Stack<>();
        StringBuilder check = new StringBuilder();  // for문을 사용하지 않아도 출력하기 편리함
        int start = 0;


        // N이 0이 될 때 까지 == N번 반복
        while (N --> 0)  {
            st = new StringTokenizer(bf.readLine());
            int c = Integer.parseInt((st.nextToken()));
            if (c > start){     // 입력값 c가 start보다 크다면 0~c 까지의 값을 stack에 넣어주어야 함
                for (int i = start + 1; i<=c; i++){
                    stack.push(i);
                    check.append("+").append("\n");
                }
                start = c;  // 다음 입력값을 기준으로 stack에 넣어줘야 하므로 start를 c의 값으로 할당

            }
            else if (stack.peek() != c){    // 입력값 c가 start보다 작은 것은 수열이 형성되지 않으므로 stack의 맨 오른쪽 값과 같은지 확인
                System.out.println("NO");
                return;
            }
            stack.pop();
            check.append("-").append("\n");

        }
        System.out.println(check);
        
    }
}
