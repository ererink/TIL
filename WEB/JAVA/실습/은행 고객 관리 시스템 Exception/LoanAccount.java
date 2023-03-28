package WS07;

public class LoanAccount extends AccountDto {
    private String mortgage;

    public LoanAccount(int id, String number, int balance, int userId) {
        super(id, number, balance, userId);
        this.mortgage = mortgage;
    }

    public String getMortgage() {
        return mortgage;
    }

    public void setMortgage(String mortgage) {
        this.mortgage = mortgage;
    }
    @Override
    public String toString() {
        return getAccountSeq() + getNumber() + getBalance() + getUserId() + mortgage;
    }
}
