package JAVA.실습;

public class For04 {

	public static void main(String[] args) {
		int dice1, dice2;

		while (true) {
		    dice1 = (int)(Math.random() * 6) + 1;
		    dice2 = (int)(Math.random() * 6) + 1;
		    
		    if (dice1 + dice2 == 5) {
		        System.out.println("(" + dice1 + ", " + dice2 + ")");
		        System.out.println("(" + dice2 + ", " + dice1 + ")");
		        break;
		    }
		}

	}

}
