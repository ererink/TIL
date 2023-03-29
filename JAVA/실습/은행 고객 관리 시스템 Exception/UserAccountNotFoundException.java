package WS07;

public class UserAccountNotFoundException extends Exception {
    UserAccountNotFoundException(){
        super("계좌 없음");
    }
}
