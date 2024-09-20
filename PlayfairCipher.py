import tkinter as tk
from tkinter import filedialog, messagebox

class PlayfairCipher:
    def __init__(self, key):
        self.key = self.generate_key_matrix(key)
    
    def generate_key_matrix(self, key):
        key = key.lower().replace("j", "i")
        matrix = []
        alphabet = "abcdefghiklmnopqrstuvwxyz"
        for char in key:
            if char not in matrix and char in alphabet:
                matrix.append(char)
        for char in alphabet:
            if char not in matrix:
                matrix.append(char)
        return [matrix[i:i + 5] for i in range(0, len(matrix), 5)]
    
    def find_position(self, letter):
        for i, row in enumerate(self.key):
            if letter in row:
                return i, row.index(letter)
        return None
    
    def prepare_text(self, text):
        text = text.lower().replace("j", "i").replace(" ", "")
        prepared_text = ""
        i = 0
        while i < len(text):
            a = text[i]
            if i + 1 < len(text):
                b = text[i + 1]
                if a != b:
                    prepared_text += a + b
                    i += 2
                else:
                    prepared_text += a + 'x'
                    i += 1
            else:
                prepared_text += a + 'x'
                i += 1
        return prepared_text

    def encrypt(self, plaintext):
        plaintext = self.prepare_text(plaintext)
        ciphertext = ""
        for i in range(0, len(plaintext), 2):
            a, b = plaintext[i], plaintext[i + 1]
            row1, col1 = self.find_position(a)
            row2, col2 = self.find_position(b)
            if row1 == row2:
                ciphertext += self.key[row1][(col1 + 1) % 5] + self.key[row2][(col2 + 1) % 5]
            elif col1 == col2:
                ciphertext += self.key[(row1 + 1) % 5][col1] + self.key[(row2 + 1) % 5][col2]
            else:
                ciphertext += self.key[row1][col2] + self.key[row2][col1]
        return ciphertext
    
    def decrypt(self, ciphertext):
        plaintext = ""
        for i in range(0, len(ciphertext), 2):
            a, b = ciphertext[i], ciphertext[i + 1]
            row1, col1 = self.find_position(a)
            row2, col2 = self.find_position(b)
            if row1 == row2:
                plaintext += self.key[row1][(col1 - 1) % 5] + self.key[row2][(col2 - 1) % 5]
            elif col1 == col2:
                plaintext += self.key[(row1 - 1) % 5][col1] + self.key[(row2 - 1) % 5][col2]
            else:
                plaintext += self.key[row1][col2] + self.key[row2][col1]
        return plaintext

# GUI Implementation
class PlayfairApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Playfair Cipher")
        
        # Labels and inputs
        self.label_key = tk.Label(root, text="Enter Key (min 12 characters):")
        self.label_key.pack()

        self.entry_key = tk.Entry(root, width=50)
        self.entry_key.pack()

        self.label_input = tk.Label(root, text="Input Message:")
        self.label_input.pack()

        self.text_input = tk.Text(root, height=5, width=50)
        self.text_input.pack()

        # Buttons
        self.button_encrypt = tk.Button(root, text="Encrypt", command=self.encrypt_message)
        self.button_encrypt.pack()

        self.button_decrypt = tk.Button(root, text="Decrypt", command=self.decrypt_message)
        self.button_decrypt.pack()

        self.button_file = tk.Button(root, text="Upload File", command=self.upload_file)
        self.button_file.pack()

        # Output
        self.label_output = tk.Label(root, text="Output Message:")
        self.label_output.pack()

        self.text_output = tk.Text(root, height=5, width=50)
        self.text_output.pack()

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_input.insert(tk.END, content)

    def encrypt_message(self):
        key = self.entry_key.get()
        if len(key) < 12:
            messagebox.showerror("Error", "Key must be at least 12 characters long")
            return
        message = self.text_input.get("1.0", tk.END).strip()
        cipher = PlayfairCipher(key)
        encrypted_message = cipher.encrypt(message)
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, encrypted_message)

    def decrypt_message(self):
        key = self.entry_key.get()
        if len(key) < 12:
            messagebox.showerror("Error", "Key must be at least 12 characters long")
            return
        message = self.text_input.get("1.0", tk.END).strip()
        cipher = PlayfairCipher(key)
        decrypted_message = cipher.decrypt(message)
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, decrypted_message)

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = PlayfairApp(root)
    root.mainloop()
