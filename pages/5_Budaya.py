import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import load_css, page_header, load_data, display_image

st.set_page_config(page_title="Budaya Solo — Monggo Pinarak", page_icon="🎭", layout="wide")
load_css()

st.sidebar.page_link("app.py", label="🏠 Kembali ke Beranda")
st.sidebar.markdown("---")

page_header("🎭 Budaya Solo", "Warisan seni dan tradisi adiluhung Kota Solo")

data = load_data("budaya.json")

kategori_list = ["Semua"] + sorted(list(set(d["kategori"] for d in data)))
selected_kat = st.selectbox("Filter Kategori", kategori_list)

filtered = data if selected_kat == "Semua" else [d for d in data if d["kategori"] == selected_kat]

st.markdown(f"**{len(filtered)} item budaya**")
st.divider()

for item in filtered:
    col_img, col_info = st.columns([1, 2])
    with col_img:
        display_image(item["foto"], width=280)
    with col_info:
        st.markdown(
            f"<span style='background:#D4AF37;color:#2C1810;font-size:0.7rem;font-weight:700;"
            f"padding:2px 10px;border-radius:20px;display:inline-block;'>{item['kategori']}</span>",
            unsafe_allow_html=True
        )
        st.markdown(f"### {item['nama']}")
        st.write(item["deskripsi"])
        st.caption(f"📍 **Tempat:** {item['tempat']}")
        st.caption(f"📅 **Jadwal:** {item['jadwal']}")
        with st.expander("📖 Baca Artikel Lengkap"):
            st.write(item.get("artikel", "Artikel belum tersedia."))
    st.divider()
