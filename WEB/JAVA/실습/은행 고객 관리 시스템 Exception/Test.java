package WS07;

public class Test {
    public static void main(String[] args) {

        BankService bankService = new BankServiceImpl();
        System.out.println(bankService.getAccountList());
        System.out.println(bankService.getAccountListSortByBalance());
        System.out.println(bankService.getAccountListSortByUserSeq());

        for (AccountDto accountDto : bankService.getAccountList()) {
            System.out.println(accountDto);
        }
        try {
            System.out.println(bankService.withdraw(665,3, 1000));
        }catch (Exception e){
            System.out.println(e);
        }
    }

}
