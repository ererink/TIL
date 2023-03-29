package day03;

//package com.itskb.ws03.dto;

public class UserDto {
    int id;
    String name;
    String email;
    String phoneNumber;
    boolean isActive;

    public UserDto(int id, String name, String email, String phoneNumber, boolean isActive) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.phoneNumber = phoneNumber;
        this.isActive = isActive;
    }

}    