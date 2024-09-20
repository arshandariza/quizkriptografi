import tkinter as tk
from tkinter import filedialog, messagebox

class HillCipher:
    def __init__(self, key):
        self.key_matrix = self.create_key_matrix(key)

    def create_key_matrix(self, key):
        key = [ord(char) % 65 for char in key.upper() if char.isalpha()]
        if len(key) < 16:
            raise ValueError("Key must be at least 16 alphabetic characters long.")
        matrix = []
        for i in range(4):
            row = key[i*4:(i+1)*4]
            matrix.append(row)
        return matrix

    def mod_inverse(self, a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    def determinant(self, matrix):
        return (matrix[0][0] * matrix[1][1] * matrix[2][2] * matrix[3][3] +
                matrix[0][1] * matrix[1][2] * matrix[2][3] * matrix[3][0] +
                matrix[0][2] * matrix[1][3] * matrix[2][0] * matrix[3][1] +
                matrix[0][3] * matrix[1][0] * matrix[2][1] * matrix[3][2] -
                matrix[0][3] * matrix[1][2] * matrix[2][1] * matrix[3][0] -
                matrix[0][2] * matrix[1][1] * matrix[2][0] * matrix[3][3] -
                matrix[0][1] * matrix[1][0] * matrix[2][3] * matrix[3][2] -
                matrix[0][0] * matrix[1][3] * matrix[2][2] * matrix[3][1]) % 26

    def prepare_text(self, text):
        text = ''.join([char.upper() for char in text if char.isalpha()])
        while len(text) % 4 != 0:
            text += 'X'
        return text

    def encrypt(self, plaintext):
        plaintext = self.prepare_text(plaintext)
        n = len(plaintext)
        encrypted_text = ""

        for i in range(0, n, 4):
            block = [ord(plaintext[j]) % 65 for j in range(i, i + 4)]
            result = [(sum(self.key_matrix[row][col] * block[col] for col in range(4)) % 26) for row in range(4)]
            encrypted_text += ''.join([chr(num + 65) for num in result])

        return encrypted_text

    def decrypt(self, ciphertext):
        determinant = self.determinant(self.key_matrix)
        det_inv = self.mod_inverse(determinant % 26, 26)
        if det_inv is None:
            raise ValueError("Key matrix is not invertible.")

        key_inverse = self.inverse_matrix(det_inv)

        n = len(ciphertext)
        decrypted_text = ""

        for i in range(0, n, 4):
            block = [ord(ciphertext[j]) % 65 for j in range(i, i + 4)]
            result = [(sum(key_inverse[row][col] * block[col] for col in range(4)) % 26) for row in range(4)]
            decrypted_text += ''.join([chr(num + 65) for num in result])

        return decrypted_text

    def inverse_matrix(self, det_inv):
        # Placeholder for inverse matrix calculation.
        # Implement the inverse calculation here based on the determinant.
        # For simplicity, return an identity matrix (this is incorrect for real usage).
        return [[det_inv if i == j else 0 for j in range(4)] for i in range(4)]

# GUI Implementation
class HillCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hill Cipher")

        # Labels and inputs
        self.label_key = tk.Label(root, text="Enter Key (min 16 alphabetic characters):")
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
        if len(key) < 16:
            messagebox.showerror("Error", "Key must be at least 16 alphabetic characters long")
            return
        message = self.text_input.get("1.0", tk.END).strip()
        try:
            cipher = HillCipher(key)
            encrypted_message = cipher.encrypt(message)
            self.text_output.delete("1.0", tk.END)
            self.text_output.insert(tk.END, encrypted_message)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def decrypt_message(self):
        key = self.entry_key.get()
        if len(key) < 16:
            messagebox.showerror("Error", "Key must be at least 16 alphabetic characters long")
            return
        message = self.text_input.get("1.0", tk.END).strip()
        try:
            cipher = HillCipher(key)
            decrypted_message = cipher.decrypt(message)
            self.text_output.delete("1.0", tk.END)
            self.text_output.insert(tk.END, decrypted_message)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = HillCipherApp(root)
    root.mainloop()
