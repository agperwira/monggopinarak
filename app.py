import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from utils import load_css, load_data, gold_divider

st.set_page_config(
    page_title="Monggo Pinarak — Jelajah Kota Solo",
    page_icon="🏰",
    layout="wide",
    initial_sidebar_state="expanded",
)
load_css()

# ── HERO ──────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">✦ Portal Wisata Resmi ✦</div>
    <div class="hero-title">Monggo Pinarak</div>
    <div class="hero-sub">Selamat Datang di Kota Surakarta — Jantung Budaya Jawa</div>
    <div class="hero-tagline">"Monggo Pinarak" — Silakan Mampir, Nikmati Keindahan Solo</div>
</div>
""", unsafe_allow_html=True)

# ── INTRO ──────────────────────────────────────────────────────
col_l, col_r = st.columns([3, 2], gap="large")

with col_l:
    st.markdown("""
    <div class="info-box">
        <h3 style="color:#8B4513;margin:0 0 .6rem;font-size:1.2rem;font-weight:700;">
            🏯 Tentang Solo
        </h3>
        <p style="color:#5D4037;line-height:1.8;margin:0;">
            <b>Surakarta (Solo)</b> adalah kota budaya bersejarah di Jawa Tengah, rumah bagi
            <b>Keraton Kasunanan</b> dan <b>Kadipaten Mangkunegaran</b>. Dikenal sebagai pusat
            <b>batik</b>, <b>wayang</b>, <b>gamelan</b>, dan kuliner autentik Jawa yang tak tertandingi.
        </p>
        <p style="color:#5D4037;line-height:1.8;margin:.6rem 0 0;">
            Gunakan portal ini untuk merencanakan perjalanan terbaik Anda ke Solo —
            dari destinasi wisata hingga itinerary lengkap siap pakai.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_r:
    # Quick facts
    facts = [
        ("📍", "Jawa Tengah, Indonesia"),
        ("🗓️", "Berdiri sejak 1745"),
        ("👥", "±570.000 jiwa"),
        ("🌡️", "27–32°C sepanjang tahun"),
        ("🚂", "2 stasiun kereta aktif"),
    ]
    for icon, text in facts:
        st.markdown(
            f"<div style='display:flex;align-items:center;gap:10px;padding:7px 12px;"
            f"background:white;border-radius:8px;margin-bottom:6px;"
            f"border:1px solid #E8D5B0;box-shadow:0 1px 4px rgba(139,69,19,.08);'>"
            f"<span style='font-size:1.1rem;'>{icon}</span>"
            f"<span style='color:#3E2723;font-size:0.88rem;'>{text}</span></div>",
            unsafe_allow_html=True
        )

gold_divider()

# ── MENU UTAMA ─────────────────────────────────────────────────
st.markdown(
    "<h2 style='color:#8B4513;font-size:1.4rem;font-weight:800;"
    "margin-bottom:1.2rem;'>🗂️ Jelajahi Solo</h2>",
    unsafe_allow_html=True
)

menus = [
    ("🏰", "Informasi Solo",     "Sejarah, fakta & transportasi",        "pages/1_Informasi_Solo.py"),
    ("🗺️", "Wisata",             "Destinasi wisata terbaik",              "pages/2_Wisata_Solo.py"),
    ("🍽️", "Kuliner",            "Cita rasa autentik Solo",               "pages/3_Kuliner.py"),
    ("☕",  "Coffeeshop",        "Tempat ngopi estetik",                  "pages/4_Coffeeshop.py"),
    ("🎭", "Budaya",             "Seni & tradisi adiluhung",              "pages/5_Budaya.py"),
    ("🎁", "Oleh-oleh",         "Buah tangan khas Solo",                 "pages/6_Oleh_Oleh.py"),
    ("🧳", "Paket Jalan-jalan", "Itinerary lengkap siap pakai",          "pages/7_Paket_Jalan_Jalan.py"),
]

# Baris 1 — 4 kolom
cols1 = st.columns(4, gap="medium")
for i, (icon, name, desc, page) in enumerate(menus[:4]):
    with cols1[i]:
        st.markdown(
            f"<div class='menu-card'>"
            f"<div class='menu-icon'>{icon}</div>"
            f"<div class='menu-name'>{name}</div>"
            f"<div class='menu-desc'>{desc}</div>"
            f"</div>",
            unsafe_allow_html=True
        )
        st.page_link(page, label=f"Buka →", use_container_width=True)

