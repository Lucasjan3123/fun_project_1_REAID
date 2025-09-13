import streamlit as st

# Fake user database
USER_CREDENTIALS = {
    "admin": "1234",
    "lucas": "pass123"
}

# ============ INIT SESSION ============
if "page" not in st.session_state:
    st.session_state.page = "personality"
if "perso_current" not in st.session_state:
    st.session_state.perso_current = 0
if "perso_answers" not in st.session_state:
    st.session_state.perso_answers = []
if "perso_submitted" not in st.session_state:
    st.session_state.perso_submitted = False
if "sidebar_visible" not in st.session_state:
    st.session_state.sidebar_visible = False


# ====================== CUSTOM STYLE ======================
sidebar_style = """
<style>
/* Sidebar full tinggi */
[data-testid="stSidebar"] {
    padding: 0;
    height: 100vh;
    background: linear-gradient(to bottom, white 15vh, #1E90FF 15vh);
    border-right: 2px solid black;
    display: flex;
    flex-direction: column;
}

/* Title */
.sidebar-title {
    text-align: center;
    padding: 1.5em 1em;
    font-size: 1.4em;
    font-weight: bold;
    color: #333;
}

/* Button wrapper flex */
sidebar-buttons {
    display: flex;
    flex-direction: column;
    padding: 1em;
    gap: 0.8em;
    height: 100%;   /* pastikan penuh */
}

.sidebar-buttons button {
    flex: 1;   /* semua tombol berbagi tinggi sama rata */
    width: 100% !important;
    background-color: white !important;
    color: black !important;
    border: 1px solid #ddd !important;
    font-size: 1em !important;
    font-weight: 500 !important;
    border-radius: 12px !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.15);
}

/* Tombol seragam */
[data-testid="stSidebar"] button {
    flex: 0 0 auto;
    background-color: white !important;
    color: black !important;
    border: 1px solid #ddd !important;
    padding: 0.8em 1em !important;
    font-size: 1em !important;
    font-weight: 500 !important;
    border-radius: 12px !important;
    width: 100% !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    transition: all 0.3s ease-in-out;
}

/* Hover effect */
[data-testid="stSidebar"] button:hover {
    background-color: #f0f0f0 !important;
    border: 1px solid #bbb !important;
    transform: translateY(-2px);
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
}
</style>
"""


# ========== LOGIN FUNCTION ==========
import streamlit as st

# Fake database user
USER_CREDENTIALS = {
    "admin": "1234",
    "lucas": "pass123"
}

