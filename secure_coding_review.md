# Secure Coding Review

## 1. Introduction

This document outlines the process of conducting a secure coding review for a web application developed in **Java** using the Spring Boot framework. The review aims to identify security vulnerabilities and provide recommendations for secure coding practices.

## 2. Choice of Programming Language and Application

- **Programming Language**: Java
- **Application Type**: Spring Boot Web Application

## 3. Sample Code

Below is a simple Spring Boot application that will be reviewed for security vulnerabilities:

```java
package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@SpringBootApplication
@RestController
@RequestMapping("/user")
public class UserApplication {

    private Map<String, String> users = new HashMap<>();

    public static void main(String[] args) {
        SpringApplication.run(UserApplication.class, args);
    }

    @PostMapping
    public String createUser (@RequestParam String username, @RequestParam String password) {
        users.put(username, password); // Storing password in plain text
        return "User  created";
    }
}