import streamlit as st
import sys
from pathlib import Path

# Membuka akses ke folder utama agar bisa import utils
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import load_css, page_header, gold_divider

# Set konfigurasi halaman
st.set_page_config(
    page_title="Kuis Solo — Monggo Pinarak",
    page_icon="🎓",
    layout="wide"
)

# Load CSS custom dari repositori
load_css()

# Menu kembali ke beranda di sidebar
st.sidebar.page_link("app.py", label="🏠 Kembali ke Beranda")
st.sidebar.markdown("---")

# Header Halaman
page_header("🎓 Kuis Interaktif Solo", "Uji pengetahuanmu tentang kota budaya Surakarta!")

# Menginisialisasi session state untuk menyimpan status kuis
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'selected_answers' not in st.session_state:
    st.session_state.selected_answers = {}
if 'quiz_finished' not in st.session_state:
    st.session_state.quiz_finished = False

# Fungsi untuk melakukan rerun dengan aman di berbagai versi Streamlit
def safe_rerun():
    try:
        st.rerun()
    except AttributeError:
        st.experimental_rerun()

# Daftar 10 pertanyaan kuis tentang Solo
QUESTIONS = [
    {
        "question": "Di lembah sungai manakah kota Solo (Surakarta) berada?",
        "options": ["Sungai Bengawan Solo", "Sungai Ciliwung", "Sungai Brantas", "Sungai Serayu"],
        "answer": "Sungai Bengawan Solo",
        "hint": "Ingat lagu keroncong terkenal ciptaan Gesang!"
    },
    {
        "question": "Tahun berapakah Keraton Kasunanan Surakarta didirikan?",
        "options": ["1945", "1830", "1745", "1757"],
        "answer": "1745",
        "hint": "Dua ratus tahun sebelum Indonesia merdeka."
    },
    {
        "question": "Dua kerajaan/kadipaten aktif yang menjaga budaya di Solo saat ini adalah...",
        "options": [
            "Kesultanan Yogyakarta & Pakualaman",
            "Kasunanan Surakarta & Kadipaten Mangkunegaran",
            "Kerajaan Pajang & Demak",
            "Kasultanan Cirebon & Banten"
        ],
        "answer": "Kasunanan Surakarta & Kadipaten Mangkunegaran",
        "hint": "Keduanya didirikan berdasarkan Perjanjian Giyanti dan Salatiga."
    },
    {
        "question": "Apa nama dua kampung batik legendaris dan bersejarah di Solo?",
        "options": [
            "Campung Trusmi & Pekalongan",
            "Kampung Laweyan & Kauman",
            "Kampung Kotagede & Malioboro",
            "Kampung Tegalgendu & Giriloyo"
        ],
        "answer": "Kampung Laweyan & Kauman",
        "hint": "Salah satunya terkenal dengan perkumpulan saudagar batik muslim zaman dahulu."
    },
    {
        "question": "Perjanjian bersejarah tahun 1755 yang membagi kerajaan Mataram Islam menjadi Surakarta dan Yogyakarta adalah...",
        "options": ["Perjanjian Salatiga", "Perjanjian Giyanti", "Perjanjian Kartasura", "Perjanjian Bongaya"],
        "answer": "Perjanjian Giyanti",
        "hint": "Namanya diambil dari nama sebuah desa di timur Surakarta (sekarang Karanganyar)."
    },
    {
        "question": "Siapakah tokoh nasional kelahiran Solo yang menjabat sebagai Presiden ke-7 Republik Indonesia?",
        "options": ["Joko Widodo", "Soekarno", "Susilo Bambang Yudhoyono", "B.J. Habibie"],
        "answer": "Joko Widodo",
        "hint": "Beliau juga pernah menjabat sebagai Walikota Solo dan Gubernur DKI Jakarta."
    },
    {
        "question": "Apa nama stasiun kereta api utama di kota Solo yang namanya dijadikan judul lagu campursari legendaris?",
        "options": ["Stasiun Purwosari", "Stasiun Solo Jebres", "Stasiun Solo Balapan", "Stasiun Solo Kota"],
        "answer": "Stasiun Solo Balapan",
        "hint": "Lagu tersebut dinyanyikan oleh Didi Kempot."
    },
    {
        "question": "Selat Solo adalah hidangan khas yang merupakan akulturasi (perpaduan) antara kuliner Jawa dengan kuliner...",
        "options": ["Belanda (Eropa)", "Tiongkok (Cina)", "Arab", "India"],
        "answer": "Belanda (Eropa)",
        "hint": "Nama 'Selat' berasal dari kata 'Sla' atau 'Salad' dalam bahasa Belanda."
    },
    {
        "question": "Pura Mangkunegaran didirikan oleh Raden Mas Said. Siapa julukan terkenal beliau karena keberaniannya berperang?",
        "options": ["Pangeran Sambernyawa", "Pangeran Diponegoro", "Sultan Agung", "Paku Buwono VI"],
        "answer": "Pangeran Sambernyawa",
        "hint": "Julukan ini diberikan oleh Belanda karena pasukannya yang bergerak cepat dan mematikan."
    },
    {
        "question": "Pasar tradisional di kota Solo yang menjadi pusat perdagangan batik terbesar dan legendaris adalah...",
        "options": ["Pasar Gede", "Pasar Klewer", "Pasar Triwindu", "Pasar Depok"],
        "answer": "Pasar Klewer",
        "hint": "Lokasinya terletak sangat dekat dengan Alun-Alun Utara dan Masjid Agung Surakarta."
    }
]

