import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import load_css, page_header, load_data, render_card

st.set_page_config(page_title="Kuliner Solo — Monggo Pinarak", page_icon="🍽️", layout="wide")
load_css()

st.sidebar.page_link("app.py", label="🏠 Kembali ke Beranda")
st.sidebar.markdown("---")

page_header("🍽️ Kuliner Solo", "Cita rasa autentik Kota Solo yang menggugah selera")

data = load_data("kuliner.json")

col_f1, col_f2 = st.columns(2)
with col_f1:
    kategori_list = ["Semua"] + sorted(list(set(d["kategori"] for d in data)))
    selected_kat = st.selectbox("Kategori Makanan", kategori_list)
with col_f2:
    waktu_list = ["Semua"] + sorted(list(set(d["waktu"] for d in data)))
    selected_waktu = st.selectbox("Waktu Makan", waktu_list)

filtered = data
if selected_kat != "Semua":
    filtered = [d for d in filtered if d["kategori"] == selected_kat]
if selected_waktu != "Semua":
    filtered = [d for d in filtered if d["waktu"] == selected_waktu]

st.markdown(f"**{len(filtered)} kuliner ditemukan**")
st.divider()

cols = st.columns(3)
for i, item in enumerate(filtered):
    with cols[i % 3]:
        render_card(
            title=item["nama"],
            desc=item["deskripsi"],
            img_path=item["foto"],
            badge=item["waktu"],
            meta=[
                f"💰 {item['harga_rata']}  ·  ⭐ {item['rating']}/5",
                f"📍 {item['lokasi_terbaik']}",
            ]
        )
