import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import load_css, page_header, gold_divider

st.set_page_config(page_title="Informasi Solo — Monggo Pinarak", page_icon="🏰", layout="wide")
load_css()

page_header("🏰 Informasi Kota Solo", "Mengenal Surakarta — Kota Budaya di Jantung Jawa")

# Fakta singkat
col1, col2, col3, col4 = st.columns(4)
stats = [
    ("44.04 km²", "Luas Wilayah"),
    ("±570.000", "Jumlah Penduduk"),
    ("1745", "Tahun Berdiri"),
    ("5 Kecamatan", "Wilayah Adm."),
]
for col, (num, label) in zip([col1, col2, col3, col4], stats):
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{num}</div>
            <div class="stat-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

gold_divider()

# Dua kolom: deskripsi + peta
col_text, col_map = st.columns([1, 1])

with col_text:
    st.markdown("""
    <div class="info-box">
        <h3 style="color:#8B4513; font-family:'Playfair Display',serif;">Tentang Surakarta</h3>
        <p style="color:#5D4037; line-height:1.8;">
        <b>Surakarta</b> atau yang lebih dikenal dengan nama <b>Solo</b> adalah kota budaya terbesar
        di Jawa Tengah. Terletak di lembah Sungai Bengawan Solo, kota ini menyimpan kekayaan sejarah
        kerajaan Mataram Islam yang tak ternilai.
        </p>
        <p style="color:#5D4037; line-height:1.8;">
        Solo adalah rumah bagi dua kerajaan yang masih aktif hingga kini —
        <b>Keraton Kasunanan Surakarta</b> dan <b>Kadipaten Mangkunegaran</b>.
        Keduanya menjaga tradisi seni, budaya, dan adat istiadat Jawa yang adiluhung.
        </p>
        <p style="color:#5D4037; line-height:1.8;">
        Dikenal sebagai kota <b>batik</b>, <b>wayang</b>, dan <b>kuliner</b>, Solo juga merupakan
        kota kelahiran para tokoh nasional, termasuk Presiden Joko Widodo.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_map:
    try:
        import folium
        from streamlit_folium import st_folium

        m = folium.Map(location=[-7.5755, 110.8243], zoom_start=13, tiles="CartoDB positron")
        lokasi = [
            ("Keraton Kasunanan", -7.5756, 110.8243, "🏰"),
            ("Pura Mangkunegaran", -7.5678, 110.8198, "🏛️"),
            ("Pasar Klewer", -7.5748, 110.8228, "🛍️"),
            ("Pasar Gede", -7.5697, 110.8282, "🏪"),
            ("Taman Balekambang", -7.5540, 110.8120, "🌳"),
        ]
        for nama, lat, lon, icon in lokasi:
            folium.Marker(
                [lat, lon],
                popup=nama,
                tooltip=f"{icon} {nama}",
                icon=folium.Icon(color="orange", icon="star"),
            ).add_to(m)

        st_folium(m, width=None, height=380)
    except ImportError:
        st.info("Install streamlit-folium untuk menampilkan peta: `pip install streamlit-folium folium`")

gold_divider()

# Timeline sejarah
st.markdown("### 📜 Timeline Sejarah Solo")

timeline = [
    ("1745", "Keraton Kasunanan didirikan oleh Paku Buwono II setelah perjanjian Giyanti"),
    ("1755", "Perjanjian Giyanti — Kerajaan Mataram dibagi menjadi Kasunanan Surakarta dan Kesultanan Yogyakarta"),
    ("1757", "Perjanjian Salatiga — Kadipaten Mangkunegaran berdiri di bawah Raden Mas Said (Mangkunegara I)"),
    ("1830", "Solo berkembang pesat sebagai pusat perdagangan dan kebudayaan Jawa"),
    ("1902", "Jalur kereta api Solo-Batavia dibuka, mempercepat pertumbuhan ekonomi"),
    ("1945", "Solo menjadi bagian Republik Indonesia pasca proklamasi kemerdekaan"),
    ("1968", "Solo ditetapkan sebagai kotamadya mandiri"),
    ("2000-an", "Solo bangkit sebagai kota budaya, wisata, dan MICE nasional"),
]

for tahun, kejadian in timeline:
    st.markdown(f"""
    <div class="timeline-item">
        <div class="timeline-year">{tahun}</div>
        <div class="timeline-text">{kejadian}</div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# Transportasi
st.markdown("### 🚉 Cara ke Solo")
t1, t2, t3 = st.columns(3)
with t1:
    st.markdown("""
    **🚂 Kereta Api**
    - Stasiun Solo Balapan (utama)
    - Stasiun Purwosari
    - Terhubung ke Jakarta, Surabaya, Yogyakarta, Bandung
    """)
with t2:
    st.markdown("""
    **✈️ Pesawat**
    - Bandara Adisumarmo (SOC)
    - ±30 menit dari pusat kota
    - Penerbangan dari Jakarta, Bali, Surabaya
    """)
with t3:
    st.markdown("""
    **🚌 Bus & Darat**
    - Terminal Tirtonadi (terbesar di Jawa Tengah)
    - Tol Trans Jawa akses mudah
    - ±8 jam dari Jakarta via tol
    """)
