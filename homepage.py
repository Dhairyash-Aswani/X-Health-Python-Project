from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import Calendar
from datetime import datetime



# === Add this to the top of your file ===
def update_time(label):
    now = datetime.now().strftime("%H:%M:%S")
    label.config(text="Current Time: " + now)
    label.after(1000, update_time, label)

# ====== Initialize Window ======
root = Tk()
root.title("X-Health")
root.geometry("1024x768")
root.configure(bg="white")

# ====== Navbar ======
nav_bar = Frame(root, bg="white", height=80)
nav_bar.place(x=0, y=0, width=1024, height=80)

logo_path = r"C:\Users\Yasharth\OneDrive\Desktop\Yasharth\Python\\Mini project (Xhealth)\X-Health Logo.jpg"
logo_img = Image.open(logo_path).resize((120, 60), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_img)
logo_label = Label(nav_bar, image=logo_photo, bg="white")
logo_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# ====== Main Content Area ======
main_content = Frame(root)
main_content.place(x=0, y=80, width=1024, height=688)

# ====== Background Image ======
bg_path = r"C:\Users\Yasharth\OneDrive\Desktop\Yasharth\Python\\Mini project (Xhealth)\landing page background.png"
bg_img = Image.open(bg_path).resize((1024, 688), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_img)

# ====== Page Frames ======
frames = {}

def create_page(name):
    frame = Frame(main_content, width=1024, height=688)
    frame.pack_propagate(False)
    frame.place(x=0, y=0)

    bg_label = Label(frame, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    frames[name] = frame
    return frame

# ====== Page Functions ======

def show_home():
    if "Home" not in frames:
        frame = create_page("Home")

        label = Label(frame, text="Welcome to Home", font=("Arial", 24, "bold"), bg="white")
        label.place(relx=0.5, rely=0.3, anchor=CENTER)

        # Time label at top-right
        time_label = Label(frame, text="", font=("Arial", 14), bg="white", fg="black")
        time_label.place(relx=0.98, rely=0.02, anchor=NE)  # Top-right corner
        update_time(time_label)

    frames["Home"].tkraise()

def show_find_hospital():
    if "Find Hospital" not in frames:
        frame = create_page("Find Hospital")
        label = Label(frame, text="Search Hospitals Near You", font=("Arial", 20, "bold"), bg="white")
        label.place(relx=0.5, rely=0.3, anchor=CENTER)
        # You can add search fields, dropdowns, etc. here
    frames["Find Hospital"].tkraise()

def show_medical_services():
    if "Medical Services" not in frames:
        frame = create_page("Medical Services")
        label = Label(frame, text="Our Medical Services", font=("Arial", 20, "bold"), bg="white")
        label.place(relx=0.5, rely=0.3, anchor=CENTER)
        # Add service categories, buttons, etc.
    frames["Medical Services"].tkraise()

def show_health_library():
    if "Health Library" not in frames:
        frame = create_page("Health Library")
        label = Label(frame, text="Explore the Health Library", font=("Arial", 20, "bold"), bg="white")
        label.place(relx=0.5, rely=0.3, anchor=CENTER)
        # Add categories, search bar, articles list, etc.
    frames["Health Library"].tkraise()

# ====== Navigation Buttons ======

nav_buttons = [
    ("Home", show_home),
    ("Find Hospital", show_find_hospital),
    ("Medical Services", show_medical_services),
    ("Health Library", show_health_library)
]

x_positions = [50, 200, 600, 750]

for i, (text, func) in enumerate(nav_buttons):
    btn = Button(nav_bar, text=text, font=("Arial", 12, "bold"), bg="white", fg="black", bd=0, command=func)
    btn.place(x=x_positions[i], rely=0.5, anchor=W)

# ====== Start with Home ======
show_home()

# ====== Run App ======
root.mainloop()
