from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
import random

# Storage for appointments
appointments = []

# === Update Time Function ===
def update_time(label):
    now = datetime.now().strftime("%H:%M:%S")
    label.config(text="Current Time: " + now)
    label.after(1000, update_time, label)

# ====== Initialize Window ======
root = Tk()
root.title("X-Health")
root.geometry("1024x768")
root.configure(bg="#E6F2FF")

# ====== Navbar ======
nav_bar = Frame(root, bg="#0A1F44", height=80)
nav_bar.place(x=0, y=0, width=1024, height=80)

# Logo
logo_path = r"D:\Dhairyash\\College\2nd year\sem4\PRP\X-Health(Python Project)\X-Health Logo.jpg"
logo_img = Image.open(logo_path).resize((120, 60), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_img)
logo_label = Label(nav_bar, image=logo_photo, bg="#0A1F44")
logo_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Profile Icon and Menu
profile_icon_path = r"D:\Dhairyash\\College\2nd year\sem4\PRP\X-Health(Python Project)\profile_icon.png"
profile_img = Image.open(profile_icon_path).resize((40, 40), Image.LANCZOS)
profile_photo = ImageTk.PhotoImage(profile_img)

def logout_function():
    root.destroy()   # Destroy the homepage window
    import X_health_loginpage  # Import the login page file
    X_health_loginpage.open_login_window()

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

# ====== Book Appointment Logic ======
def book_appointment(category, doctor):
    appointment = {
        "category": category,
        "doctor": doctor,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    appointments.append(appointment)
    messagebox.showinfo("Appointment Booked", f"Appointment booked with Dr. {doctor}\nSpecialty: {category}\nTime: {appointment['time']}")
    update_history_box()

# ====== Doctor Info Functions ======
def show_doctor_info(frame, category, doctor_name):
    info_label = Label(frame, text=f"Dr. {doctor_name}\nSpecialty: {category}\nExperience: 10 years\nRating: 4.8/5", font=("Arial", 14), bg="#E6F2FF", justify=LEFT)
    info_label.pack(pady=10)
    book_btn = Button(frame, text="Book Appointment", bg="#3ABEF9", fg="white", font=("Arial", 12), command=lambda: book_appointment(category, doctor_name))
    book_btn.pack(pady=5)

def handle_category_selection(category):
    if "Doctor Info" in frames:
        frames["Doctor Info"].destroy()
    frame = create_page("Doctor Info")

    title = Label(frame, text=f"Available {category}s", font=("Arial", 20, "bold"), bg="#E6F2FF", fg="#0A1F44")
    title.pack(pady=10)

    doctors = {
        "General Physician": ["Amit Sharma"],
        "Cardiologist": ["Neha Verma"],
        "Dermatologist": ["Ravi Kapoor"],
        "Pediatrician": ["Sunita Rao"],
        "Neurologist": ["Karan Malhotra"],
        "Orthopedic": ["Divya Nair"]
    }
    for doc in doctors.get(category, []):
        show_doctor_info(frame, category, doc)

# ====== Page Functions ======
def show_home():
    if "Home" not in frames:
        frame = create_page("Home")

        welcome_label = Label(frame, text="Welcome to X-Health!", font=("Arial", 36, "bold"), bg="#E6F2FF", fg="#0A1F44")
        welcome_label.place(relx=0.5, rely=0.15, anchor=CENTER)

        time_label = Label(frame, text="", font=("Arial", 14), bg="#E6F2FF", fg="#222222")
        time_label.place(relx=0.98, rely=0.02, anchor=NE)
        update_time(time_label)

        health_tips = [
        "Drink plenty of water every day!",
        "Take a 5-minute walk every hour.",
        "Eat fruits and vegetables daily.",
        "Sleep at least 7-8 hours a night.",
        "Wash your hands regularly.",
        "Limit your screen time and rest your eyes.",
        "Stretch your body for 5 minutes every morning.",
        "Practice deep breathing to reduce stress.",
        "Cut down on sugary drinks and junk food.",
        "Include protein in every meal.",
        "Wear sunscreen when going outdoors.",
        "Take short breaks while studying or working.",
        "Keep a good posture while sitting.",        
        "Meditate for 10 minutes a day.",
        "Keep your surroundings clean.",
        "Avoid smoking and drinking alcohol.",        
        ]
        random_tip = random.choice(health_tips)

        tip_label_title = Label(frame, text="Today's Health Tip:", font=("Arial", 20, "bold"), bg="#E6F2FF", fg="#3ABEF9")
        tip_label_title.place(relx=0.5, rely=0.35, anchor=CENTER)

        tip_label = Label(frame, text=random_tip, font=("Arial", 16), bg="#E6F2FF", fg="#222222", wraplength=600, justify=CENTER)
        tip_label.place(relx=0.5, rely=0.42, anchor=CENTER)

    frames["Home"].tkraise()

history_box = None

def update_history_box():
    if history_box:
        history_box.delete(1.0, END)
        for appt in appointments:
            history_box.insert(END, f"{appt['time']} - {appt['doctor']} ({appt['category']})\n")

def show_book_appointment():
    global history_box

    if "Book Appointment" not in frames:
        frame = create_page("Book Appointment")

        label = Label(frame, text="Book Your Appointment", font=("Arial", 20, "bold"), bg="#E6F2FF", fg="#0A1F44")
        label.place(relx=0.5, rely=0.05, anchor=CENTER)

        instruction = Label(frame, text="Select the type of doctor you want to book an appointment with:", font=("Arial", 14), bg="#E6F2FF", fg="#222222")
        instruction.place(relx=0.5, rely=0.12, anchor=CENTER)

        categories = [
            "General Physician", "Cardiologist", "Dermatologist",
            "Pediatrician", "Neurologist", "Orthopedic"
        ]

        for i, category in enumerate(categories):
            btn = Button(
                frame,
                text=category,
                font=("Arial", 14),
                bg="#3ABEF9",
                fg="white",
                width=20,
                height=2,
                bd=0,
                activebackground="#0A1F44",
                activeforeground="white",
                command=lambda c=category: handle_category_selection(c)
            )
            row = i // 3
            col = i % 3
            btn.place(relx=0.2 + col * 0.3, rely=0.25 + row * 0.15, anchor=CENTER)

        # Appointment History Section
        history_title = Label(frame, text="Your Appointment History", font=("Arial", 16, "bold"), bg="#E6F2FF", fg="#0A1F44")
        history_title.place(relx=0.5, rely=0.65, anchor=CENTER)

        history_box = Text(frame, height=8, width=80, font=("Arial", 12))
        history_box.place(relx=0.5, rely=0.80, anchor=CENTER)

        update_history_box()

    frames["Book Appointment"].tkraise()

def show_medical_services():
        if "Health Library" not in frames:
            frame = create_page("Medical Services")
            
            import medical_service
            medical_service.load_medical_services(frame)

            frames["Medical Services"] = frame 

        frames["Medical Services"].tkraise()

def show_health_library():
    if "Health Library" not in frames:
        frame = create_page("Health Library")

        import health_library
        health_library.load_health_library(frame)

        frames["Health Library"] = frame  # <-- important

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
    e.widget['background'] = '#3ABEF9'
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