# Fungsi untuk me-reset kuis
def reset_quiz():
    st.session_state.quiz_started = True
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.selected_answers = {}
    st.session_state.quiz_finished = False

# TAMPILAN 1: HALAMAN MULAI
if not st.session_state.quiz_started:
    st.markdown("""
    <div class="info-box" style="text-align: center; padding: 2.5rem; margin-bottom: 1.5rem;">
        <h2 style="color:#8B4513; margin-top:0;">🎮 Uji Pengetahuanmu!</h2>
        <p style="color:#5D4037; font-size: 1.1rem; line-height: 1.7;">
            Apakah kamu sudah membaca halaman <b>Informasi Solo</b> dan <b>Wisata Solo</b>?<br>
            Mari kita lihat seberapa baik pemahamanmu tentang sejarah, budaya, dan geografi Kota Surakarta!
        </p>
        <p style="color:#795548; font-size: 0.9rem;">
            Total Pertanyaan: <b>10 Soal Pilihan Ganda</b>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_start, _ = st.columns([1, 3])
    with col_start:
        if st.button("🚀 Mulai Kuis Sekarang!", use_container_width=True, type="primary"):
            st.session_state.quiz_started = True
            safe_rerun()

# TAMPILAN 2: SEDANG MENGERJAKAN SOAL
elif st.session_state.quiz_started and not st.session_state.quiz_finished:
    q_idx = st.session_state.current_question
    q_data = QUESTIONS[q_idx]
    
    # Progress Bar
    progress = (q_idx) / len(QUESTIONS)
    st.progress(progress, text=f"Pertanyaan {q_idx + 1} dari {len(QUESTIONS)}")
    
    st.markdown(f"""
    <div style="background: white; border-radius: 10px; padding: 1.5rem; border: 1px solid #E8D5B0; margin-bottom: 1.5rem; box-shadow:0 2px 5px rgba(0,0,0,0.05);">
        <span style="background: #8B4513; color: white; padding: 3px 8px; border-radius: 5px; font-size: 0.8rem; font-weight: bold;">SOAL {q_idx + 1}</span>
        <h3 style="color: #3E2723; margin-top: 0.8rem; font-weight: 700;">{q_data['question']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Radio button pilihan jawaban
    selected = st.radio(
        "Pilih jawaban yang menurutmu benar:",
        options=q_data["options"],
        index=None,
        key=f"q_radio_{q_idx}"
    )
    
    # Petunjuk (Hint)
    with st.expander("💡 Butuh Bantuan? Tampilkan Petunjuk"):
        st.info(q_data["hint"])
        
    gold_divider()
    
    # Navigasi tombol
    col_prev, col_next = st.columns([1, 1])
    
    with col_next:
        if selected:
            btn_text = "Pertanyaan Berikutnya ➡️" if q_idx < len(QUESTIONS) - 1 else "🏁 Kirim Jawaban!"
            if st.button(btn_text, use_container_width=True, type="primary"):
                # Simpan jawaban
                st.session_state.selected_answers[q_idx] = selected
                
                # Cek jika benar
                if selected == q_data["answer"]:
                    st.session_state.score += 1
                
                # Pindah ke pertanyaan berikutnya atau selesai
                if q_idx < len(QUESTIONS) - 1:
                    st.session_state.current_question += 1
                else:
                    st.session_state.quiz_finished = True
                safe_rerun()
        else:
            st.button("Pilih salah satu jawaban untuk melanjutkan", disabled=True, use_container_width=True)

# TAMPILAN 3: KUIS SELESAI (HASIL AKHIR)
elif st.session_state.quiz_finished:
    total_score = st.session_state.score
    percentage = int((total_score / len(QUESTIONS)) * 100)
    
    # Perbaikan bug DeltaGenerator: Menggunakan standard if statement
    if percentage >= 80:
        st.balloons()
    
    st.markdown("### 🏁 Hasil Skor Kuis Kamu")
    
    # Kartu Hasil Skor
    color_score = "#2E7D32" if percentage >= 80 else ("#EF6C00" if percentage >= 50 else "#C62828")
    
    st.markdown(f"""
    <div style="background: white; border-radius: 12px; padding: 2rem; border: 2px solid {color_score}; text-align: center; margin-bottom: 1.5rem;">
        <h1 style="color: {color_score}; font-size: 3.5rem; margin: 0;">{percentage}%</h1>
        <p style="color: #5D4037; font-size: 1.2rem; font-weight: bold; margin: 0.5rem 0 1.5rem 0;">
            Kamu menjawab benar {total_score} dari {len(QUESTIONS)} pertanyaan!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feedback Teks
    if percentage == 100:
        st.success("🎉 LUAR BIASA! Kamu menjawab semua pertanyaan dengan sempurna! Kamu adalah Ahli Budaya Solo!")
    elif percentage >= 80:
        st.success("👏 Hebat sekali! Pemahamanmu tentang kota Solo sudah sangat baik!")
    elif percentage >= 60:
        st.warning("👍 Cukup bagus! Kamu sudah memahami dasar-dasar sejarah kota Solo.")
    else:
        st.error("📚 Yuk baca lagi halaman **Informasi Solo** agar ingatanmu semakin kuat!")
        
    gold_divider()
    
    # Review Jawaban
    st.markdown("### 🔍 Evaluasi Jawaban:")
    for i, q_data in enumerate(QUESTIONS):
        user_ans = st.session_state.selected_answers.get(i, "Tidak dijawab")
        correct_ans = q_data["answer"]
        is_correct = (user_ans == correct_ans)
        
        status_icon = "✅" if is_correct else "❌"
        status_color = "green" if is_correct else "red"
        
        st.markdown(f"""
        **Soal {i+1}:** {q_data['question']}  
        * Jawaban Kamu: <span style="color:{status_color}; font-weight:bold;">{user_ans} {status_icon}</span>  
        * Jawaban Benar: **{correct_ans}**  
        ---
        """, unsafe_allow_html=True)
        
    # Tombol Ulangi Kuis
    col_reset, _ = st.columns([1, 2])
    with col_reset:
        if st.button("🔄 Ulangi Kuis", use_container_width=True, type="primary"):
            reset_quiz()
            safe_rerun()

# Footer
st.markdown("""
<div style="text-align: center; color: #A0826D; font-size: 0.85rem; margin-top: 2rem;">
    Monggo Pinarak - Portal Edukasi & Wisata Kota Surakarta 🏰
</div>
""", unsafe_allow_html=True)
