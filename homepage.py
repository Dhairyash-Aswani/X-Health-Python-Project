from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import random

# === Update Time Function ===
def update_time(label):
    now = datetime.now().strftime("%H:%M:%S")
    label.config(text="Current Time: " + now)
    label.after(1000, update_time, label)

# ====== Initialize Window ======
root = Tk()
root.title("X-Health")
root.geometry("1024x768")
root.configure(bg="#E6F2FF")  # Background color: Light Grayish Blue

# ====== Navbar ======
nav_bar = Frame(root, bg="#0A1F44", height=80)  # Primary color: Deep Navy Blue
nav_bar.place(x=0, y=0, width=1024, height=80)

# Logo
logo_path = r"D:\Dhairyash\College\2nd year\sem4\PRP\X-Health(Python Project)\X-Health Logo.jpg"
logo_img = Image.open(logo_path).resize((120, 60), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_img)
logo_label = Label(nav_bar, image=logo_photo, bg="#0A1F44")
logo_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Profile Icon and Menu
profile_icon_path = r"D:\Dhairyash\College\2nd year\sem4\PRP\X-Health(Python Project)\profile_icon.png"
profile_img = Image.open(profile_icon_path).resize((40, 40), Image.LANCZOS)
profile_photo = ImageTk.PhotoImage(profile_img)

def logout_function():
    root.destroy()

def toggle_menu(event):
    try:
        profile_menu.tk_popup(event.x_root, event.y_root)
    finally:
        profile_menu.grab_release()

profile_btn = Button(nav_bar, image=profile_photo, bg="#0A1F44", bd=0, activebackground="#0A1F44")
profile_btn.place(relx=0.95, rely=0.5, anchor=CENTER)
profile_btn.bind("<Button-1>", toggle_menu)

profile_menu = Menu(root, tearoff=0, bg="#E6F2FF", fg="#222222", activebackground="#40E0D0", activeforeground="#0A1F44")
profile_menu.add_command(label="Logout", command=logout_function)

# ====== Main Content Area ======
main_content = Frame(root, bg="#E6F2FF")
main_content.place(x=0, y=80, width=1024, height=688)

# ====== Page Frames ======
frames = {}

def create_page(name):
    frame = Frame(main_content, width=1024, height=688, bg="#E6F2FF")
    frame.pack_propagate(False)
    frame.place(x=0, y=0)
    frames[name] = frame
    return frame

# ====== Page Functions ======

def show_home():
    if "Home" not in frames:
        frame = create_page("Home")

        # Welcome Banner
        welcome_label = Label(
            frame,
            text="Welcome to X-Health!",
            font=("Arial", 36, "bold"),
            bg="#E6F2FF",
            fg="#0A1F44"  # Primary color
        )
        welcome_label.place(relx=0.5, rely=0.15, anchor=CENTER)

        # Live Time
        time_label = Label(frame, text="", font=("Arial", 14), bg="#E6F2FF", fg="#222222")  # Text color
        time_label.place(relx=0.98, rely=0.02, anchor=NE)
        update_time(time_label)

        # Health Tip of the Day
        health_tips = [
            "Drink plenty of water every day!",
            "Take a 5-minute walk every hour.",
            "Eat fruits and vegetables daily.",
            "Sleep at least 7-8 hours a night.",
            "Wash your hands regularly."
        ]

        random_tip = random.choice(health_tips)

        tip_label_title = Label(
            frame,
            text="Today's Health Tip:",
            font=("Arial", 20, "bold"),
            bg="#E6F2FF",
            fg="#3ABEF9"  # Secondary color
        )
        tip_label_title.place(relx=0.5, rely=0.35, anchor=CENTER)

        tip_label = Label(
            frame,
            text=random_tip,
            font=("Arial", 16),
            bg="#E6F2FF",
            fg="#222222",
            wraplength=600,
            justify=CENTER
        )
        tip_label.place(relx=0.5, rely=0.42, anchor=CENTER)

    frames["Home"].tkraise()

def show_book_appointment():
    if "Book Appointment" not in frames:
        frame = create_page("Book Appointment")
        label = Label(frame, text="Book Your Appointment", font=("Arial", 20, "bold"), bg="#E6F2FF", fg="#0A1F44")
        label.place(relx=0.5, rely=0.2, anchor=CENTER)
    frames["Book Appointment"].tkraise()

def show_medical_services():
    if "Medical Services" not in frames:
        frame = create_page("Medical Services")
        label = Label(frame, text="Our Medical Services", font=("Arial", 20, "bold"), bg="#E6F2FF", fg="#0A1F44")
        label.place(relx=0.5, rely=0.3, anchor=CENTER)
    frames["Medical Services"].tkraise()

def show_health_library():
    if "Health Library" not in frames:
        frame = create_page("Health Library")
        label = Label(frame, text="Explore the Health Library", font=("Arial", 20, "bold"), bg="#E6F2FF", fg="#0A1F44")
        label.place(relx=0.5, rely=0.3, anchor=CENTER)
    frames["Health Library"].tkraise()

# ====== Navigation Buttons ======
nav_buttons = [
    ("Home", show_home),
    ("Book Appointment", show_book_appointment),
    ("Medical Services", show_medical_services),
    ("Health Library", show_health_library)
]

x_positions = [50, 200, 600, 750]

def on_enter(e):
    e.widget['background'] = '#3ABEF9'  # Secondary color
    e.widget['foreground'] = '#0A1F44'
    e.widget['cursor'] = 'hand2'

def on_leave(e):
    e.widget['background'] = '#0A1F44'
    e.widget['foreground'] = 'white'
    e.widget['cursor'] = 'arrow'

for i, (text, func) in enumerate(nav_buttons):
    btn = Button(
        nav_bar, text=text, font=("Arial", 12, "bold"),
        bg="#0A1F44", fg="white", bd=0, command=func,
        relief="flat", padx=10, pady=5, activebackground="#40E0D0", activeforeground="#0A1F44"
    )
    btn.place(x=x_positions[i], rely=0.5, anchor=W)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# ====== Start with Home ======
show_home()

# ====== Run App ======
root.mainloop()
