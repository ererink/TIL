package WS06;

import java.util.ArrayList;

public interface BankService {
    ArrayList<AccountDto> getAccountList(int userSeq);

    UserDto getUserDetail(int userSeq);

    ArrayList<AccountDto> getAccountListSortByBalance();

    ArrayList<AccountDto> getAccountListSortByUserSeq();
}