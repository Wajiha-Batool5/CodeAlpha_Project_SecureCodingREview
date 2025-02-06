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