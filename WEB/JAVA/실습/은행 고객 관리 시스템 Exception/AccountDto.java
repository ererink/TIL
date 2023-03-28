package WS07;

public class AccountDto implements Comparable<AccountDto>{
    private int accountSeq;
    private String number;
    private int balance;
    private int userId;

    public AccountDto(){}

    public AccountDto(int id, String number, int balance, int userId) {
        this.accountSeq = accountSeq;
        this.number = number;
        this.balance = balance;
        this.userId = userId;
    }

    public int getAccountSeq() {
        return accountSeq;
    }

    public void setAccountSeq(int accountSeq) {
        this.accountSeq = accountSeq;
    }

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public int getBalance() {
        return balance;
    }

    public void setBalance(int balance) {
        this.balance = balance;
    }

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    @Override
    public int compareTo(AccountDto o){
        return (int) (this.balance - o.balance);
    }

    @Override
    public String toString() {
        return "AccountDto{" +
                "accountSeq=" + accountSeq +
                ", number='" + number + '\'' +
                ", balance=" + balance +
                ", userId=" + userId +
                '}';
    }
}
