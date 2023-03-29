package WS05;

import java.util.ArrayList;
import java.util.List;

public class BankService {
    private List<AccountDto> accountList;

    public BankService() {
        this.accountList = new ArrayList<>();
    }

    public void addAccount(AccountDto account) {
        accountList.add(account);
    }

    public void removeAccount(int accountId) {
        for (AccountDto account : accountList) {
            if (account.getId() == accountId) {
                accountList.remove(account);
            }
        }
    }

    public List<AccountDto> getAccountList() {
        return accountList;
    }

    public double getAccountBalance(int accountId) {
        double balance = 0;
        for (AccountDto account : accountList) {
            if (account.getId() == accountId) {
                balance = account.getBalance();
            }
        }
        return balance;
    }

    public void transfer(int fromAccountId, int toAccountId, double amount) {
        AccountDto fromAccount = null;
        AccountDto toAccount = null;
        for (AccountDto account : accountList) {
            if (account.getId() == fromAccountId) {
                fromAccount = account;
            }
            if (account.getId() == toAccountId) {
                toAccount = account;
            }
        }
        if (fromAccount != null && toAccount != null) {
            if (fromAccount instanceof SavingAccount) {
                SavingAccount fromSavingAccount = (SavingAccount) fromAccount;
                double transferFee = fromSavingAccount.getTransferFee();
                amount += transferFee;
            }
        }
    }
}

