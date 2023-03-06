package day03;

import day03.AccountDto;
import day03.UserDto;

//package com.itskb.ws03.service;
//
//import com.itskb.ws03.dto.AccountDto;
//import com.itskb.ws03.dto.UserDto;

public class BankService {
    private final UserDto[] users;
    private final AccountDto[] accounts;

    public BankService() {
        users = new UserDto[10];
        accounts = new AccountDto[5];
        
        // 사용자 정보 배열에 저장 
        users[0] = new UserDto(1, "Erin", "eerin@gmail.com", "1234567890", false);
        users[1] = new UserDto(2, "김예린", "ererink@gmail.com", "010010110101", true);
        // 계좌 정보 배열에 저장 
        accounts[0] = new AccountDto(1, "123456789", 1000.0, 1);
        accounts[1] = new AccountDto(2, "987654321", 500.0, 1);
        accounts[2] = new AccountDto(3, "456789123", 2000.0, 2);    
    }
    
    // 특정 사용자의 계좌목록 출력 
    public AccountDto[] getUserAccounts(int userId) {     // userId 매개변수를 받아서 해당 유저가 가지고 있는 계좌 정보를 담은 AccountDto 배열을 반환
        AccountDto[] userAccounts = new AccountDto[5];    // AccountDto 배열 생성, 각각의 크기는 5로 제한한다.

        int index = 0;
        for (AccountDto account : accounts) {
            if (account != null && account.getUserId() == userId) {	// 계좌를 하나씩 확인하면서 userId와 일치하는 계좌를 userAccounts 배열에 추가
                userAccounts[index++] = account;					// 계좌를 추가할 때마다 index 변수를 증가시켜 해당 계좌를 저장할 배열의 인덱스를 조절
            }
        }
        System.out.print(userAccounts);        
       return userAccounts;
    }
}

