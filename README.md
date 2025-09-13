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
👉 [https://funproject1reaid-idtxngymum3x79jfss5ez3.streamlit.app/]


## 📷 Preview Aplikasi ##
1. 🔑 Login Page

Halaman login dengan username & password.
Jika berhasil login → diarahkan ke dashboard.

📸 [masukkan screenshot login di sini]

2. 🎭 Personality Quiz

Jawab 10 pertanyaan untuk mengetahui profesi yang sesuai:
misalnya Programmer, Designer, atau Data Scientist.
Hasil quiz ditampilkan dalam bentuk meme/gambar + penjelasan posisi.

📸 [masukkan screenshot personality quiz]

3. 🧠 Trivia Quiz

Kuis pengetahuan umum dengan skor otomatis.
Hasil skor ditampilkan setelah menjawab semua pertanyaan.

📸 [masukkan screenshot trivia quiz]

4. 👤 Profile Page

Menampilkan data profil pengguna:

Nama / Username

Skills dengan progress bar

Hobi / Interests

Kontak (Email, LinkedIn, GitHub)

📸 [masukkan screenshot profile]

5. 🚪 Logout

Keluar dari aplikasi dan kembali ke halaman login.

📸 [masukkan screenshot logout]

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
