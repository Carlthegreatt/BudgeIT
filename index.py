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
            "Welcome to BudgeIT",
            "Already have an account? Login here",
            lambda: (
                reg.destroy(),
                LoginWindow("Login", 400, 500).login_window_style(),
            ),
        )

    def _build_ui(self, window, header_text, link_text, link_action):
        main_frame = ctk.CTkFrame(window, fg_color="#252B3B")
        main_frame.pack(expand=True, fill="both")

        frame = ctk.CTkFrame(master=main_frame, fg_color="#0D1826", corner_radius=20)
        frame.pack(pady=40, padx=40, fill="both", expand=True)

        ctk.CTkLabel(
            master=frame,
            text=header_text,
            font=ctk.CTkFont(family="Helvetica", size=20, weight="bold"),
        ).pack(pady=20)

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
            "Login to BudgeIT",
            "Don't have an account? Register here",
            lambda: (
                log.destroy(),
                RegisterWindow("Register", 400, 500).register_window_style(),
            ),
        )

    def _build_ui(self, window, header_text, link_text, link_action):
        main_frame = ctk.CTkFrame(window, fg_color="#252B3B")
        main_frame.pack(expand=True, fill="both")

        frame = ctk.CTkFrame(master=main_frame, fg_color="#0D1826", corner_radius=20)
        frame.pack(pady=40, padx=40, fill="both", expand=True)

        ctk.CTkLabel(
            master=frame,
            text=header_text,
            font=ctk.CTkFont(family="Helvetica", size=20, weight="bold"),
        ).pack(pady=20)

        for placeholder in ["Username", "Password"]:
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


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x400")
app.title("Main Window")

user_login = LoginWindow("Login", 400, 500)
ctk.CTkButton(app, text="Get Started", command=user_login.login_window_style).pack(
    pady=100
)

app.mainloop()
