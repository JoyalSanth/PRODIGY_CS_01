import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Logic
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

# Encrypt Text
def encrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    shift = shift_value.get()
    if not text:
        messagebox.showerror("Error", "Please enter some text!")
        return
    encrypted_text = caesar_cipher(text, shift, "encrypt")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_text)

# Decrypt Text
def decrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    shift = shift_value.get()
    if not text:
        messagebox.showerror("Error", "Please enter some text!")
        return
    decrypted_text = caesar_cipher(text, shift, "decrypt")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)

# Copy to Clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END).strip())
    root.update()
    messagebox.showinfo("Copied", "Text copied to clipboard!")

# UI Setup
root = tk.Tk()
root.title("🔐 Caesar Cipher GUI")
root.geometry("500x400")
root.configure(bg="#282c34")

# Header
header = tk.Label(root, text="Caesar Cipher", font=("Arial", 18, "bold"), fg="white", bg="#282c34")
header.pack(pady=10)

# Input Text Box
input_label = tk.Label(root, text="Enter Text:", font=("Arial", 12), fg="white", bg="#282c34")
input_label.pack()
input_text = tk.Text(root, height=3, width=50, font=("Arial", 12))
input_text.pack(pady=5)

# Shift Value
shift_label = tk.Label(root, text="Shift Value:", font=("Arial", 12), fg="white", bg="#282c34")
shift_label.pack()
shift_value = tk.IntVar(value=3)
shift_entry = tk.Entry(root, textvariable=shift_value, width=5, font=("Arial", 12))
shift_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#282c34")
button_frame.pack(pady=10)
encrypt_button = tk.Button(button_frame, text="Encrypt", font=("Arial", 12, "bold"), command=encrypt_text, bg="#4CAF50", fg="white")
encrypt_button.grid(row=0, column=0, padx=10)
decrypt_button = tk.Button(button_frame, text="Decrypt", font=("Arial", 12, "bold"), command=decrypt_text, bg="#FF9800", fg="white")
decrypt_button.grid(row=0, column=1, padx=10)

# Output Text Box
output_label = tk.Label(root, text="Output:", font=("Arial", 12), fg="white", bg="#282c34")
output_label.pack()
output_text = tk.Text(root, height=3, width=50, font=("Arial", 12), bg="#f4f4f4")
output_text.pack(pady=5)

# Copy Button
copy_button = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12, "bold"), command=copy_to_clipboard, bg="#007BFF", fg="white")
copy_button.pack(pady=5)

# Run Application
root.mainloop()
