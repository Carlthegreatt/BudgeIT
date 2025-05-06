import customtkinter as ctk
from PIL import Image, ImageTk


def popup_animation():
    width, height = 100, 80
    final_width, final_height = 400, 500
    step = 100

    # Create the pop-up window
    popup = ctk.CTkToplevel(app)
    popup.overrideredirect(False)  # Keep window decorations
    popup.transient(app)  # Stay on top of main window
    popup.grab_set()  # Make modal: block interaction with main window
    

    
    # Center the popup relative to the main window
    main_x = app.winfo_rootx()
    main_y = app.winfo_rooty()
    main_width = app.winfo_width()
    main_height = app.winfo_height()
    start_x = main_x + (main_width // 2) - (width // 2)
    start_y = main_y + (main_height // 2) - (height // 2)
    popup.geometry(f"{width}x{height}+{start_x}+{start_y}")

    popup.title("Login")

    # background_image = ctk.CTkImage(light_image=Image.open('bg.jpg'),dark_image=Image.open('bg.jpg'),size=(400, 500))
    # background_label = ctk.CTkLabel(popup, image=background_image)
    # background_label = ctk.CTkLabel(popup, image=background_image)
    
   
    main_frame = ctk.CTkFrame(popup, fg_color="#252B3B")  # Frame background color
    main_frame.pack(expand=True, fill="both")

    frame = ctk.CTkFrame(master=main_frame, fg_color='#0D1826', corner_radius=20    ) 
    label = ctk.CTkLabel(master=frame, text="Login to BudgeIT",font=ctk.CTkFont(family="Helvetica", size=20, weight="bold") )
   

    user_entry= ctk.CTkEntry(master=frame,fg_color='#12233B' ,placeholder_text="Username", corner_radius=15,height=40 ,width=250, border_width=0) 
    user_pass= ctk.CTkEntry(master=frame,fg_color='#12233B',placeholder_text="Password",show="*" ,corner_radius=15,height=40,width=250, border_width=0) 
    button = ctk.CTkButton(master=frame,fg_color='#4628A1',text='Login',hover_color='#252B3B', corner_radius=30,height=40,width=250, border_width=0) 
    

    def grow():
        nonlocal width, height, start_x, start_y
        if width < final_width or height < final_height:
            width = min(width + step, final_width)
            height = min(height + step, final_height)
            # Update position to stay centered during growth
            x = main_x + (main_width // 2) - (width // 2)
            y = main_y + (main_height // 2) - (height // 2)
            popup.geometry(f"{width}x{height}+{x}+{y}")
            popup.after(30, grow)
        else:
            
            # background_label.place(relwidth=1, relheight=1)
            label.pack(pady=20) 
            frame.pack(pady=40,padx=40,fill='both',expand=True) 
            label.pack(pady=30,padx=10) 
            user_entry.pack(pady=12,padx=10) 
            user_pass.pack(pady=12,padx=10) 
            button.pack(pady=12,padx=10) 
    grow()



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x400")
app.title("Main Window")
  # or "light"
button = ctk.CTkButton(app, fg_color="#252B3B", text="Click Me")
button.pack(pady=2)
btn = ctk.CTkButton(app,  text="Get Started", command=popup_animation)
btn.pack(pady=100)

app.mainloop()
