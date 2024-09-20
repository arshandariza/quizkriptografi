Program ini merupakan aplikasi desktop yang dibuat menggunakan Python dengan Tkinter sebagai antarmuka pengguna (GUI). Aplikasi ini dapat mengenkripsi dan mendekripsi teks menggunakan dua algoritma kriptografi klasik:

Playfair Cipher
Hill Cipher
Pengguna dapat menginput teks secara langsung melalui GUI atau mengunggah file teks (.txt). Program ini juga memungkinkan pengguna untuk menginput kunci enkripsi dengan ketentuan panjang tertentu.

2. Persyaratan Sistem
Untuk menjalankan program ini, Anda memerlukan:

Python 3.x terinstal di sistem Anda.
Tkinter (sudah termasuk dalam instalasi standar Python).
Untuk versi Hill Cipher dengan NumPy, Anda memerlukan pustaka NumPy (bisa diabaikan jika menggunakan versi Hill Cipher tanpa NumPy).
Cara Instalasi NumPy (Jika diperlukan)
Jalankan perintah berikut di terminal/command prompt untuk menginstal NumPy:

Salin kode
pip install numpy
3. Cara Menjalankan Program
Download Source Code

Unduh atau klon repositori dari GitHub yang berisi semua kode sumber.
Jalankan Program

Buka terminal atau command prompt.
Navigasi ke direktori tempat file Python berada.
Jalankan salah satu dari program berikut:
Salin kode
python playfair_cipher.py
atau
Salin kode
python hill_cipher.py
atau
Salin kode
python hill_cipher_no_numpy.py
4. Input dan Output
4.1 Playfair Cipher
Input Key: Masukkan kunci enkripsi dengan panjang minimal 12 karakter.
Input Text: Anda bisa memasukkan teks untuk dienkripsi/didekripsi langsung melalui GUI atau mengunggah file teks dengan format .txt.
Output: Hasil enkripsi atau dekripsi akan ditampilkan di area output setelah tombol "Encrypt" atau "Decrypt" diklik.
4.2 Hill Cipher
Input Key: Masukkan kunci enkripsi dengan panjang minimal 16 karakter alfabetik.
Input Text: Anda bisa memasukkan teks untuk dienkripsi/didekripsi langsung melalui GUI atau mengunggah file .txt.
Output: Hasil enkripsi atau dekripsi akan ditampilkan di area output setelah tombol "Encrypt" atau "Decrypt" diklik.
4.3 Hill Cipher (Tanpa NumPy)
Program ini sama seperti Hill Cipher di atas, tetapi tidak menggunakan pustaka eksternal seperti NumPy.
5. Contoh Penggunaan
Playfair Cipher
Key: SECRETKEYSECRET
Plaintext: HELLOWORLD
Ciphertext: EMBAXNKEKS
Hill Cipher
Key: HILLCIPHERKEYXYZ
Plaintext: ATTACKATDAWN
Ciphertext: PSAAVSRXZBQC
Hill Cipher (Tanpa NumPy)
Key: HILLCIPHERKEYXYZ
Ciphertext: PSAAVSRXZBQC
Decrypted Text: ATTACKATDAWN
6. File Tambahan
Screenshots: Screenshot dari GUI program disertakan di repositori GitHub.
Readme.txt: Penjelasan ini ada di file README.txt yang disertakan di dalam repositori GitHub.
