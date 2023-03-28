package WS07;

public class SavingAccount extends AccountDto {
    private double transferFee;

    public SavingAccount(int id, String number, int balance, int userId) {
        super(id, number, balance, userId);
        this.transferFee = transferFee;
    }

    public double getTransferFee() {
        return transferFee;
    }

    public void setTransferFee(double transferFee) {
        this.transferFee = transferFee;
    }

}
