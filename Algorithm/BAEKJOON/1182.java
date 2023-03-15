package Day5.B1182_부분수열의합;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1182_부분수열의합_김예린 {
    static int N, M, cal, cnt;
    static boolean check;
    static int [] arr;
    static boolean [] isSelected;

    static void subset(int num){
        if (num==N){
            cal = 0;
            check = false;
            for (int i=0; i<N; i++){
                if (isSelected[i]){
                    cal += arr[i];
                    check = true;
                }
            }
            if (cal == M && check){
                cnt++;
            }

            return;
        }
        
        isSelected[num] = true;
        subset(num+1);
        isSelected[num] = false;
        subset(num+1);

    }
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        isSelected = new boolean[N];
        arr = new int[N];
        cnt = 0;


        st = new StringTokenizer(bf.readLine(), " ");
        for (int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        subset(0);

        System.out.println(cnt);
    }
}
