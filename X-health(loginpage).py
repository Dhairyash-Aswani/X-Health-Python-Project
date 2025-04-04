from tkinter import *
from tkinter import Button  # Use tkinter.Button for buttons where you need customization
from tkinter.ttk import Entry  # Keep using ttk for Entry, as it doesn't need customization
from tkinter import Label  # Use tkinter.Label for labels where you need background color
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="xhealth"
)
mycursor = mydb.cursor()

# Function to open the dashboard after successful login
def open_dashboard(username):
    dashboard = Toplevel(root)  # Create a new window
    dashboard.title("Home Page")
    dashboard.geometry("800x800")

    welcome_label = Label(dashboard, text=f"Welcome, {username}!", font=("Arial", 16))
    welcome_label.pack(pady=20)

# Function to handle signup action
def signup_action():
    new_window = Toplevel(root)  # Create a new window
    new_window.title("Sign up")
    new_window.geometry("450x450")

    # Load the image
    image_path = r"D:\Dhairyash\\College\2nd year\sem4\PRP\X-Health(Python Project)\landing page display image.jpg"
    image = Image.open(image_path)
    image = image.resize((300, 150), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    new_window.photo = photo  # Keep reference to avoid garbage collection
    logo_label = Label(new_window, image=photo)
    logo_label.pack(pady=10)

    welcome_label = Label(new_window, text="WELCOME TO X-HEALTH", font=("Arial", 16))
    welcome_label.pack(pady=10)

    email_label = Label(new_window, text="Email", font=("Arial", 12))
    email_label.pack(pady=5)
    email_entry = Entry(new_window, font=("Arial", 12), width=30)
    email_entry.pack(pady=5)

    mobile_label = Label(new_window, text="Mobile Number", font=("Arial", 12))
    mobile_label.pack(pady=5)
    mobile_entry = Entry(new_window, font=("Arial", 12), width=30)
    mobile_entry.pack(pady=5)

    username_label = Label(new_window, text="Username", font=("Arial", 12))
    username_label.pack(pady=5)
    username_entry = Entry(new_window, font=("Arial", 12), width=30)
    username_entry.pack(pady=5)

    password_label = Label(new_window, text="Password", font=("Arial", 12))
    password_label.pack(pady=5)
    password_entry = Entry(new_window, font=("Arial", 12), width=30, show="*")
    password_entry.pack(pady=5)

    def save_signup_details():
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()
        mobile = mobile_entry.get()

        if username and password and email and mobile:
            Insert = "INSERT INTO login (username, password, email, mobile) VALUES (%s, %s, %s, %s)"
            Value = (username, password, email, mobile)
            mycursor.execute(Insert, Value)
            mydb.commit()
            messagebox.showinfo("Success", "Sign-up complete!")
            new_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill all details!")

    signup_btn = Button(new_window, text="Sign Up", font=("Arial", 12), bg="blue", fg="white", width=10, height=2, command=save_signup_details)
    signup_btn.pack(pady=20)

# Function to handle login action
def login_action():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        mycursor.execute("SELECT * FROM login WHERE username=%s AND password=%s", (username, password))
        user = mycursor.fetchone()
        if user:
            messagebox.showinfo("Logged in Successfully", f"Welcome {username}!")
            open_dashboard(username)
        else:
            messagebox.showerror("Error", "Invalid Username or Password!")
    else:
        messagebox.showerror("Error", "All fields are required!")

# Initialize the main window
root = Tk()
root.title("X-Health Login")
root.geometry("900x550")
root.configure(bg="#23395B")  # Set a default background color for the window

# Configure the grid to allow expansion
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Apply gradient background (using tkinter.Frame instead of ttk.Frame)
gradient_frame_left = Frame(root, bg="#95C8F0")  # Use tkinter.Frame
gradient_frame_left.grid(row=0, column=0, sticky="nsew")  # Expand in all directions

gradient_frame_right = Frame(root, bg="#23395B")  # Use tkinter.Frame
gradient_frame_right.grid(row=0, column=1, sticky="nsew")  # Expand in all directions

# Make frames expandable with the window
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

# Load and display the logo on the left frame
image_path = r"D:\Dhairyash\\College\2nd year\sem4\PRP\X-Health(Python Project)\landing page display image.jpg"
image = Image.open(image_path)
image = image.resize((400, 400), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Store reference to avoid garbage collection
root.photo = photo

# Add the logo image on the left side
logo_label = Label(gradient_frame_left, image=photo, bg="#95C8F0")
logo_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Add a Login title on the right side
login_title = Label(gradient_frame_right, text="Login", font=("Arial", 24), bg="#23395B", fg="white")
login_title.place(relx=0.5, rely=0.15, anchor=CENTER)

# Username Field
username_label = Label(gradient_frame_right, text="Username", font=("Arial", 12), bg="#23395B", fg="white")
username_label.place(relx=0.5, rely=0.3, anchor=CENTER)
username_entry = Entry(gradient_frame_right, font=("Arial", 12), width=30)
username_entry.place(relx=0.5, rely=0.35, anchor=CENTER)

# Password Field
password_label = Label(gradient_frame_right, text="Password", font=("Arial", 12), bg="#23395B", fg="white")
password_label.place(relx=0.5, rely=0.45, anchor=CENTER)
password_entry = Entry(gradient_frame_right, font=("Arial", 12), width=30, show="*")
password_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

# Login Button
login_button = Button(gradient_frame_right, text="Login", font=("Arial", 12), bg="blue", fg="white", width=10, height=2, command=login_action)
login_button.place(relx=0.5, rely=0.6, anchor=CENTER)

# Signup Link
signup_label = Label(gradient_frame_right, text="Create an account", font=("Arial", 10), bg="#23395B", fg="white", cursor="hand2")
signup_label.place(relx=0.4, rely=0.75, anchor=CENTER)
signup_button = Button(gradient_frame_right, text="Signup", font=("Arial", 10), bg="blue", fg="white", width=8, command=signup_action)
signup_button.place(relx=0.6, rely=0.75, anchor=CENTER)

# Forget Password
forgot_password_label = Label(gradient_frame_right, text="Forget Password?", font=("Arial", 10), bg="#23395B", fg="white", cursor="hand2")
forgot_password_label.place(relx=0.5, rely=0.85, anchor=CENTER)

# Run the application
root.mainloop()
