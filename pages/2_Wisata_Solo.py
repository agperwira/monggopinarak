import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import load_css, page_header, load_data, render_card

st.set_page_config(page_title="Wisata Solo — Monggo Pinarak", page_icon="🗺️", layout="wide")
load_css()

st.sidebar.page_link("app.py", label="🏠 Kembali ke Beranda")
st.sidebar.markdown("---")

page_header("🗺️ Wisata Solo", "Destinasi terbaik yang wajib dikunjungi di Kota Solo")

data = load_data("wisata.json")

kategori_list = ["Semua"] + sorted(list(set(d["kategori"] for d in data)))
selected_kat = st.selectbox("Filter Kategori", kategori_list)
if selected_kat != "Semua":
    data = [d for d in data if d["kategori"] == selected_kat]

st.markdown(f"**{len(data)} destinasi ditemukan**")
st.divider()

cols = st.columns(3)
for i, item in enumerate(data):
    with cols[i % 3]:
        render_card(
            title=item["nama"],
            desc=item["deskripsi"],
            img_path=item["foto"],
            badge=item["kategori"],
            meta=[
                f"🎟️ {item['harga_tiket']}  ·  ⭐ {item['rating']}/5",
                f"🕐 {item['jam_buka']}",
                f"📍 {item['alamat']}",
            ]
        )
        with st.expander("💡 Tips"):
            st.write(item.get("tips", "—"))

st.divider()
st.markdown("### 🗺️ Peta Destinasi Wisata Solo")
try:
    import folium
    from streamlit_folium import st_folium
    m = folium.Map(location=[-7.5700, 110.8200], zoom_start=14, tiles="CartoDB positron")
    colors = {"Budaya & Sejarah": "red", "Belanja": "blue", "Alam & Rekreasi": "green"}
    for item in load_data("wisata.json"):
        lat = item.get("lat")
        lon = item.get("lon")
        if lat and lon and lat != 0.0 and lon != 0.0:
            folium.Marker(
                [lat, lon],
                popup=folium.Popup(f"<b>{item['nama']}</b><br>{item['alamat']}<br>Tiket: {item['harga_tiket']}", max_width=200),
                tooltip=f"🏛️ {item['nama']}",
                icon=folium.Icon(color=colors.get(item["kategori"], "orange"), icon="info-sign"),
            ).add_to(m)
    st_folium(m, width=None, height=450)
except ImportError:
    st.info("Install: `pip install streamlit-folium folium`")
