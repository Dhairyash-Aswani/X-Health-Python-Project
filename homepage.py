from tkinter import *
from PIL import Image, ImageTk

# Function to simulate navigation button click actions
def navigate_action(text):
    print(f"Navigating to {text}...")

# Initialize the main window
root = Tk()
root.title("X-Health(HOME)")
root.geometry("1024x768")

# Create header frame for navigation
header_frame = Frame(root, bg="white", height=80)
header_frame.pack(side=TOP, fill=X)

# Create a container frame to center buttons inside the header
button_container = Frame(header_frame, bg="white")
button_container.pack(pady=10)

# Add navigation buttons and center them
buttons = ["Discover Apollo", "Find Hospital", "Medical Services", "Health Library"]
for button_text in buttons:
    button = Button(button_container, text=button_text, bg="white", font=("Arial", 12), command=lambda bt=button_text: navigate_action(bt))
    button.pack(side=LEFT, padx=10)

# Load and display the image (simulating the large image in the center)
image_path = r"D:\Dhairyash\\College\2nd year\sem4\PRP\X-Health(Python Project)\landing page backgorund.png"  # Update the path to the uploaded image
image = Image.open(image_path)
image = image.resize((1024, 512), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Store the reference to avoid garbage collection
root.photo = photo

# Display the image in a label
image_label = Label(root, image=photo)
image_label.pack(pady=20)

# Run the Tkinter application
root.mainloop()
