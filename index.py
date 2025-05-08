import customtkinter as ctk
import json
import os
from tkinter import messagebox


class Window:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

    def create_window(self):
        window = ctk.CTkToplevel()
        window.geometry(f"{self.width}x{self.height}")
        window.title(self.title)
        window.resizable(False, False)
        window.configure(fg_color="#252B3B")
        return window


class RegisterWindow(Window):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)
        self.username_entry = None
        self.password_entry = None
        self.confirm_password_entry = None
        self.message_label = None
        self.users_file = "users.json"
        self._load_users()

    def _load_users(self):
        if os.path.exists(self.users_file):
            with open(self.users_file, "r") as f:
                self.users = json.load(f)
        else:
            self.users = {}
            self._save_users()

    def _save_users(self):
        with open(self.users_file, "w") as f:
            json.dump(self.users, f, indent=4)

    def _handle_register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not username or not password or not confirm_password:
            self.message_label.configure(
                text="Please fill in all fields", text_color="#FF0000"
            )
            return

        if password != confirm_password:
            self.message_label.configure(
                text="Passwords do not match", text_color="#FF0000"
            )
            return

        if username in self.users:
            self.message_label.configure(
                text="Username already exists", text_color="#FF0000"
            )
            return

        # Store the new user
        self.users[username] = {"password": password}
        self._save_users()
        self.message_label.configure(
            text="Registration successful! Please login.", text_color="#00FF00"
        )
        self.window.after(
            2000,
            lambda: (
                self.window.destroy(),
                LoginWindow("Login", 400, 450).login_window_style(),
            ),
        )

    def register_window_style(self):
        self.window = super().create_window()
        self.window.transient(app)
        self.window.grab_set()

        self._build_ui(
            self.window,
            "Create Account",
            "Join BudgeIT today",
            "Already have an account? Login here",
            lambda: (
                self.window.destroy(),
                LoginWindow("Login", 400, 450).login_window_style(),
            ),
        )

    def _build_ui(self, window, header_text, sub_header_text, link_text, link_action):
        main_frame = ctk.CTkFrame(window, fg_color="#252B3B")
        main_frame.pack(expand=True, fill="both")

        frame = ctk.CTkFrame(master=main_frame, fg_color="#0D1826", corner_radius=20)
        frame.pack(pady=40, padx=40, fill="both", expand=True)

        ctk.CTkLabel(
            master=frame,
            text=header_text,
            font=ctk.CTkFont(family="Helvetica", size=30, weight="bold"),
        ).pack(pady=(25, 0))

        ctk.CTkLabel(
            master=frame,
            text=sub_header_text,
            font=ctk.CTkFont(family="Helvetica", size=14),
            text_color="#A6ADC8",
        ).pack(pady=(5, 10))

        # Username entry
        self.username_entry = ctk.CTkEntry(
            master=frame,
            fg_color="#12233B",
            placeholder_text="Username",
            corner_radius=15,
            height=40,
            width=250,
        )
        self.username_entry.pack(pady=12)

        # Password entry
        self.password_entry = ctk.CTkEntry(
            master=frame,
            fg_color="#12233B",
            placeholder_text="Password",
            show="*",
            corner_radius=15,
            height=40,
            width=250,
        )
        self.password_entry.pack(pady=12)

        # Confirm Password entry
        self.confirm_password_entry = ctk.CTkEntry(
            master=frame,
            fg_color="#12233B",
            placeholder_text="Confirm Password",
            show="*",
            corner_radius=15,
            height=40,
            width=250,
        )
        self.confirm_password_entry.pack(pady=(12, 5))

        # Message label for validation feedback
        self.message_label = ctk.CTkLabel(
            master=frame,
            text="",
            font=ctk.CTkFont(family="Helvetica", size=12),
            text_color="#FF0000",
        )
        self.message_label.pack(pady=(0, 5))

        # Register button
        ctk.CTkButton(
            master=frame,
            fg_color="#4628A1",
            text="Register",
            hover_color="#252B3B",
            corner_radius=30,
            height=40,
            width=250,
            command=self._handle_register,
        ).pack(pady=(0, 12))

        link = ctk.CTkLabel(
            master=frame,
            text=link_text,
            text_color="white",
            font=ctk.CTkFont(size=10),
            cursor="hand2",
        )
        link.pack(pady=(0, 20))
        link.bind("<Button-1>", lambda e: link_action())


