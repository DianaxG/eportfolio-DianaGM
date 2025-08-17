package com.example.eventtrackingapp_dianagalvez;

public class LoginHelper {
    public static boolean validateCredentials(String username, String password) {
        return username.equals("admin") && password.equals("admin123");
    }
}
