# 📘 Dokumentasi Mini AppsQuiz 
📝 Deskripsi

Aplikasi ini adalah web app interaktif berbasis Streamlit yang berisi:

🔑 Login Page dengan autentikasi sederhana

🎭 Personality Quiz untuk mengetahui tipe kepribadian

🧠 Quiz Umum untuk menguji pengetahuan

👤 Profile Page berisi informasi pengguna

🚪 Logout untuk keluar dari aplikasi

# 🚀 Cara Menjalankan Aplikasi

## Clone atau salin project ##

<pre> git clone &lt;url_repo&gt; cd &lt;nama_folder&gt;  </pre>


## Buat virtual environment (opsional tapi disarankan) ##

<pre> 
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
 </pre>

## Install dependencies ##

<pre> pip install -r requirements.txt  </pre>


## Jalankan aplikasi Streamlit ##

<pre> streamlit run app.py  </pre>


## Akses aplikasi ##
Buka browser di:
👉 [https://funproject1reaid-lv8iueqmycfmhjneoetqk8.streamlit.app/]


## 📷 Preview Aplikasi ##
1. 🔑 Login Page

Halaman login dengan username & password.
Jika berhasil login → diarahkan ke dashboard.

<img width="956" height="552" alt="image" src="https://github.com/user-attachments/assets/90b04704-d761-40e3-94c9-e2bbffac4b16" />

2. 🎭 Personality Quiz

Jawab 10 pertanyaan untuk mengetahui profesi yang sesuai:
misalnya Programmer, Designer, atau Data Scientist.
Hasil quiz ditampilkan dalam bentuk meme/gambar + penjelasan posisi.

<img width="764" height="510" alt="image" src="https://github.com/user-attachments/assets/f19cff89-2db8-4290-acf5-34d971675a40" />
<img width="1354" height="539" alt="image" src="https://github.com/user-attachments/assets/58d17300-80c6-4409-a2a0-bf0b8891fe9a" />
<img width="1198" height="566" alt="image" src="https://github.com/user-attachments/assets/cec20502-8bfe-43c0-b41a-bcaaf3a6124e" />

3. 🧠 Trivia Quiz

Kuis pengetahuan umum dengan skor otomatis.
Hasil skor ditampilkan setelah menjawab semua pertanyaan.

<img width="1358" height="537" alt="image" src="https://github.com/user-attachments/assets/bb6794b9-71c1-4520-a940-3304e8bfb7c1" />
<img width="1360" height="573" alt="image" src="https://github.com/user-attachments/assets/46d12f31-1609-4e49-87c6-fc3caf215373" />
<img width="1345" height="520" alt="image" src="https://github.com/user-attachments/assets/dc79642c-f174-4612-acab-cab82ac67657" />

4. 👤 Profile Page

Menampilkan data profil pengguna:

Nama / Username

Skills dengan progress bar

Hobi / Interests

Kontak (Email, LinkedIn, GitHub)

<img width="1335" height="523" alt="image" src="https://github.com/user-attachments/assets/40819f0f-5731-452a-a2a5-615fec9e9e54" />


5. 🚪 Logout

Keluar dari aplikasi dan kembali ke halaman login.

<img width="1347" height="499" alt="image" src="https://github.com/user-attachments/assets/9dd21f7a-ac53-4819-943b-f32339f6a15a" />


## 📖 Instruksi Penggunaan ##

Login
Masukkan username & password (contoh: admin / 1234).

Pilih Menu di Sidebar

🎭 Personality Quiz → jawab pertanyaan → lihat hasil.

🧠 Trivia Quiz → jawab soal → lihat skor akhir.

👤 Profile → lihat informasi akun.

🚪 Logout → keluar dari aplikasi.

Enjoy the app! 🎉

## 🔧 Teknologi yang Digunakan ## 

Python 3.x

Streamlit untuk UI interaktif

Custom CSS untuk desain login & sidebar

Session State untuk login/logout