def login():
    # CSS untuk desain login page
        st.markdown(
        """
        <style>
        .login-container {
            background: linear-gradient(135deg, #ffffff, #f9f9ff);
            padding: 40px 30px;
            border-radius: 20px;
            border: 1px solid #e6e6e6;
            box-shadow: 0 8px 20px rgba(0,0,0,0.12);
            width: 380px;
            margin: 80px auto;
            text-align: center;
            transition: all 0.3s ease-in-out;
        }
        .login-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 28px rgba(0,0,0,0.18);
        }
        .login-logo {
            width: 90px;
            margin-bottom: 15px;
            border-radius: 50%;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .login-title {
            font-size: 26px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #2c3e50;
        }
        .login-subtitle {
            font-size: 14px;
            color: #7f8c8d;
            margin-bottom: 25px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

        st.markdown('<img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" class="login-logo">', unsafe_allow_html=True)
        st.markdown('<div class="login-title">🔑 Trivia Quiz Login</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-subtitle">Masukkan username & password untuk melanjutkan</div>', unsafe_allow_html=True)


        username = st.text_input("👤 Username")
        password = st.text_input("🔒 Password", type="password")

        if st.button("Login"):
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.success(f"Welcome, {username}!")
                st.rerun()
            else:
                st.error("❌ Username atau password salah!")

def logout():
    st.session_state["logged_in"] = False
    st.session_state.pop("username", None)
    st.rerun()

# ====================== TOGGLE SIDEBAR ======================
def show_sidebar():
    st.markdown(sidebar_style, unsafe_allow_html=True)
    st.sidebar.markdown('<div class="sidebar-title">📌 Menu</div>', unsafe_allow_html=True)
    st.sidebar.markdown('<div class="sidebar-buttons">', unsafe_allow_html=True)

    if st.sidebar.button("🎭 Personality Quiz"):
       st.session_state.page = "personality"
    if st.sidebar.button("🎯 Quiz "):
        st.session_state.page = "quiz"
    if st.sidebar.button("👤 Profile"):
        st.session_state.page = "profile"
    if st.sidebar.button("🚪 Logout"):
        st.session_state.page = "logout"

    st.sidebar.markdown('</div>', unsafe_allow_html=True)
# ====================== HEADER ======================
def show_header():
    st.markdown(
        """
        <div style="background-color:#4A90E2;
                    padding:15px;
                    border-radius:10px;
                    text-align:center;
                    margin-bottom:20px;">
            <h1 style="color:white; margin:0;">Trivia Quiz 🎉</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

# ====================== QUIZ LOGIC ======================
def quiz_page():
    # Inisialisasi state
    if "current" not in st.session_state:
        st.session_state.current = 0
    if "submitted" not in st.session_state:
        st.session_state.submitted = False
    if "answers" not in st.session_state:
        st.session_state.answers = [None] * len(questions)

    current = st.session_state.current
    question = questions[current]

    # Layout 2 kolom
    col_left, col_right = st.columns([3, 1])

    # ----- LEFT COLUMN -----
    with col_left:
        st.progress((current + 1) / len(questions))
        st.write(f"**Soal {current+1}:** {question['q']}")

        selected = st.radio(
            "Pilih jawaban:",
            question["options"],
            index=question["options"].index(st.session_state.answers[current])
            if st.session_state.answers[current] is not None else 0,
            key=f"q_{current}"
        )

        st.session_state.answers[current] = selected

        if current < len(questions) - 1:
            if st.button("Next"):
                st.session_state.current += 1
                st.rerun()
        else:
            if st.button("Submit"):
                st.session_state.submitted = True
                st.rerun()

    # ----- RIGHT COLUMN -----
    with col_right:
        st.subheader("Quiz Questions List")
        for i, q in enumerate(questions):
            label = f"Question {i+1}"
            ans = st.session_state.answers[i]
            if ans is not None:
                st.success(label)
            elif i == current:
                st.warning(label)
            else:
                st.write(label)

    # ----- RESULTS -----
    if st.session_state.submitted:
        score = 0
        st.subheader("Hasil Quiz")
        for i, q in enumerate(questions):
            user_ans = st.session_state.answers[i]
            if user_ans is None:
                st.warning(f"Q{i+1}: Belum dijawab ⚠️ (Benar: {q['answer']})")
            elif user_ans == q["answer"]:
                st.success(f"Q{i+1}: Benar ✅ ({user_ans})")
                score += 1
            else:
                st.error(f"Q{i+1}: Salah ❌ (Jawabanmu: {user_ans}, Benar: {q['answer']})")
        st.info(f"**Total Skor: {score}/{len(questions)}**")

        if score == len(questions):
            st.image("https://i.imgflip.com/30zz5g.jpg", caption="Perfect Score! 🔥")
        elif score >= len(questions) // 2:
            st.image("https://i.imgflip.com/4t0m5.jpg", caption="Not bad 😎")
        else:
            st.image("https://i.imgflip.com/1ur9b0.jpg", caption="Better luck next time 😅")

# ============ HALAMAN PERSONALITY QUIZ ============
def personality_quiz():
    st.title("🎭 Personality Quiz")
    st.write("Jawab pertanyaan berikut untuk mengetahui profesi yang cocok untukmu!")

    current = st.session_state.perso_current
    question = personality_questions[current]

    st.write(f"**Soal {current+1}:** {question['q']}")

    options = list(question["options"].keys())

    selected = st.radio(
        "Pilih jawaban:",
        options,
        index=(
            options.index(st.session_state.perso_answers[current])
            if len(st.session_state.perso_answers) > current and st.session_state.perso_answers[current] is not None
            else 0
        ) if len(st.session_state.perso_answers) > current else 0,
        key=f"perso_q_{current}"
    )

    # Simpan jawaban
    if len(st.session_state.perso_answers) <= current:
        st.session_state.perso_answers.append(selected)
    else:
        st.session_state.perso_answers[current] = selected

    # Tombol navigasi
    if current < total_perso_q - 1:
        if st.button("Next"):
            st.session_state.perso_current += 1
            st.rerun()
    else:
        if st.button("Submit"):
            st.session_state.perso_submitted = True
            st.rerun()

    # Kalau sudah submit
    if st.session_state.perso_submitted:
        st.subheader("🔮 Hasil Personality Quiz")
        scores = {"Programmer": 0, "Designer": 0, "Data Scientist": 0}

        for i, ans in enumerate(st.session_state.perso_answers):
            profession = personality_questions[i]["options"][ans]
            scores[profession] += 1

        # Profesi dengan skor tertinggi
        result = max(scores, key=scores.get)
        st.success(f"Kamu cocok menjadi seorang **{result}**!")
        
        if result == "Programmer":
            st.image("https://i.imgflip.com/4/4t0m5.jpg", caption="Programmer Life 😂")
            st.markdown("### 👨‍💻 Kamu cocok jadi **Programmer**!")
            st.write(
                "Kamu suka berpikir logis, menyelesaikan masalah dengan kode, "
                "dan senang menciptakan solusi otomatis. Posisi ini cocok buat kamu "
                "yang suka bekerja dengan teknologi dan tantangan."
            )

        elif result == "Designer":
            st.image("https://i.imgflip.com/2/30zz5g.jpg", caption="Designer Mode 🎨")
            st.markdown("### 🎨 Kamu cocok jadi **Designer**!")
            st.write(
                "Kamu punya mata yang tajam untuk detail dan estetika. "
                "Kamu bisa mengubah ide menjadi visual yang menarik dan "
                "membuat orang lain terkesan."
            )

        elif result == "Data Scientist":
            st.image("https://i.imgflip.com/1bij.jpg", caption="Data is the new oil 📊")
            st.markdown("### 📊 Kamu cocok jadi **Data Scientist**!")
            st.write(
                "Kamu suka menganalisis data, mencari pola tersembunyi, "
                "dan mengambil keputusan berdasarkan angka. "
                "Profesi ini cocok untuk pemikir analitis."
            ) 
        
        # Reset tombol
        if st.button("Ulangi Quiz"):
            st.session_state.perso_current = 0
            st.session_state.perso_answers = []
            st.session_state.perso_submitted = False
            st.rerun()


    

# ====================== PROFILE PAGE ======================

def profile_page():
    st.title("👤 My Profile")

    # Ambil username dari session
    username = st.session_state.get("username", "Guest")

    # Foto + deskripsi
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("https://i.pravatar.cc/250", width=150, caption=username)
    with col2:
        st.subheader(username)
        st.write(
            f"Halo, saya **{username}** 👋. "
            "Seorang software engineer muda yang suka belajar hal baru, "
            "membuat project kreatif, dan membangun solusi digital."
        )

    st.markdown("---")

    # Bagian skill dengan progress bar
    st.subheader("💡 Skills")
    st.progress(80)  
    st.text("Python (80%)")
    st.progress(70)  
    st.text("SQL & Database (70%)")
    st.progress(60)  
    st.text("Streamlit & Data Viz (60%)")

    st.markdown("---")

    # Bagian interest/hobi
    st.subheader("🎯 Interests")
    st.write("💻 Coding | 📊 Data Science | 🥊 Muay Thai | 📚 Self-Development")

    st.markdown("---")

    # Bagian kontak
    st.subheader("📬 Get in Touch")
    st.write(f"📧 Email: {username}@example.com")
    st.write("🌐 LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com)")
    st.write("🐙 GitHub: [github.com/yourusername](https://github.com)")


# ====================== QUESTIONS DATA ======================
questions = [
    {"q": "Ibukota Indonesia adalah?", "options": ["Jakarta", "Bandung", "Surabaya", "Medan"], "answer": "Jakarta"},
    {"q": "2 + 5 = ?", "options": ["5", "6", "7", "8"], "answer": "7"},
    {"q": "Planet terbesar di tata surya adalah?", "options": ["Bumi", "Mars", "Saturnus", "Jupiter"], "answer": "Jupiter"},
    {"q": "Bahasa resmi yang digunakan di Brasil?", "options": ["Spanyol", "Inggris", "Portugis", "Perancis"], "answer": "Portugis"},
    {"q": "Siapa penemu lampu pijar?", "options": ["Newton", "Edison", "Einstein", "Tesla"], "answer": "Edison"},
    {"q": "Gunung tertinggi di dunia adalah?", "options": ["Kilimanjaro", "Everest", "Elbrus", "Andes"], "answer": "Everest"},
    {"q": "Sungai terpanjang di dunia adalah?", "options": ["Amazon", "Nil", "Yangtze", "Mississippi"], "answer": "Nil"},
    {"q": "Proklamasi kemerdekaan Indonesia dibacakan pada tahun?", "options": ["1940", "1942", "1945", "1950"], "answer": "1945"},
    {"q": "Hewan tercepat di darat adalah?", "options": ["Singa", "Cheetah", "Kuda", "Rusa"], "answer": "Cheetah"},
    {"q": "Lambang kimia dari emas adalah?", "options": ["Ag", "Au", "Fe", "Pt"], "answer": "Au"},
]

personality_questions = [
    {
        "q": "Apa aktivitas yang paling kamu nikmati?",
        "options": {
            "Menulis kode atau memecahkan masalah logika": "Programmer",
            "Membuat desain visual atau ilustrasi": "Designer",
            "Menganalisis data atau angka": "Data Scientist"
        }
    },
    {
        "q": "Kalau kamu kerja dalam tim, biasanya kamu jadi orang yang...",
        "options": {
            "Menjelaskan logika & bikin sistem jalan": "Programmer",
            "Menyusun tampilan biar enak dilihat": "Designer",
            "Ngumpulin data & bikin laporan": "Data Scientist"
        }
    },
    {
        "q": "Skill mana yang paling ingin kamu kembangkan?",
        "options": {
            "Bahasa pemrograman (Python, Java, dll.)": "Programmer",
            "Software desain (Figma, Photoshop, dll.)": "Designer",
            "Statistik & Machine Learning": "Data Scientist"
        }
    },
    {
        "q": "Bagian favorit dari sebuah proyek menurutmu adalah...",
        "options": {
            "Membangun sistem dan logika yang bekerja": "Programmer",
            "Mendesain UI/UX agar menarik": "Designer",
            "Mengolah data jadi insight berguna": "Data Scientist"
        }
    },
    {
        "q": "Kalau dikasih sebuah masalah besar, kamu akan...",
        "options": {
            "Mecah jadi algoritma kecil lalu coding": "Programmer",
            "Visualisasikan masalah dengan sketsa/gambar": "Designer",
            "Kumpulkan data & cari pola": "Data Scientist"
        }
    },
    {
        "q": "Software/tool mana yang lebih sering kamu gunakan?",
        "options": {
            "VS Code, IntelliJ, PyCharm": "Programmer",
            "Figma, Photoshop, Illustrator": "Designer",
            "Excel, Python (pandas), SQL": "Data Scientist"
        }
    },
    {
        "q": "Kalau lihat dashboard dengan banyak angka...",
        "options": {
            "Aku lebih suka coding backend-nya": "Programmer",
            "Aku mau bikin tampilannya lebih indah": "Designer",
            "Aku langsung analisis angka dan cari insight": "Data Scientist"
        }
    },
    {
        "q": "Jenis tugas apa yang menurutmu paling menantang?",
        "options": {
            "Debugging error yang kompleks": "Programmer",
            "Membuat desain yang sesuai keinginan klien": "Designer",
            "Membersihkan dataset besar biar siap dianalisis": "Data Scientist"
        }
    },
    {
        "q": "Kalau punya waktu luang, kamu lebih suka...",
        "options": {
            "Ngoprek open source project": "Programmer",
            "Membuat karya seni/desain baru": "Designer",
            "Baca artikel riset atau data analytics": "Data Scientist"
        }
    },
    {
        "q": "Tujuan karier jangka panjangmu adalah...",
        "options": {
            "Membangun software yang berguna": "Programmer",
            "Menciptakan desain yang impactful": "Designer",
            "Menggunakan data untuk bikin keputusan besar": "Data Scientist"
        }
    }
]

total_perso_q = len(personality_questions)


# ====================== MAIN APP ======================
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
else:
    show_header()  # panggil selalu header

    if st.session_state.sidebar_visible:
        show_sidebar()
    else:
        if st.button("📂 Open Sidebar"):
            st.session_state.sidebar_visible = True
            
    # Render page sesuai state
    if st.session_state.page == "personality":
        personality_quiz()
    elif st.session_state.page == "quiz":
        quiz_page()
    elif st.session_state.page == "profile":
        profile_page()
    elif st.session_state.page == "logout":
        logout()



