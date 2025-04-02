from tkinter import *
from PIL import Image, ImageTk

# Function to switch between frames
def show_frame(frame):
    frame.tkraise()
    if frame == frames["home"]:
        back_button.pack_forget()
    else:
        back_button.pack(side=RIGHT, padx=20, pady=20)

# Initialize main window
root = Tk()
root.title("X-Health")
root.geometry("1024x768")
root.configure(bg="white")

# Create a container to stack frames
container = Frame(root)
container.pack(fill=BOTH, expand=True)

# Dictionary to store frames
frames = {}

for F in ("home", "find_hospital", "medical_services", "health_library"):
    frame = Frame(container, bg="white")
    frames[F] = frame
    frame.grid(row=0, column=0, sticky="nsew")

# Navbar frame (common for all pages)
nav_bar = Frame(root, bg="white", height=80)
nav_bar.pack(side=TOP, fill=X)

# Create left and right navigation button frames
left_nav = Frame(nav_bar, bg="white")
left_nav.pack(side=LEFT, padx=20)
right_nav = Frame(nav_bar, bg="white")
right_nav.pack(side=RIGHT, padx=20)

# Load and place the X-Health logo at the center of the navbar
image_path = r"D:\Dhairyash\\College\2nd year\sem4\PRP\X-Health(Python Project)\X-Health Logo.jpg"  # Update path
logo_img = Image.open(image_path).resize((120, 60), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_img)
logo_label = Label(nav_bar, image=logo_photo, bg="white")
logo_label.pack(side=TOP, pady=5)

# Navigation buttons
nav_buttons = ["Home", "Find Hospital", "Medical Services", "Health Library"]
nav_frames = ["home", "find_hospital", "medical_services", "health_library"]

for text, page in zip(nav_buttons[:2], nav_frames[:2]):
    btn = Button(left_nav, text=text + " ↓", font=("Arial", 12, "bold"), bg="white", fg="black", bd=0, command=lambda p=page: show_frame(frames[p]))
    btn.pack(side=LEFT, padx=10, pady=20)

for text, page in zip(nav_buttons[2:], nav_frames[2:]):
    btn = Button(right_nav, text=text + " ↓", font=("Arial", 12, "bold"), bg="white", fg="black", bd=0, command=lambda p=page: show_frame(frames[p]))
    btn.pack(side=LEFT, padx=10, pady=20)

# Back button to return to home page
back_button = Button(nav_bar, text="← Back", font=("Arial", 12), bg="#3B5998", fg="white", command=lambda: show_frame(frames["home"]))
back_button.pack_forget()  # Hide initially

# Add content to each frame
for name, frame in frames.items():
    label = Label(frame, text=f"Welcome to {name.replace('_', ' ').title()} Page", font=("Arial", 20), bg="white")
    label.pack(anchor=W, padx=20, pady=20)  # Align text to the left below the navbar

# Show home page by default
show_frame(frames["home"])

root.mainloop()