class LoginWindow(Window):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)
        self.username_entry = None
        self.password_entry = None
        self.message_label = None
        self.users_file = "users.json"
        self._load_users()

    def _load_users(self):
        if os.path.exists(self.users_file):
            with open(self.users_file, "r") as f:
                self.users = json.load(f)
        else:
            self.users = {}
            self._save_users()

    def _save_users(self):
        with open(self.users_file, "w") as f:
            json.dump(self.users, f, indent=4)

    def _authenticate_user(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            return True
        return False

    def _handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            self.message_label.configure(
                text="Please fill in all fields", text_color="#FF0000"
            )
            return

        if self._authenticate_user(username, password):
            self.message_label.configure(text="Login successful!", text_color="#00FF00")
            self.window.after(
                2000,
                lambda: (
                    self.window.destroy(),
                    # Here you can add code to open the main application window
                ),
            )
        else:
            self.message_label.configure(
                text="Invalid username or password", text_color="#FF0000"
            )

    def login_window_style(self):
        self.window = super().create_window()
        self.window.transient(app)
        self.window.grab_set()

        self._build_ui(
            self.window,
            "Welcome Back",
            "Please sign in to continue",
            "Don't have an account? Register here",
            lambda: (
                self.window.destroy(),
                RegisterWindow("Register", 400, 500).register_window_style(),
            ),
        )

    def _build_ui(self, window, header_text, sub_header_text, link_text, link_action):
        main_frame = ctk.CTkFrame(window, fg_color="#252B3B")
        main_frame.pack(expand=True, fill="both")

        frame = ctk.CTkFrame(master=main_frame, fg_color="#0D1826", corner_radius=20)
        frame.pack(pady=40, padx=40, fill="both", expand=True)

        ctk.CTkLabel(
            master=frame,
            text=header_text,
            font=ctk.CTkFont(family="Helvetica", size=30, weight="bold"),
        ).pack(pady=(30, 0))

        ctk.CTkLabel(
            master=frame,
            text=sub_header_text,
            font=ctk.CTkFont(family="Helvetica", size=14),
            text_color="#A6ADC8",
        ).pack(pady=(5, 10))

        # Username entry
        self.username_entry = ctk.CTkEntry(
            master=frame,
            fg_color="#12233B",
            placeholder_text="Enter your username",
            corner_radius=15,
            height=40,
            width=250,
        )
        self.username_entry.pack(pady=12)

        # Password entry
        self.password_entry = ctk.CTkEntry(
            master=frame,
            fg_color="#12233B",
            placeholder_text="Enter your password",
            show="*",
            corner_radius=15,
            height=40,
            width=250,
        )
        self.password_entry.pack(pady=(12, 5))

        # Message label for validation feedback
        self.message_label = ctk.CTkLabel(
            master=frame,
            text="",
            font=ctk.CTkFont(family="Helvetica", size=12),
            text_color="#FF0000",
        )
        self.message_label.pack(pady=(0, 5))

        # Login button
        ctk.CTkButton(
            master=frame,
            fg_color="#4628A1",
            text="Login",
            hover_color="#252B3B",
            corner_radius=30,
            height=40,
            width=250,
            command=self._handle_login,
        ).pack(pady=(0, 12))

        link = ctk.CTkLabel(
            master=frame,
            text=link_text,
            text_color="white",
            font=ctk.CTkFont(size=10),
            cursor="hand2",
        )
        link.pack(pady=(0, 20))
        link.bind("<Button-1>", lambda e: link_action())


class MainWindow(Window):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)
        self.user_login = RegisterWindow("Register", 400, 500)

    def create_main_window(self):
        app = ctk.CTk()
        app.geometry(f"{self.width}x{self.height}")
        app.title(self.title)
        app.configure(fg_color="#252B3B")

        # Create main container
        main_container = ctk.CTkFrame(app, fg_color="#252B3B")
        main_container.pack(expand=True, fill="both", padx=40, pady=40)

        # Left side content
        left_frame = ctk.CTkFrame(main_container, fg_color="#0D1826", corner_radius=20)
        left_frame.pack(side="left", expand=True, fill="both", padx=(0, 20))

        # Logo and title
        ctk.CTkLabel(
            left_frame,
            text="BudgeIT",
            font=ctk.CTkFont(family="Helvetica", size=48, weight="bold"),
        ).pack(pady=(60, 10))

        ctk.CTkLabel(
            left_frame,
            text="Smart Budget Management",
            font=ctk.CTkFont(family="Helvetica", size=18),
            text_color="#A6ADC8",
        ).pack(pady=(0, 40))

        # Features list
        features = [
            "📊 Track your expenses in real-time",
            "💰 Set and manage your budget goals",
            "📈 Visualize your spending patterns",
            "🔔 Get smart notifications and alerts",
        ]

        for feature in features:
            ctk.CTkLabel(
                left_frame,
                text=feature,
                font=ctk.CTkFont(family="Helvetica", size=14),
                text_color="#FFFFFF",
            ).pack(pady=8, anchor="w", padx=40)

        # Right side content
        right_frame = ctk.CTkFrame(main_container, fg_color="#0D1826", corner_radius=20)
        right_frame.pack(side="right", expand=True, fill="both")

        # Welcome message
        ctk.CTkLabel(
            right_frame,
            text="Welcome to BudgeIT",
            font=ctk.CTkFont(family="Helvetica", size=32, weight="bold"),
        ).pack(pady=(60, 10))

        ctk.CTkLabel(
            right_frame,
            text="Your personal finance companion",
            font=ctk.CTkFont(family="Helvetica", size=16),
            text_color="#A6ADC8",
        ).pack(pady=(0, 40))

        # Get Started button with modern styling
        get_started_btn = ctk.CTkButton(
            right_frame,
            text="Get Started",
            font=ctk.CTkFont(family="Helvetica", size=16, weight="bold"),
            fg_color="#4628A1",
            hover_color="#5B3BBF",
            corner_radius=30,
            height=50,
            width=200,
            command=self.user_login.register_window_style,
        )
        get_started_btn.pack(pady=20)

        # Additional info
        ctk.CTkLabel(
            right_frame,
            text="Join thousands of users managing their finances smarter",
            font=ctk.CTkFont(family="Helvetica", size=12),
            text_color="#A6ADC8",
        ).pack(pady=(20, 0))

        return app


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

main_window = MainWindow("BudgeIT - Smart Budget Management", 800, 600)
app = main_window.create_main_window()
app.mainloop()
