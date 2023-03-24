package day03;

public class LoanAccount extends AccountDto {
    private String collateral;

    public LoanAccount(int id, String number, double balance, int userId, String collateral) {
        super(id, number, balance, userId);
        this.collateral = collateral;
    }

    public String getCollateral() {
        return collateral;
    }

    public void setCollateral(String collateral) {
        this.collateral = collateral;
    }

}
