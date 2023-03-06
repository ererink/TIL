package day03;

//package com.itskb.ws03.dto;

public class AccountDto {
    private int id;
    private String number;
    private double balance;
    private int userId;

    public AccountDto(int id, String number, double balance, int userId) {
        this.id = id;
        this.number = number;
        this.balance = balance;
        this.userId = userId;
    }
    public int getUserId() {
        return userId;
    }
}
