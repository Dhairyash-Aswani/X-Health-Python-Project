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

def signup_action():
    new_window = Toplevel(root)
    new_window.title("Sign up")
    new_window.geometry("450x600")

    # Create canvas and scrollbar
    canvas = Canvas(new_window)
    scrollbar = Scrollbar(new_window, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Create a centered frame inside scrollable_frame
    form_frame = Frame(scrollable_frame)
    form_frame.pack(pady=20)

    # Load the image
    image_path = r"D:\Dhairyash\\College\2nd year\sem4\PRP\X-Health(Python Project)\X-Health Logo.jpg"
    image = Image.open(image_path)
    image = image.resize((300, 150), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    new_window.photo = photo
    logo_label = Label(form_frame, image=photo)
    logo_label.pack(pady=10)

    welcome_label = Label(form_frame, text="WELCOME TO X-HEALTH", font=("Arial", 16))
    welcome_label.pack(pady=10)

    # Fields
    def create_label_entry(text):
        label = Label(form_frame, text=text, font=("Arial", 12))
        label.pack(pady=5)
        entry = Entry(form_frame, font=("Arial", 12), width=30)
        entry.pack(pady=5)
        return entry

    name_entry = create_label_entry("Name")
    age_entry = create_label_entry("Age")
    gender_entry = create_label_entry("Gender")
    address_entry = create_label_entry("Address")
    email_entry = create_label_entry("Email")
    mobile_entry = create_label_entry("Mobile Number")
    username_entry = create_label_entry("Username")
    password_label = Label(form_frame, text="Password", font=("Arial", 12))
    password_label.pack(pady=5)
    password_entry = Entry(form_frame, font=("Arial", 12), width=30, show="*")
    password_entry.pack(pady=5)

    def save_signup_details():
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_entry.get()
        address = address_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()
        mobile = mobile_entry.get()

        if username and password and email and mobile:
            Insert = "INSERT INTO login (name, age, gender, address, email, mobile, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            Value = (name, age, gender, address, email, mobile, username, password)
            mycursor.execute(Insert, Value)
            mydb.commit()
            messagebox.showinfo("Success", "Sign-up complete!")
            new_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill all details!")

    signup_btn = Button(form_frame, text="Sign Up", font=("Arial", 12), bg="blue", fg="white", width=10, height=2, command=save_signup_details)
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
            #open_dashboard(username)
            root.destroy() # Close login window (optional)
            # Correct way to open homepage
            import homepage
            homepage.open_dashboard(username)
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
image_path = r"D:\Dhairyash\\College\2nd year\sem4\PRP\X-Health(Python Project)\X-Health Logo.jpg"
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
