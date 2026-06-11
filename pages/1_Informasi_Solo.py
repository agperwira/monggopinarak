import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import load_css, page_header, gold_divider

st.set_page_config(page_title="Informasi Solo — Monggo Pinarak", page_icon="🏰", layout="wide")
load_css()

st.sidebar.page_link("app.py", label="🏠 Kembali ke Beranda")
st.sidebar.markdown("---")

page_header("🏰 Informasi Lengkap Kota Solo", "Mengenal Lebih Dekat Surakarta — Jantung Budaya dan Sejarah Jawa")

# Membuat tab untuk menyusun informasi agar rapi dan interaktif
tab_profil, tab_sejarah, tab_tradisi, tab_transportasi = st.tabs([
    "📍 Profil & Geografi",
    "📜 Sejarah & Kerajaan",
    "🎭 Tradisi & Seni Budaya",
    "🚉 Panduan Transportasi"
])

# ── TAB 1: PROFIL & GEOGRAFI ──────────────────────────────────────────────────
with tab_profil:
    # Fakta singkat dalam bentuk kartu
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

    col_text, col_map = st.columns([1, 1], gap="large")

    with col_text:
        st.markdown("""
        <div class="info-box">
            <h3 style="color:#8B4513; margin-top:0;">Geografi & Batas Wilayah</h3>
            <p style="color:#5D4037; line-height:1.7;">
                <b>Surakarta</b> atau yang lebih populer dengan nama <b>Solo</b> terletak di dataran rendah di lembah 
                Sungai Bengawan Solo. Kota ini secara geografis dikelilingi oleh wilayah penyangga yang dikenal sebagai 
                <b>Solo Raya</b> (Sukoharjo, Karanganyar, Boyolali, Klaten, Sragen, dan Wonogiri).
            </p>
            <p style="color:#5D4037; line-height:1.7;">
                <b>Batas Wilayah Administratif:</b><br>
                <ul>
                    <li><b>Utara:</b> Kabupaten Karanganyar & Kabupaten Boyolali</li>
                    <li><b>Timur:</b> Kabupaten Karanganyar & Kabupaten Sukoharjo</li>
                    <li><b>Selatan:</b> Kabupaten Sukoharjo</li>
                    <li><b>Barat:</b> Kabupaten Karanganyar & Kabupaten Sukoharjo</li>
                </ul>
            </p>
            <p style="color:#5D4037; line-height:1.7;">
                Meskipun wilayahnya relatif kecil dibanding kota besar lain, Solo merupakan kota terpadat di Jawa Tengah, 
                menjadikannya pusat kegiatan ekonomi, pariwisata, dan edukasi yang sangat sibuk.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_map:
        st.markdown("### 🗺️ Peta Interaktif & Landmark Solo")
        try:
            import folium
            from streamlit_folium import st_folium

            m = folium.Map(location=[-7.5705, 110.8243], zoom_start=13, tiles="CartoDB positron")
            lokasi = [
                ("Keraton Kasunanan Surakarta", -7.5756, 110.8243, "🏰"),
                ("Pura Mangkunegaran", -7.5678, 110.8198, "🏛️"),
                ("Pasar Klewer (Pusat Batik)", -7.5748, 110.8228, "🛍️"),
                ("Pasar Gede Hardjonagoro", -7.5697, 110.8282, "🏪"),
                ("Taman Balekambang Solo", -7.5540, 110.8120, "🌳"),
                ("Stasiun Solo Balapan", -7.5568, 110.8216, "🚂"),
                ("Kampung Batik Laweyan", -7.5677, 110.7967, "🎨")
            ]
            for nama, lat, lon, icon in lokasi:
                folium.Marker(
                    [lat, lon],
                    popup=nama,
                    tooltip=f"{icon} {nama}",
                    icon=folium.Icon(color="orange", icon="star"),
                ).add_to(m)

            st_folium(m, width=None, height=350)
        except ImportError:
            st.info("Install streamlit-folium untuk menampilkan peta: `pip install streamlit-folium folium`")

# ── TAB 2: SEJARAH & KERAJAAN ──────────────────────────────────────────────────
with tab_sejarah:
    st.markdown("""
    <div class="info-box">
        <h3 style="color:#8B4513; margin-top:0;">Dua Istana Kembar Kota Solo</h3>
        <p style="color:#5D4037; line-height:1.7;">
            Keunikan utama Kota Solo adalah adanya <b>dua kerajaan aktif</b> yang berdampingan dan terus menjaga 
            adat istiadat Jawa hingga hari ini:
        </p>
        <ol>
            <li>
                <b>Keraton Kasunanan Surakarta Hadiningrat:</b> Didirikan pada tahun 1745 oleh Susuhunan Pakubuwono II 
                sebagai penerus Dinasti Mataram Islam setelah istana Kartasura hancur akibat Geger Pecinan.
            </li>
            <li>
                <b>Pura Mangkunegaran:</b> Istana kadipaten yang didirikan pada tahun 1757 oleh Raden Mas Said 
                (bergelar Mangkunegara I atau Pangeran Sambernyawa) melalui Perjanjian Salatiga.
            </li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    gold_divider()

    st.markdown("### 📜 Timeline Sejarah Perkembangan Solo")
    timeline = [
        ("1745", "Pakubuwono II memindahkan ibukota kerajaan Mataram Islam dari Kartasura ke Desa Sala (cikal bakal kota Solo)"),
        ("1755", "Perjanjian Giyanti membagi Kerajaan Mataram menjadi Kasunanan Surakarta (Solo) dan Kesultanan Yogyakarta"),
        ("1757", "Perjanjian Salatiga mendirikan Kadipaten Mangkunegaran di bawah kepemimpinan Raden Mas Said"),
        ("1945", "Solo menyatakan bergabung dengan Republik Indonesia sebagai Daerah Istimewa Surakarta (DIS) setelah proklamasi"),
        ("1946", "Solo berubah status administratif menjadi Kota Madya Mandiri karena dinamika politik saat itu"),
        ("2005", "Solo mulai meluncurkan slogan <b>'Solo: The Spirit of Java'</b> sebagai kota kebudayaan internasional")
    ]

    for tahun, kejadian in timeline:
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-year">{tahun}</div>
            <div class="timeline-text">{kejadian}</div>
        </div>
        """, unsafe_allow_html=True)

# ── TAB 3: TRADISI & SENI BUDAYA ──────────────────────────────────────────────────
with tab_tradisi:
    st.markdown("### 🎭 Ritual, Tradisi, dan Seni Ikonik Kota Solo")
    
    col_trad1, col_trad2 = st.columns(2, gap="large")
    
    with col_trad1:
        st.markdown("""
        <div class="info-box" style="height: 100%;">
            <h4 style="color:#8B4513; margin-top:0;">✨ Upacara & Ritual Tahunan</h4>
            <ul>
                <li>
                    <b>Kirab Pusaka Malam 1 Suro:</b> Ritual membersihkan dan mengarak pusaka keraton yang dipimpin oleh 
                    <i>Kebo Bule Kyai Slamet</i> (kerbau albino suci milik keraton) pada pergantian tahun baru Jawa.
                </li>
                <li>
                    <b>Upacara Sekaten:</b> Perayaan menyambut kelahiran Nabi Muhammad SAW dengan pasar malam rakyat 
                    dan dibunyikannya gamelan pusaka Kyai Guntur Madu dan Guntur Sari di Masjid Agung Solo.
                </li>
                <li>
                    <b>Grebeg Mulud / Syawal:</b> Prosesi pengarakan 'Gunungan' raksasa berisi hasil bumi dari keraton 
                    menuju Masjid Agung untuk didoakan lalu diperebutkan oleh masyarakat umum.
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_trad2:
        st.markdown("""
        <div class="info-box" style="height: 100%;">
            <h4 style="color:#8B4513; margin-top:0;">🎨 Kesenian & Julukan Ikonik</h4>
            <ul>
                <li>
                    <b>Wayang Orang Sriwedari:</b> Salah satu pertunjukan teater tradisional legendaris yang membawakan 
                    kisah Mahabarata dan Ramayana, masih dipentaskan secara rutin sejak tahun 1911.
                </li>
                <li>
                    <b>Kampung Batik Laweyan & Kauman:</b> Sentra industri batik tulis dan cap bersejarah dengan lorong 
                    sempit bergaya arsitektur kolonial, Jawa, dan Islam.
                </li>
                <li>
                    <b>Solo: The Spirit of Java:</b> Slogan pariwisata resmi yang bermakna bahwa Solo merupakan pusat, 
                    jiwa, dan cerminan dari kebudayaan Jawa yang adiluhung (bernilai tinggi).
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ── TAB 4: PANDUAN TRANSPORTASI ──────────────────────────────────────────────────
with tab_transportasi:
    st.markdown("### 🚉 Cara Terbaik Menuju dan Berkeliling Kota Solo")
    
    t1, t2, t3 = st.columns(3)
    with t1:
        st.markdown("""
        <div class="info-box" style="height: 100%;">
            <h4 style="color:#8B4513; margin-top:0;">🚂 Kereta Api</h4>
            <p style="color:#5D4037; font-size:0.9rem;">
                <b>Stasiun Utama:</b><br>
                - Stasiun Solo Balapan (Kereta Eksekutif & KRL Solo-Jogja)<br>
                - Stasiun Purwosari (Kereta Ekonomi)<br>
                - Stasiun Solo Jebres (Kereta Lintas Utara)
            </p>
            <p style="color:#5D4037; font-size:0.9rem; font-style:italic;">
                Sangat disarankan menggunakan KRL Commuter Line jika Anda bepergian PP dari Yogyakarta.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with t2:
        st.markdown("""
        <div class="info-box" style="height: 100%;">
            <h4 style="color:#8B4513; margin-top:0;">✈️ Jalur Udara</h4>
            <p style="color:#5D4037; font-size:0.9rem;">
                <b>Bandara Utama:</b><br>
                Bandara Internasional Adi Soemarmo (SOC).<br>
                Terletak di Colomadu (Karanganyar) / Ngemplak (Boyolali), berjarak sekitar 20 menit dari pusat Kota Solo via Tol Bandara.
            </p>
            <p style="color:#5D4037; font-size:0.9rem; font-style:italic;">
                Tersedia layanan Kereta Bandara (BIAS) langsung dari Stasiun Solo Balapan menuju terminal bandara.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with t3:
        st.markdown("""
        <div class="info-box" style="height: 100%;">
            <h4 style="color:#8B4513; margin-top:0;">🚌 Bus & Jalur Darat</h4>
            <p style="color:#5D4037; font-size:0.9rem;">
                <b>Terminal & Akses Tol:</b><br>
                - Terminal Tirtonadi (Terminal tipe A terbesar di Jawa Tengah).<br>
                - Akses Tol Trans Jawa (Gerbang Tol Colomadu & GT Gondangrejo) memangkas waktu dari Jakarta menjadi hanya 6-7 jam berkendara.
            </p>
        </div>
        """, unsafe_allow_html=True)

gold_divider()
st.markdown("""
<div style="text-align: center; color: #A0826D; font-size: 0.85rem; margin-top: 1rem;">
    Monggo Pinarak — Jelajah dan Nikmati Keindahan Surakarta Hadiningrat 🏰
</div>
""", unsafe_allow_html=True)
