import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import load_css, page_header, load_data, render_card

st.set_page_config(page_title="Oleh-oleh Solo — Monggo Pinarak", page_icon="🎁", layout="wide")
load_css()

page_header("🎁 Oleh-oleh Solo", "Buah tangan khas Kota Solo untuk orang tersayang")

data = load_data("oleholeh.json")

kategori_list = ["Semua"] + sorted(list(set(d["kategori"] for d in data)))
selected_kat = st.selectbox("Filter Kategori", kategori_list)
filtered = data if selected_kat == "Semua" else [d for d in data if d["kategori"] == selected_kat]

st.markdown(f"**{len(filtered)} oleh-oleh ditemukan**")
st.divider()

cols = st.columns(3)
for i, item in enumerate(filtered):
    with cols[i % 3]:
        render_card(
            title=item["nama"],
            desc=item["deskripsi"],
            img_path=item["foto"],
            badge=item["kategori"],
            meta=[
                f"💰 {item['harga_rata']}",
                f"🏪 {item['toko_rekomendasi']}",
            ]
        )
        with st.expander("💡 Tips Membeli"):
            st.write(item.get("tips", "—"))
