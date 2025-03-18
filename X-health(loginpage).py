from tkinter.ttk import *
from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="xhealth"
)
mycursor = mydb.cursor()
# Function to handle login action
def signup_action():
    username = username_entry.get()
    password = password_entry.get()

    Insert = "Insert into login(username,password) values(%s,%s)"
    if(username!="" and password!=""):
            Value = (username,password)
            print(Value)
            mycursor.execute(Insert, Value)
            mydb.commit()
            messagebox.askokcancel("Information", "Record inserted")            
    else:
        if (username == "" and password == ""):
            messagebox.askokcancel("Information", "Please Fill All Details")
        else:
            messagebox.askokcancel("Information", "Some fields left blank")

# Initialize the main window
root = Tk()
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
login_button = Button(root, text="LOGIN", font=("Arial", 12), bg="blue", fg="white", width=10, height=2, command=signup_action)
login_button.pack(pady=20)

signup_button = Button(root, text="SIGNUP", font=("Arial", 12), bg="blue", fg="white", width=10, height=2, command=signup_action)
signup_button.pack(pady=20)

# Run the application
root.mainloop()
