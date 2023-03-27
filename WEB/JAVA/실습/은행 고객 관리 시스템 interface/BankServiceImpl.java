package WS06;

import java.util.Collections;
import java.util.*;

public class BankServiceImpl implements BankService{
    ArrayList<SavingAccount> accounts = new ArrayList<SavingAccount>();
    ArrayList<WS06.UserDto> users = new ArrayList<>();
    public BankServiceImpl() {

        // 사용자 정보 배열에 저장
        users.add(0, new WS06.UserDto(1, "Erin", "eerin@gmail.com", "1234567890", false));
        users.add(1, new UserDto(2, "김예린", "ererink@gmail.com", "010010110101", true));

        // 계좌 정보 배열에 저장
        accounts.add(0, new WS06.LoanAccount(20, "0200202021020", 1000.0, 1));
        accounts.add(0, new WS06.LoanAccount(10, "5271752782272", 50089, 2));
        accounts.add(0, new WS06.LoanAccount(60, "2728737575272", 76000, 3));

        accounts.add(0, new WS06.SavingAccount(60, "2728737575272", 345300, 4));
        accounts.add(0, new WS06.SavingAccount(60, "2728737575272", 6435300, 5));

        accounts.add(0, new WS06.InstallAccount(50, "2728737575272", 232100, 6));
        accounts.add(0, new WS06.InstallAccount(40, "2728737575272", 254200, 7));

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
    public WS06.UserDto getUserDetail(int userSeq) {
        for (UserDto user : users){
            if (user.getId() == userSeq) {
                return user;
            }
        }

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
    public ArrayList<WS06.AccountDto> getAccountListSortByUserSeq() {
        ArrayList<SavingAccount> sortByAccountList = new ArrayList<>();
        for (SavingAccount ac : accounts){
            sortByAccountList.add(ac);
        }

        Collections.sort(sortByAccountList, new Comparator<AccountDto>() {
            @Override
            public int compare(AccountDto o1, AccountDto o2) {
                return o1.getId() - o2.getId();
            }

            @Override
            public boolean equals(Object obj) {
                return false;
            }
        });
        return sortByAccountList;
    }
}