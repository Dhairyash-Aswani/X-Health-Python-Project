from tkinter.ttk import *
from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="xhealth"
)
mycursor = mydb.cursor()


#homepage opens after successfull log in 
def open_dashboard(username):
    dashboard = Toplevel(root)  # Create a new window
    dashboard.title("Home Page")
    dashboard.geometry("800x800")

    welcome_label = Label(dashboard, text=f"Welcome, {username}!", font=("Arial", 16))
    welcome_label.pack(pady=20)

    #logout_button = Button(dashboard, text="Logout", font=("Arial", 12), bg="red", fg="white", width=10, height=2, command=dashboard.destroy)
    #logout_button.pack(pady=20)




# Function to handle signup
def signup_action():
    new_window = Toplevel(root)  # Create a new window
    new_window.title("Sign up")
    new_window.geometry("450x450")

    # Load the image
    image_path = r"C:\Users\Yasharth\OneDrive\Desktop\Yasharth\Python\\Mini project (Xhealth)\X-Health Logo.jpg"
    image = Image.open(image_path)
    image = image.resize((300, 150), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # Store a reference to avoid garbage collection
    new_window.photo = photo

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

    # Function to store signup details in the database
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
                new_window.destroy()  # Close the signup window
        else:
            messagebox.showerror("Error", "Please fill all details!")

    # Signup Button
    signup_btn = Button(new_window, text="Sign Up", font=("Arial", 12), bg="blue", fg="white", width=10, height=2, command=save_signup_details)
    signup_btn.pack(pady=20)

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
root.geometry("500x550")

# Load and display the logo
image_path = r"C:\Users\Yasharth\OneDrive\Desktop\Yasharth\Python\\Mini project (Xhealth)\X-Health Logo.jpg"
image = Image.open(image_path)
image = image.resize((300, 150), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Store reference to avoid garbage collection
root.photo = photo

# Add the logo image
logo_label = Label(root, image=photo)
logo_label.pack(pady=10)

# Add a Welcome Label
welcome_label = Label(root, text="WELCOME TO X-HEALTH", font=("Arial", 16))
welcome_label.pack(pady=10)

# Username Field
username_label = Label(root, text="Username", font=("Arial", 12))
username_label.pack(pady=5)
username_entry = Entry(root, font=("Arial", 12), width=30)
username_entry.pack(pady=5)

# Password Field
password_label = Label(root, text="Password", font=("Arial", 12))
password_label.pack(pady=5)
password_entry = Entry(root, font=("Arial", 12), width=30, show="*")
password_entry.pack(pady=5)

# Login Button
login_button = Button(root, text="Login", font=("Arial", 12), bg="blue", fg="white", width=10, height=2,command=login_action)
login_button.pack(pady=20)

# Signup Button
acc_label = Label(root, text="Don't have and account?", font=("Arial", 9))
acc_label.pack(pady=3)
signup_button = Button(root, text="Signup", font=("Arial", 12), bg="blue", fg="white", width=10, height=2, command=signup_action)
signup_button.pack(pady=20)

# Run the application
root.mainloop()
