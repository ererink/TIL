package WS05;

public class AccountDto {
    private int id;
    private String number;
    private double balance;
    private int userId;

    public AccountDto(int id, String number, double balance, int userId) {
        this.id = id;
        this.number = number;
        this.balance = balance;
        this.userId = userId;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    @Override
    public String toString() {
        return id + " | " + number + " | " + balance + " | " + userId;
    }
}
