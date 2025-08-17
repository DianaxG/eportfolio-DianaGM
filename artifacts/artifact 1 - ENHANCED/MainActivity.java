package com.example.eventtrackingapp_dianagalvez;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import com.google.android.material.textfield.TextInputLayout;
import android.text.TextWatcher;
import android.text.Editable;
import com.example.eventtrackingapp_dianagalvez.TextWatcherAdapter;

public class MainActivity extends AppCompatActivity {

    private EditText usernameEditText;
    private EditText passwordEditText;
    private Button loginButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_login);

        // Keep existing window inset logic
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        initializeUI();
        setupLoginButton();
    }

    private void initializeUI() {
        usernameEditText = findViewById(R.id.username);
        passwordEditText = findViewById(R.id.password);
        loginButton = findViewById(R.id.buttonLogin);

        usernameEditText.addTextChangedListener(new TextWatcherAdapter() {
            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                if (s.length() == 0) {
                    TextInputLayout usernameLayout = findViewById(R.id.usernameLayout);
                    usernameLayout.setError("Username is required");
                } else {
                    TextInputLayout usernameLayout = findViewById(R.id.usernameLayout);
                    usernameLayout.setError(null);
                }
            }
        });

        passwordEditText.addTextChangedListener(new TextWatcherAdapter() {
            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                if (s.length() == 0) {
                    TextInputLayout passwordLayout = findViewById(R.id.passwordLayout);
                    passwordLayout.setError("Password is required");
                } else {
                    TextInputLayout passwordLayout = findViewById(R.id.passwordLayout);
                    passwordLayout.setError(null);
                }
            }
        });
    }


    private void setupLoginButton() {
        loginButton.setOnClickListener(v -> {
            String username = usernameEditText.getText().toString();
            String password = passwordEditText.getText().toString();

            if (LoginHelper.validateCredentials(username, password)) {
                Intent intent = new Intent(this, DashboardActivity.class);
                startActivity(intent);
            } else {
                Toast.makeText(this, "Invalid credentials", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
