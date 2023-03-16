package Day6.B1920_수찾기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B1920_수찾기_김예린 {
    static int BinarySearch(int[] n_arr, int target){
        int low = 0;
        int high = n_arr.length - 1;


        while (low <= high) {
            int mid = (low + high) / 2;
            if (n_arr[mid] == target) {
                return 1;
            } else if (n_arr[mid] > target) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int[] n_arr = new int[N];
        st = new StringTokenizer(bf.readLine(), " ");
        for (int i = 0; i < N; i++) {
            n_arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(n_arr);

        st = new StringTokenizer(bf.readLine());
        int M = Integer.parseInt(st.nextToken());
        int[] m_arr = new int[M];
        st = new StringTokenizer(bf.readLine(), " ");
        for (int i = 0; i < M; i++) {
            m_arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < M; i++) {
            System.out.println(BinarySearch(n_arr, m_arr[i]));
        }
    }
}
