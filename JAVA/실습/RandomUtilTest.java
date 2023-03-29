package day03;

import day03.RandomUtil;

public class RandomUtilTest {

    public static void main(String[] args) {
        int a = 10;
        int b = 100;
        
        // getRandomInt1 메소드 호출 예시
        int randomInt1 = RandomUtil.getRandomInt1(a, b);
        System.out.println("getRandomInt1 결과: " + randomInt1);
        
        // getRandomInt2 메소드 호출 예시
        int randomInt2 = RandomUtil.getRandomInt2(a, b);
        System.out.println("getRandomInt2 결과: " + randomInt2);
    }

}
