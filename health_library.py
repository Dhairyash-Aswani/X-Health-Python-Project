import tkinter as tk
from tkinter import messagebox, scrolledtext
import mysql.connector
import google.generativeai as genai

# === Gemini API Key ===
genai.configure(api_key="AIzaSyCu9w5HA0kqVxSrCDTsaQbWZGQVV4ZQ5lo")
model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="xhealth"
    )

def fetch_data():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM health_library LIMIT 1")
    record = cursor.fetchone()
    db.close()
    return record

def open_add_data_form(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    frame.configure(bg="#E6F2FF")

    labels = [
        "Username",
        "Medical History",
        "Current Diseases",
        "Surgeries Done",
        "Medications",
        "Allergies",
        "Family Medical History"
    ]

    entries = {}

    for idx, label_text in enumerate(labels):
        label = tk.Label(frame, text=label_text, bg="#E6F2FF", fg="#0A1F44", font=("Arial", 12))
        label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")

        entry = tk.Entry(frame, width=40)
        entry.grid(row=idx, column=1, padx=10, pady=5)
        entries[label_text] = entry

    def save_to_db():
        try:
            db = connect_db()
            cursor = db.cursor()
            cursor.execute("SELECT id FROM health_library LIMIT 1")
            existing = cursor.fetchone()

            values = tuple(entry.get() for entry in entries.values())

            if existing:
                query = """
                    UPDATE health_library SET
                    username=%s,
                    medical_history=%s,
                    current_diseases=%s,
                    surgeries_done=%s,
                    medications=%s,
                    allergies=%s,
                    family_medical_history=%s
                    WHERE id=%s
                    """
                cursor.execute(query, values + (existing[0],))
            else:
                query = """
                    INSERT INTO health_library
                    (username, medical_history, current_diseases, surgeries_done, medications, allergies, family_medical_history)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                cursor.execute(query, values)

            db.commit()
            db.close()

            messagebox.showinfo("Success", "Your health data has been saved successfully!")
            load_health_library(frame)
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    save_button = tk.Button(frame, text="Save", command=save_to_db, bg="#40E0D0", fg="white", font=("Arial", 12, "bold"))
    save_button.grid(row=len(labels), columnspan=2, pady=20)

def open_gemini_chatbox(frame, user_context):
    chat_window = tk.Toplevel(frame)
    chat_window.title("Gemini AI Chat")
    chat_window.geometry("600x650")
    chat_window.configure(bg="#E6F2FF")

    chat_log = scrolledtext.ScrolledText(chat_window, wrap=tk.WORD, font=("Arial", 12))
    chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    chat_log.insert(tk.END, "\u2728 Gemini is ready to help you with health tips!\n\n")

    entry = tk.Entry(chat_window, font=("Arial", 12))
    entry.pack(padx=10, pady=5, fill=tk.X)

    def send_message():
        prompt = entry.get()
        if not prompt.strip():
            return

        chat_log.insert(tk.END, f"\nYou: {prompt}\n")
        entry.delete(0, tk.END)

        try:
            full_prompt = f"Patient health details: {user_context}\n\nUser question: {prompt}"
            response = model.generate_content(full_prompt)
            chat_log.insert(tk.END, f"Gemini: {response.text}\n")
        except Exception as e:
            chat_log.insert(tk.END, f"[Error contacting Gemini API: {e}]\n")

    send_btn = tk.Button(chat_window, text="Send", command=send_message, bg="#40E0D0", fg="white", font=("Arial", 12))
    send_btn.pack(pady=5)

def load_health_library(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    frame.configure(bg="#E6F2FF")

    record = fetch_data()

    if record:
        labels = [
            "Username",
            "Medical History",
            "Current Diseases",
            "Surgeries Done",
            "Medications",
            "Allergies",
            "Family Medical History"
        ]

        values_text = ""
        for idx, value in enumerate(record[1:]):
            label = tk.Label(frame, text=f"{labels[idx]}: {value}", bg="#E6F2FF", fg="#222222", font=("Arial", 12))
            label.pack(pady=5, anchor="w", padx=20)
            values_text += f"{labels[idx]}: {value}\n"

        update_button = tk.Button(frame, text="Update Data", command=lambda: open_add_data_form(frame), bg="#40E0D0", fg="white", font=("Arial", 12, "bold"))
        update_button.pack(pady=10)

        ai_button = tk.Button(frame, text="💬 Chat with Gemini AI", command=lambda: open_gemini_chatbox(frame, values_text), bg="#3ABEF9", fg="white", font=("Arial", 12, "bold"))
        ai_button.pack(pady=10)

    else:
        no_data_label = tk.Label(frame, text="No Data to Display", font=("Arial", 20, "bold"), bg="#E6F2FF", fg="#0A1F44")
        no_data_label.pack(pady=40)

        add_button = tk.Button(frame, text="Add Data", command=lambda: open_add_data_form(frame), bg="#40E0D0", fg="white", font=("Arial", 12, "bold"))
        add_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("XHealth Library")
    root.geometry("800x600")
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)
    load_health_library(main_frame)
    root.mainloop()