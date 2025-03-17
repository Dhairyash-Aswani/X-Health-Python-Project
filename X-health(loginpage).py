import tkinter as tk
from tkinter import Label, Entry, Button
from PIL import Image, ImageTk

# Function to handle login action
def login_action():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "dhairyash.aswani" or password == "pass@123":
        print("Please enter both username and password!")
    else:
        print(f"Username: {username}, Password: {password}")

# Initialize the main window
root = tk.Tk()
root.title("X-Health Login")
root.geometry("500x400")

# Update the path to your local image
image_path = r"E:\Dhairyash Aswani\sem 4\python_GUI\images\X-health.png"  # Full path to your image
image = Image.open(image_path)
image = image.resize((300, 150), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS
photo = ImageTk.PhotoImage(image)

# Add the logo image to the window
logo_label = Label(root, image=photo)
logo_label.pack(pady=10)

# Add a Welcome Label
welcome_label = Label(root, text="WELCOME TO X-HEALTH", font=("Arial", 16))
welcome_label.pack(pady=10)

# Create Username and Password labels and entry boxes
username_label = Label(root, text="Username", font=("Arial", 12))
username_label.pack(pady=5)
username_entry = Entry(root, font=("Arial", 12), width=30)
username_entry.pack(pady=5)

password_label = Label(root, text="Password", font=("Arial", 12))
password_label.pack(pady=5)
password_entry = Entry(root, font=("Arial", 12), width=30, show="*")
password_entry.pack(pady=5)

# Create a Login button with more styling
login_button = Button(root, text="Login", font=("Arial", 12), bg="blue", fg="white", width=10, height=2, command=login_action)
login_button.pack(pady=20)

# Run the application
root.mainloop()
