import tkinter as tk
from tkinter import ttk

def load_medical_services(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    frame.configure(bg="#E6F2FF")

    label = tk.Label(frame, text="Nearby Hospitals", font=("Arial", 20, "bold"), bg="#E6F2FF", fg="#0A1F44")
    label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    hospitals_data = [
        {"name": "CityCare Hospital", "location": "Sector 21, New Delhi", "contact": "011-12345678", "rating": "4.5★"},
        {"name": "HealthFirst Clinic", "location": "MG Road, Bangalore", "contact": "080-98765432", "rating": "4.2★"},
        {"name": "Sunshine Hospital", "location": "Park Street, Kolkata", "contact": "033-44455566", "rating": "4.6★"},
        {"name": "Healing Touch Centre", "location": "Bandra West, Mumbai", "contact": "022-88889999", "rating": "4.3★"},
        {"name": "Lifeline Hospital", "location": "Anna Nagar, Chennai", "contact": "044-77776666", "rating": "4.4★"},
        {"name": "Green Valley Clinic", "location": "Vashi, Navi Mumbai", "contact": "022-55554444", "rating": "4.1★"},
    ]

    for i, hospital in enumerate(hospitals_data):
        row = i // 2
        col = i % 2

        card = tk.Frame(frame, bg="white", bd=1, relief="solid")
        card.place(relx=0.05 + col * 0.5, rely=0.15 + row * 0.25, relwidth=0.4, relheight=0.2)

        name_label = tk.Label(card, text=hospital["name"], font=("Arial", 14, "bold"), bg="white", fg="#0A1F44")
        name_label.pack(anchor="w", padx=10, pady=(10, 0))

        location_label = tk.Label(card, text="Location: " + hospital["location"], font=("Arial", 12), bg="white")
        location_label.pack(anchor="w", padx=10, pady=2)

        contact_label = tk.Label(card, text="Contact: " + hospital["contact"], font=("Arial", 12), bg="white")
        contact_label.pack(anchor="w", padx=10, pady=2)

        rating_label = tk.Label(card, text="Rating: " + hospital["rating"], font=("Arial", 12), bg="white")
        rating_label.pack(anchor="w", padx=10, pady=2)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Medical Services Example")
    root.geometry("800x600")
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)
    load_medical_services(main_frame)
    root.mainloop()