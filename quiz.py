import tkinter as tk
from tkinter import filedialog, messagebox

# Fungsi untuk Vigenere Cipher (Enkripsi)
def vigenere_encrypt(plain_text, key):
    encrypted_text = []
    key = key.upper()
    for i, char in enumerate(plain_text):
        if char.isalpha():
            shift = (ord(key[i % len(key)]) - 65)
            encrypted_char = chr((ord(char.upper()) + shift - 65) % 26 + 65)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

# Fungsi untuk Vigenere Cipher (Dekripsi)
def vigenere_decrypt(cipher_text, key):
    decrypted_text = []
    key = key.upper()
    for i, char in enumerate(cipher_text):
        if char.isalpha():
            shift = (ord(key[i % len(key)]) - 65)
            decrypted_char = chr((ord(char.upper()) - shift - 65) % 26 + 65)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

# Fungsi untuk memproses teks berdasarkan mode (enkripsi atau dekripsi)
def process_text(mode):
    text = text_area.get("1.0", tk.END).strip()
    key = entry_key.get()
    
    # Validasi kunci
    if len(key) < 12:
        messagebox.showerror("Error", "Kunci harus minimal 12 karakter!")
        return
    
    # Proses berdasarkan mode (enkripsi atau dekripsi)
    if mode == 'encrypt':
        result = vigenere_encrypt(text, key)
    elif mode == 'decrypt':
        result = vigenere_decrypt(text, key)
    
    # Tampilkan hasil di area hasil
    result_area.delete("1.0", tk.END)
    result_area.insert(tk.END, result)

# Fungsi untuk mengunggah file teks
def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)

# Inisialisasi GUI
root = tk.Tk()
root.title("Cipher Encryption Program")

# Elemen GUI untuk input teks atau file
label_text = tk.Label(root, text="Masukkan teks atau upload file:")
label_text.pack()

text_area = tk.Text(root, height=10, width=50)
text_area.pack()

button_upload = tk.Button(root, text="Upload File", command=upload_file)
button_upload.pack()

# Elemen GUI untuk input kunci
label_key = tk.Label(root, text="Masukkan Kunci (minimal 12 karakter):")
label_key.pack()

entry_key = tk.Entry(root, width=50)
entry_key.pack()

# Tombol untuk enkripsi
button_encrypt = tk.Button(root, text="Enkripsi", command=lambda: process_text('encrypt'))
button_encrypt.pack()

# Tombol untuk dekripsi
button_decrypt = tk.Button(root, text="Dekripsi", command=lambda: process_text('decrypt'))
button_decrypt.pack()

# Area untuk menampilkan hasil enkripsi/dekripsi
result_area = tk.Text(root, height=10, width=50)
result_area.pack()

root.mainloop()
