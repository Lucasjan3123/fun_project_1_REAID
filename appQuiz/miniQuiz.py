import streamlit as st

# ====================== INIT SESSION ======================
if "sidebar_visible" not in st.session_state:
    st.session_state.sidebar_visible = False

if "page" not in st.session_state:
    st.session_state.page = "quiz"

# ====================== CUSTOM STYLE ======================
sidebar_style = """
<style>
[data-testid="stSidebar"] {
    padding: 0;
    background: linear-gradient(to bottom, white 20%, #1E90FF 20%);
    border: 2px solid black;
    border-radius: 8px;
}
.sidebar-title {
    text-align: center;
    padding: 20px;
    font-size: 22px;
    font-weight: bold;
    color: #333;
}
.sidebar-buttons {
    padding: 20px 15px;
}
.stButton>button {
    display: block;
    width: 100%;
    padding: 12px 20px;
    margin: 10px 0;
    text-align: center;
    border: 2px solid black;
    border-radius: 20px;
    background-color: white;
    color: black;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #f0f0f0;
}
</style>
"""

# ====================== TOGGLE SIDEBAR ======================
def show_sidebar():
    st.markdown(sidebar_style, unsafe_allow_html=True)
    st.sidebar.markdown('<div class="sidebar-title">📌 Menu</div>', unsafe_allow_html=True)
    st.sidebar.markdown('<div class="sidebar-buttons">', unsafe_allow_html=True)

    if st.sidebar.button("🎯 Quiz"):
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

# ====================== PROFILE PAGE ======================
def profile_page():
    st.title("👤 Profile")
    st.write("Ini halaman profil user.")

# ====================== LOGOUT PAGE ======================
def logout_page():
    st.title("🚪 Logout")
    st.warning("Kamu sudah keluar dari website.")
    st.stop()

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

# ====================== MAIN ======================
show_header()  # panggil selalu header

if st.session_state.sidebar_visible:
    show_sidebar()
else:
    if st.button("📂 Open Sidebar"):
        st.session_state.sidebar_visible = True

# Render page sesuai state
if st.session_state.page == "quiz":
    quiz_page()
elif st.session_state.page == "profile":
    profile_page()
elif st.session_state.page == "logout":
    logout_page()
