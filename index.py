import customtkinter as ctk
from PIL import Image, ImageTk


def register_window(old_window):
    old_window.destroy()
    reg = ctk.CTkToplevel(app)
    reg.geometry("400x500")
    reg.transient(app)
    reg.title("New Window")
    ctk.CTkLabel(reg, text="This is a new window!", font=ctk.CTkFont(size=15)).pack(
        pady=40
    )

    reg.title("Login")


def login_window():
    log = ctk.CTkToplevel(app)
    log.geometry("400x500")
    log.transient(app)  # Stay on top of main window
    log.title("Login")

    # background_image = ctk.CTkImage(light_image=Image.open('bg.jpg'),dark_image=Image.open('bg.jpg'),size=(400, 500))
    # background_label = ctk.CTkLabel(log, image=background_image)
    # background_label = ctk.CTkLabel(log, image=background_image)

    main_frame = ctk.CTkFrame(log, fg_color="#252B3B")  # Frame background color
    main_frame.pack(expand=True, fill="both")

    frame = ctk.CTkFrame(master=main_frame, fg_color="#0D1826", corner_radius=20)
    label = ctk.CTkLabel(
        master=frame,
        text="Login to BudgeIT",
        font=ctk.CTkFont(family="Helvetica", size=20, weight="bold"),
    )
    user_entry = ctk.CTkEntry(
        master=frame,
        fg_color="#12233B",
        placeholder_text="Username",
        corner_radius=15,
        height=40,
        width=250,
        border_width=0,
    )
    user_pass = ctk.CTkEntry(
        master=frame,
        fg_color="#12233B",
        placeholder_text="Password",
        show="*",
        corner_radius=15,
        height=40,
        width=250,
        border_width=0,
    )
    button = ctk.CTkButton(
        master=frame,
        fg_color="#4628A1",
        text="Login",
        hover_color="#252B3B",
        corner_radius=30,
        height=40,
        width=250,
        border_width=0,
    )
    link = ctk.CTkLabel(
        master=frame,
        text="Don't have an account? Register here",
        text_color="white",
        font=ctk.CTkFont(underline=True, size=10),
        cursor="hand2",
    )

    label.pack(pady=20)
    frame.pack(pady=40, padx=40, fill="both", expand=True)
    label.pack(pady=30, padx=10)
    user_entry.pack(pady=12, padx=10)
    user_pass.pack(pady=12, padx=10)
    button.pack(pady=12, padx=10)
    link.pack()
    link.bind("<Button-1>", lambda e: register_window(log))


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x400")
app.title("Main Window")

btn = ctk.CTkButton(app, text="Get Started", command=login_window)
btn.pack(pady=100)

app.mainloop()
