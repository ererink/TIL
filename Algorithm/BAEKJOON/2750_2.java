package Day3.B2750_버블정렬;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
public class B2570_버블정렬_김예린 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int [] arr = new int[N];

        for (int i=0; i <N; i++){
            st = new StringTokenizer(bf.readLine());

            int inp = Integer.parseInt(st.nextToken());
            arr[i] = inp;
        }

        for (int i=0; i < N; i++){
            for (int j=1; j < N - i; j++){
                if (arr[j - 1] > arr[j]){
                    int temp = arr[j - 1];
                    arr[j - 1] = arr[j];
                    arr[j] = temp;
                }
                else {
                    continue;
                }
            }

        }
        for (int i=0; i<N; i++){
            System.out.println(arr[i]);
        }
    }
}
