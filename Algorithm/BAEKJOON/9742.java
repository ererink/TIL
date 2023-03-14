package Day4.B9742_순열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B9742_순열_김예린 {
    static boolean []  isSelected;
    static int [] selection;
    static String word = "";
    static char[] arr;
    static int N, R, cnt;   // 입력값 정수, 입력값 문자열 길이,

    static void permutation(String word, int r){
        if (r == R){
            cnt++;
            if (cnt == N){
                System.out.print(word + " " + N + " = ");
                for (int i=0; i<R; i++){
                    System.out.print(word.charAt(selection[i]));
                }
                System.out.println();
            }
            return;
        }

        for (int i=0; i < R; i++){
            if (isSelected[i]) continue;
            isSelected[i] = true;
            selection[r] = i;
            permutation(word, r+1);
            isSelected[i] = false;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
//        String input = "";

        while ((word = bf.readLine()) != null && !word.isEmpty()){
            st = new StringTokenizer(word, " ");
            word = st.nextToken().toString();
            N = Integer.parseInt(st.nextToken());
            cnt = 0;
            R = word.length();
            isSelected = new boolean[R];
            selection = new int [R];
            int fac=1;

            for (int i=1; i<=R;i++){
                fac = i*fac;
            }
            if (fac < N){
                System.out.println(word + " " + N + " = " + "No permutation");
            }
            else {
                permutation(word, 0);
            }


        }
    }
}