st.markdown("<div style='height:.6rem'></div>", unsafe_allow_html=True)

# Baris 2 — 3 kolom (tengah)
_, c1, c2, c3, _ = st.columns([0.5, 1, 1, 1, 0.5], gap="medium")
for col, (icon, name, desc, page) in zip([c1, c2, c3], menus[4:]):
    with col:
        st.markdown(
            f"<div class='menu-card'>"
            f"<div class='menu-icon'>{icon}</div>"
            f"<div class='menu-name'>{name}</div>"
            f"<div class='menu-desc'>{desc}</div>"
            f"</div>",
            unsafe_allow_html=True
        )
        st.page_link(page, label=f"Buka →", use_container_width=True)

gold_divider()

# ── STATISTIK ──────────────────────────────────────────────────
st.markdown(
    "<h2 style='color:#8B4513;font-size:1.4rem;font-weight:800;"
    "margin-bottom:1.2rem;'>📊 Konten Tersedia</h2>",
    unsafe_allow_html=True
)

stats = [
    ("wisata.json",    "🗺️", "Destinasi Wisata"),
    ("kuliner.json",   "🍽️", "Menu Kuliner"),
    ("coffeeshop.json","☕",  "Coffeeshop"),
    ("budaya.json",    "🎭", "Budaya"),
    ("oleholeh.json",  "🎁", "Oleh-oleh"),
    ("paket.json",     "🧳", "Paket Wisata"),
]

scols = st.columns(6, gap="small")
for col, (fname, icon, label) in zip(scols, stats):
    n = len(load_data(fname))
    with col:
        st.markdown(
            f"<div class='stat-card'>"
            f"<div class='stat-icon'>{icon}</div>"
            f"<div class='stat-number'>{n}</div>"
            f"<div class='stat-label'>{label}</div>"
            f"</div>",
            unsafe_allow_html=True
        )

gold_divider()

# ── WHY SOLO ───────────────────────────────────────────────────
st.markdown(
    "<h2 style='color:#8B4513;font-size:1.4rem;font-weight:800;"
    "margin-bottom:1.2rem;'>✨ Mengapa Solo?</h2>",
    unsafe_allow_html=True
)

reasons = [
    ("🏯", "Warisan Kerajaan", "Dua keraton aktif dengan tradisi 300 tahun yang masih terjaga hingga kini."),
    ("🍜", "Surga Kuliner", "Nasi Liwet, Sate Buntel, Timlo — cita rasa autentik yang wajib dicoba."),
    ("🎨", "Pusat Batik", "Kampung Batik Laweyan & Kauman — penghasil batik terbaik di Indonesia."),
    ("🎵", "Seni Tradisi", "Gamelan, wayang kulit, dan tari Jawa yang diakui UNESCO."),
    ("🛍️", "Belanja Murah", "Pasar Klewer & Triwindu — pusat oleh-oleh dengan harga terbaik."),
    ("☕", "Kafe Estetik", "Ratusan coffeeshop heritage dan modern tersebar di seluruh kota."),
]

rcols = st.columns(3, gap="medium")
for i, (icon, title, text) in enumerate(reasons):
    with rcols[i % 3]:
        st.markdown(
            f"<div style='background:white;border-radius:10px;padding:1.2rem;"
            f"border:1px solid #E8D5B0;box-shadow:0 1px 6px rgba(139,69,19,.08);"
            f"margin-bottom:1rem;'>"
            f"<div style='font-size:1.6rem;margin-bottom:.4rem;'>{icon}</div>"
            f"<div style='font-weight:700;color:#8B4513;font-size:.95rem;"
            f"margin-bottom:.3rem;'>{title}</div>"
            f"<div style='color:#795548;font-size:.83rem;line-height:1.55;'>{text}</div>"
            f"</div>",
            unsafe_allow_html=True
        )

# ── FOOTER ────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <p style="font-size:1.05rem;font-weight:700;color:#8B4513;margin:0;">🏰 Monggo Pinarak</p>
    <p style="font-size:.82rem;color:#795548;margin:.3rem 0;">
        Portal Wisata Kota Surakarta — Dibuat dengan ❤️ untuk mempromosikan budaya Solo
    </p>
    <p style="font-size:.75rem;color:#A0826D;margin:0;">
        ⚙️ Kelola konten melalui <b>Admin Panel</b> di sidebar
    </p>
</div>
""", unsafe_allow_html=True)
