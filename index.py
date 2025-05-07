import customtkinter as ctk


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

    def register_window_style(self):
        reg = super().create_window()
        reg.transient(app)

        self._build_ui(
            reg,
            "Create Account",
            "Join BudgeIT today",
            "Already have an account? Login here",
            lambda: (
                reg.destroy(),
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

        for placeholder in ["Username", "Password", "Confirm Password"]:
            ctk.CTkEntry(
                master=frame,
                fg_color="#12233B",
                placeholder_text=placeholder,
                show="*" if "Password" in placeholder else "",
                corner_radius=15,
                height=40,
                width=250,
            ).pack(pady=12)

        ctk.CTkButton(
            master=frame,
            fg_color="#4628A1",
            text="Register",
            hover_color="#252B3B",
            corner_radius=30,
            height=40,
            width=250,
        ).pack(pady=12)

        link = ctk.CTkLabel(
            master=frame,
            text=link_text,
            text_color="white",
            font=ctk.CTkFont(size=10),
            cursor="hand2",
        )
        link.pack()
        link.bind("<Button-1>", lambda e: link_action())


class LoginWindow(Window):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)

    def login_window_style(self):
        log = super().create_window()
        log.transient(app)

        self._build_ui(
            log,
            "Welcome Back",
            "Please sign in to continue",
            "Don't have an account? Register here",
            lambda: (
                log.destroy(),
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

        for placeholder in ["Enter your username", "Enter your password"]:
            ctk.CTkEntry(
                master=frame,
                fg_color="#12233B",
                placeholder_text=placeholder,
                show="*" if "Password" in placeholder else "",
                corner_radius=15,
                height=40,
                width=250,
            ).pack(pady=12)

        ctk.CTkButton(
            master=frame,
            fg_color="#4628A1",
            text="Login",
            hover_color="#252B3B",
            corner_radius=30,
            height=40,
            width=250,
        ).pack(pady=12)

        link = ctk.CTkLabel(
            master=frame,
            text=link_text,
            text_color="white",
            font=ctk.CTkFont(size=10),
            cursor="hand2",
        )
        link.pack()
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
