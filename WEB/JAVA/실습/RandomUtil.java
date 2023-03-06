package day03;

import java.util.Random;

public class RandomUtil {
    public static int getRandomInt1(int a, int b) {
    	// a와 b 중 작은 수를 min에, 큰 수를 max에 저장
        int min = Math.min(a, b);	
        int max = Math.max(a, b);
        int range = max - min + 1;
        
        // min부터 max까지의 정수 중 랜덤으로 하나 선택하여 반환
        return (int) (Math.random() * range) + min;
    }

    public static int getRandomInt2(int a, int b) {
        // a와 b 중 작은 수를 min에, 큰 수를 max에 저장
        int min = Math.min(a, b);
        int max = Math.max(a, b);
        int range = max - min + 1;
        
        // min부터 max까지의 정수 중 랜덤으로 하나 선택하여 반환
        Random random = new Random();
        return random.nextInt(range) + min;
    }
}

