import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import load_css, page_header, load_data, display_image, gold_divider

st.set_page_config(page_title="Paket Jalan-jalan — Monggo Pinarak", page_icon="🧳", layout="wide")
load_css()

st.sidebar.page_link("app.py", label="🏠 Kembali ke Beranda")
st.sidebar.markdown("---")

page_header("🧳 Paket Jalan-jalan Solo", "Itinerary lengkap untuk perjalanan tak terlupakan di Solo")

data = load_data("paket.json")

durasi_list = ["-- Pilih Durasi Perjalanan --"] + sorted(list(set(d["durasi"] for d in data)))
selected_durasi = st.selectbox("Pilih Durasi Perjalanan:", durasi_list)

gold_divider()

if selected_durasi == "-- Pilih Durasi Perjalanan --":
    st.info("💡 Silakan pilih durasi perjalanan Anda di atas untuk menampilkan rekomendasi paket itinerary lengkap.")
    st.stop()

filtered = [d for d in data if d["durasi"] == selected_durasi]

for item in filtered:
    # Header paket
    col_info, col_dl = st.columns([3, 1])
    with col_info:
        st.markdown(
            f"<span style='background:#D4AF37;color:#2C1810;font-size:.7rem;font-weight:700;"
            f"padding:3px 12px;border-radius:20px;display:inline-block;margin-right:6px;'>{item['durasi']}</span>"
            f"<span style='background:#8B4513;color:white;font-size:.7rem;font-weight:700;"
            f"padding:3px 12px;border-radius:20px;display:inline-block;'>{item['tema']}</span>",
            unsafe_allow_html=True
        )
        st.markdown(f"### {item['nama']}")
        st.write(item["deskripsi"])
        st.markdown(f"💰 **Estimasi Budget:** {item['budget_estimasi']}")

    with col_dl:
        itinerary_text = f"=== {item['nama']} ===\n"
        itinerary_text += f"Durasi: {item['durasi']} | Tema: {item['tema']}\n"
        itinerary_text += f"Budget: {item['budget_estimasi']}\n\nITINERARY:\n"
        for j in item["itinerary"]:
            itinerary_text += f"  {j['waktu']} — {j['aktivitas']}\n"
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button(
            label="⬇️ Download Itinerary",
            data=itinerary_text,
            file_name=f"itinerary_{item['id']}.txt",
            mime="text/plain",
            key=f"dl_{item['id']}",
            use_container_width=True
        )

    # Itinerary
    st.markdown("**📋 Itinerary:**")
    for j in item["itinerary"]:
        is_day = j["waktu"].startswith("HARI")
        if is_day:
            st.markdown(
                f"<div style='background:linear-gradient(135deg,#8B4513,#C4622D);"
                f"color:white;padding:7px 16px;border-radius:8px;font-weight:700;"
                f"font-size:.88rem;margin:12px 0 6px;'>{j['waktu']}</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div class='itinerary-item'>"
                f"<div class='itinerary-time'>{j['waktu']}</div>"
                f"<div class='itinerary-activity'>{j['aktivitas']}</div>"
                f"</div>",
                unsafe_allow_html=True
            )

    gold_divider()
