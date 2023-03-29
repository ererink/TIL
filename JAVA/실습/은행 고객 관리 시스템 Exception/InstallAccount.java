package WS07;

public class InstallAccount extends AccountDto {
    private int period;
    private double amount;

    public InstallAccount(int id, String number, int balance, int userId) {
        super(id, number, balance, userId);
        this.period = period;
        this.amount = amount;
    }

    public int getPeriod() {
        return period;
    }

    public void setPeriod(int period) {
        this.period = period;
    }

    public double getAmount() {
        return amount;
    }

    public void setAmount(double amount) {
        this.amount = amount;
    }
}
