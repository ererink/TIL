import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();                   // 정수의 개수
        int[] array = new int[N];               // 배열 만들기
        int cnt = 0;                            // 특정한 정수 카운트 변수

        for(int i = 0; i < N; i++) {
            array[i] = sc.nextInt();            // 배열 입력값 받기
        }

        int v= sc.nextInt();                    // 특정한 정수 입력값 받기

        for(int i = 0; i < array.length; i++) {
            if (v == array[i]){                 // 특정한 정수 찾기
                cnt++;                          // cnt + 1
            }
        }

        System.out.println(cnt);


    }
}