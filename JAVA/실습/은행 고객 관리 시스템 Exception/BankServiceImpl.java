package WS07;

import java.util.Collections;

import java.util.*;

public class BankServiceImpl implements BankService{
    ArrayList<AccountDto> accounts = new ArrayList<>();
    ArrayList<UserDto> users = new ArrayList<>();
    public BankServiceImpl() {

        // 사용자 정보 배열에 저장
        users.add(0, new UserDto(1, "Erin", "eerin@gmail.com", "1234567890", false));
        users.add(1, new UserDto(2, "김예린", "ererink@gmail.com", "010010110101", true));

        // 계좌 정보 배열에 저장
        accounts.add(0, new LoanAccount(20, "0200202021020", 1000, 1));
        accounts.add(0, new LoanAccount(10, "5271752782272", 500, 1));
        accounts.add(0, new LoanAccount(60, "2728737575272", 00, 1));

        accounts.add(0, new SavingAccount(60, "2728737575272", 00, 1));
        accounts.add(0, new SavingAccount(60, "2728737575272", 00, 1));

        accounts.add(0, new InstallAccount(50, "2728737575272", 00, 1));
        accounts.add(0, new InstallAccount(40, "2728737575272", 00, 1));

    }

    @Override
    public ArrayList<AccountDto> getAccountList(int userSeq) {
        ArrayList<AccountDto> list = new ArrayList<>();
        for (AccountDto ac : accounts) {
            if (ac != null && ac.getUserId() == userSeq) {
                list.add(ac);
            }
        }
        return list;
    }

    @Override
    public UserDto getUserDetail(int userSeq) {
        for (UserDto user : users){
            if (user.getUserSeq() == userSeq) {
                return user;
            }
        }

        return null;
    }

    @Override
    public ArrayList<AccountDto> getAccountList() {
        return null;
    }

    @Override
    public ArrayList<AccountDto> getAccountListSortByBalance() {
        ArrayList<AccountDto> sortByAccountList = new ArrayList<>();

        for (AccountDto ac : accounts){
            sortByAccountList.add(ac);
        }
        Collections.sort(sortByAccountList);
        return sortByAccountList;
    }

    @Override
    public ArrayList<AccountDto> getAccountListSortByUserSeq() {
        ArrayList<AccountDto> sortByAccountList = new ArrayList<>();
        for (AccountDto ac : accounts){
            sortByAccountList.add(ac);
        }

        Collections.sort(sortByAccountList, new Comparator<AccountDto>() {
            @Override
            public int compare(AccountDto o1, AccountDto o2) {
                return o1.getAccountSeq() - o2.getAccountSeq();
            }

            @Override
            public boolean equals(Object obj) {
                return false;
            }
        });
        return sortByAccountList;
    }

    @Override
    public AccountDto getUserAccount(int userSeq, int accountSeq) throws UserAccountNotFoundException {
        ArrayList<AccountDto> userAccount = getAccountList(userSeq);
        if (userAccount.size() == 0) {
            throw new UserAccountNotFoundException();
        }
        for (AccountDto ac : userAccount) {
            if (ac.getAccountSeq() == userSeq) {
                return ac;
            }
        }
        throw new UserAccountNotFoundException();
    }
    @Override
    public int withdraw(int userSeq, int accountSeq, int amount) throws BalanceLackException, UserAccountNotFoundException {
        AccountDto ac = getUserAccount(userSeq, accountSeq);
        if (ac.getBalance() < amount){
            throw new BalanceLackException();
        }
        ac.setBalance(ac.getBalance() - amount);
        return ac.getBalance();
    }


}
