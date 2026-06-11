import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import load_css, page_header, load_data, render_card

st.set_page_config(page_title="Coffeeshop Solo — Monggo Pinarak", page_icon="☕", layout="wide")
load_css()

st.sidebar.page_link("app.py", label="🏠 Kembali ke Beranda")
st.sidebar.markdown("---")

page_header("☕ Coffeeshop Solo", "Tempat ngopi terbaik di Kota Solo")

data = load_data("coffeeshop.json")

col_f1, col_f2 = st.columns(2)
with col_f1:
    nuansa_list = ["Semua"] + sorted(list(set(d["nuansa"] for d in data)))
    selected_nuansa = st.selectbox("Nuansa Kafe", nuansa_list)
with col_f2:
    wifi_filter = st.selectbox("WiFi", ["Semua", "Ada WiFi", "Tanpa WiFi"])

filtered = data
if selected_nuansa != "Semua":
    filtered = [d for d in filtered if d["nuansa"] == selected_nuansa]
if wifi_filter == "Ada WiFi":
    filtered = [d for d in filtered if d["wifi"]]
elif wifi_filter == "Tanpa WiFi":
    filtered = [d for d in filtered if not d["wifi"]]

st.markdown(f"**{len(filtered)} coffeeshop ditemukan**")
st.divider()

cols = st.columns(3)
for i, item in enumerate(filtered):
    with cols[i % 3]:
        wifi_icon = "📶 Ada WiFi" if item["wifi"] else "📵 Tanpa WiFi"
        render_card(
            title=item["nama"],
            desc=item["deskripsi"],
            img_path=item["foto"],
            badge=item["nuansa"],
            meta=[
                f"💰 {item['harga_rata']}  ·  ⭐ {item['rating']}/5",
                f"{wifi_icon}  ·  🕐 {item['jam_buka']}",
                f"📍 {item['alamat']}",
                f"☕ {item['menu_andalan']}",
            ]
        )
