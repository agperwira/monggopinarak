import streamlit as st
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import load_css, page_header, load_data, save_data, save_uploaded_image, ADMIN_PASSWORD

st.set_page_config(page_title="Admin Panel — Monggo Pinarak", page_icon="⚙️", layout="wide")
load_css()

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

if not st.session_state.admin_logged_in:
    st.markdown("""
    <div class="page-header">
        <h1>⚙️ Admin Panel</h1>
        <p>Kelola konten website Monggo Pinarak</p>
    </div>
    """, unsafe_allow_html=True)
    pwd = st.text_input("Masukkan Password Admin", type="password")
    if st.button("Login"):
        if pwd == ADMIN_PASSWORD:
            st.session_state.admin_logged_in = True
            st.rerun()
        else:
            st.error("Password salah!")
    st.stop()

# ===== ADMIN PANEL =====
page_header("⚙️ Admin Panel", "Kelola konten Monggo Pinarak")

if st.button("🚪 Logout"):
    st.session_state.admin_logged_in = False
    st.rerun()

st.sidebar.page_link("app.py", label="🏠 Kembali ke Beranda")
st.sidebar.markdown("---")
menu = st.sidebar.radio("Kelola Konten", [
    "🗺️ Wisata",
    "🍽️ Kuliner",
    "☕ Coffeeshop",
    "🎭 Budaya",
    "🎁 Oleh-oleh",
    "🧳 Paket Jalan-jalan",
])

# ===== MAPPING =====
config = {
    "🗺️ Wisata": {
        "file": "wisata.json",
        "category": "wisata",
        "fields": [
            ("nama", "Nama Tempat", "text"),
            ("kategori", "Kategori", "select", ["Budaya & Sejarah", "Alam & Rekreasi", "Belanja", "Hiburan"]),
            ("deskripsi", "Deskripsi", "textarea"),
            ("alamat", "Alamat", "text"),
            ("jam_buka", "Jam Buka", "text"),
            ("harga_tiket", "Harga Tiket", "text"),
            ("rating", "Rating (1-5)", "number"),
            ("lat", "Latitude", "number"),
            ("lon", "Longitude", "number"),
            ("tips", "Tips Kunjungan", "textarea"),
        ],
    },
    "🍽️ Kuliner": {
        "file": "kuliner.json",
        "category": "kuliner",
        "fields": [
            ("nama", "Nama Makanan", "text"),
            ("kategori", "Kategori", "select", ["Makanan Utama", "Jajanan", "Minuman", "Dessert"]),
            ("waktu", "Waktu Makan", "select", ["Sarapan", "Makan Siang", "Makan Malam", "Malam"]),
            ("deskripsi", "Deskripsi", "textarea"),
            ("harga_rata", "Harga Rata-rata", "text"),
            ("lokasi_terbaik", "Lokasi Terbaik", "textarea"),
            ("rating", "Rating (1-5)", "number"),
        ],
    },
    "☕ Coffeeshop": {
        "file": "coffeeshop.json",
        "category": "coffeeshop",
        "fields": [
            ("nama", "Nama Kafe", "text"),
            ("nuansa", "Nuansa", "select", ["Klasik Jawa", "Heritage", "Modern", "Instagramable", "Tradisional"]),
            ("deskripsi", "Deskripsi", "textarea"),
            ("alamat", "Alamat", "text"),
            ("jam_buka", "Jam Buka", "text"),
            ("harga_rata", "Harga Rata-rata", "text"),
            ("wifi", "Ada WiFi?", "bool"),
            ("rating", "Rating (1-5)", "number"),
            ("menu_andalan", "Menu Andalan", "text"),
        ],
    },
    "🎭 Budaya": {
        "file": "budaya.json",
        "category": "budaya",
        "fields": [
            ("nama", "Nama Budaya", "text"),
            ("kategori", "Kategori", "select", ["Seni Pertunjukan", "Kerajinan", "Seni Tari", "Upacara Adat", "Seni Musik"]),
            ("deskripsi", "Deskripsi", "textarea"),
            ("tempat", "Tempat", "text"),
            ("jadwal", "Jadwal", "text"),
            ("artikel", "Artikel Lengkap", "textarea"),
        ],
    },
    "🎁 Oleh-oleh": {
        "file": "oleholeh.json",
        "category": "oleholeh",
        "fields": [
            ("nama", "Nama Produk", "text"),
            ("kategori", "Kategori", "select", ["Makanan", "Kerajinan", "Minuman"]),
            ("deskripsi", "Deskripsi", "textarea"),
            ("harga_rata", "Harga Rata-rata", "text"),
            ("toko_rekomendasi", "Toko Rekomendasi", "textarea"),
            ("tips", "Tips Membeli", "textarea"),
        ],
    },
    "🧳 Paket Jalan-jalan": {
        "file": "paket.json",
        "category": "paket",
        "fields": [
            ("nama", "Nama Paket", "text"),
            ("durasi", "Durasi", "select", ["1 Hari", "2 Hari", "3 Hari", "4 Hari", "5 Hari"]),
            ("tema", "Tema", "text"),
            ("budget_estimasi", "Estimasi Budget", "text"),
            ("deskripsi", "Deskripsi", "textarea"),
        ],
    },
}

cfg = config[menu]
data = load_data(cfg["file"])

tab1, tab2, tab3 = st.tabs(["➕ Tambah Baru", "✏️ Edit / Hapus", "📋 Lihat Semua Data"])

# ===== TAB 1: TAMBAH =====
with tab1:
    st.markdown(f"### Tambah {menu}")
    st.markdown('<div class="admin-section">', unsafe_allow_html=True)

    new_item = {}
    for field in cfg["fields"]:
        key, label, ftype = field[0], field[1], field[2]
        if ftype == "text":
            new_item[key] = st.text_input(label, key=f"add_{key}")
        elif ftype == "textarea":
            new_item[key] = st.text_area(label, key=f"add_{key}", height=100)
        elif ftype == "select":
            options = field[3]
            new_item[key] = st.selectbox(label, options, key=f"add_{key}")
        elif ftype == "number":
            if key == "rating":
                new_item[key] = st.number_input(label, min_value=1.0, max_value=5.0, value=5.0, step=0.1, key=f"add_{key}")
            else:
                new_item[key] = st.number_input(label, key=f"add_{key}", step=0.1)
        elif ftype == "bool":
            new_item[key] = st.checkbox(label, key=f"add_{key}")

    # Upload foto
    st.markdown("**📷 Upload Foto**")
    uploaded = st.file_uploader("Pilih gambar (JPG/PNG)", type=["jpg", "jpeg", "png"], key="add_foto")
    new_item["foto"] = ""
    if uploaded:
        saved_path = save_uploaded_image(uploaded, cfg["category"])
        new_item["foto"] = saved_path
        st.image(uploaded, caption="Preview foto", width=300)
        st.success(f"Foto disimpan: {saved_path}")

    # Itinerary khusus paket
    if menu == "🧳 Paket Jalan-jalan":
        st.markdown("**📋 Itinerary** (format: WAKTU|AKTIVITAS, satu baris per jadwal)")
        itinerary_raw = st.text_area("Itinerary", height=200,
            placeholder="07.00|Sarapan Nasi Liwet\n09.00|Kunjungi Keraton\n12.00|Makan siang",
            key="add_itinerary")
        new_item["itinerary"] = []
        if itinerary_raw:
            for line in itinerary_raw.strip().split("\n"):
                if "|" in line:
                    parts = line.split("|", 1)
                    new_item["itinerary"].append({"waktu": parts[0].strip(), "aktivitas": parts[1].strip()})

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button(f"💾 Simpan {menu}", type="primary"):
        if not new_item.get("nama", "").strip():
            st.error("Nama tidak boleh kosong!")
        else:
            new_item["id"] = max([d.get("id", 0) for d in data], default=0) + 1
            data.append(new_item)
            save_data(cfg["file"], data)
            st.success(f"✅ Data '{new_item['nama']}' berhasil disimpan!")
            st.rerun()

# ===== TAB 2: EDIT / HAPUS =====
with tab2:
    st.markdown(f"### Edit / Hapus Data {menu}")
    if not data:
        st.info("Belum ada data.")
    else:
        names = [f"[{d.get('id',i+1)}] {d.get('nama','—')}" for i, d in enumerate(data)]
        selected_idx = st.selectbox("Pilih item", range(len(names)), format_func=lambda x: names[x])
        item = data[selected_idx]

        # Pakai selected_idx dalam key agar widget reset saat item berbeda dipilih
        prefix = f"edit_{selected_idx}"

        st.markdown('<div class="admin-section">', unsafe_allow_html=True)
        edited = {}
        for field in cfg["fields"]:
            key, label, ftype = field[0], field[1], field[2]
            current = item.get(key, "")
            if ftype == "text":
                edited[key] = st.text_input(label, value=str(current), key=f"{prefix}_{key}")
            elif ftype == "textarea":
                edited[key] = st.text_area(label, value=str(current), key=f"{prefix}_{key}", height=100)
            elif ftype == "select":
                options = field[3]
                idx_opt = options.index(current) if current in options else 0
                edited[key] = st.selectbox(label, options, index=idx_opt, key=f"{prefix}_{key}")
            elif ftype == "number":
                val = float(current) if current else 0.0
                if key == "rating":
                    val = max(1.0, min(5.0, val))
                    edited[key] = st.number_input(label, min_value=1.0, max_value=5.0, value=val, key=f"{prefix}_{key}", step=0.1)
                else:
                    edited[key] = st.number_input(label, value=val, key=f"{prefix}_{key}", step=0.1)
            elif ftype == "bool":
                edited[key] = st.checkbox(label, value=bool(current), key=f"{prefix}_{key}")

        # Upload foto baru
        st.markdown("**📷 Ganti Foto** (kosongkan jika tidak ingin mengganti)")
        uploaded_edit = st.file_uploader("Pilih gambar baru", type=["jpg", "jpeg", "png"], key=f"{prefix}_foto")
        edited["foto"] = item.get("foto", "")
        if uploaded_edit:
            saved_path = save_uploaded_image(uploaded_edit, cfg["category"])
            edited["foto"] = saved_path
            st.image(uploaded_edit, caption="Preview foto baru", width=300)
        elif item.get("foto") and Path(item["foto"]).exists():
            from PIL import Image
            st.image(Image.open(item["foto"]), caption="Foto saat ini", width=300)

        # Itinerary untuk paket
        if menu == "🧳 Paket Jalan-jalan":
            current_itin = item.get("itinerary", [])
            itin_text = "\n".join([f"{it['waktu']}|{it['aktivitas']}" for it in current_itin])
            itin_raw = st.text_area("Itinerary", value=itin_text, height=200, key=f"{prefix}_itinerary")
            edited["itinerary"] = []
            if itin_raw:
                for line in itin_raw.strip().split("\n"):
                    if "|" in line:
                        parts = line.split("|", 1)
                        edited["itinerary"].append({"waktu": parts[0].strip(), "aktivitas": parts[1].strip()})

        st.markdown('</div>', unsafe_allow_html=True)

        col_save, col_del = st.columns([1, 1])
        with col_save:
            if st.button("💾 Simpan Perubahan", type="primary"):
                edited["id"] = item.get("id", selected_idx + 1)
                data[selected_idx] = edited
                save_data(cfg["file"], data)
                st.success("✅ Perubahan berhasil disimpan!")
                st.rerun()
        with col_del:
            confirm = st.checkbox("Saya yakin ingin menghapus data ini", key=f"{prefix}_confirm_del")
            if st.button("🗑️ Hapus Item Ini", type="secondary", disabled=not confirm):
                nama_hapus = item.get("nama", "item ini")
                data.pop(selected_idx)
                save_data(cfg["file"], data)
                st.success(f"✅ '{nama_hapus}' berhasil dihapus!")
                st.rerun()

# ===== TAB 3: LIHAT SEMUA =====
with tab3:
    st.markdown(f"### Semua Data {menu} ({len(data)} item)")
    if data:
        import pandas as pd
        display_cols = ["id", "nama"] + [f[0] for f in cfg["fields"] if f[0] not in ("nama", "deskripsi", "artikel", "tips")]
        rows = []
        for d in data:
            row = {col: d.get(col, "") for col in display_cols if col in d or col == "id"}
            rows.append(row)
        df = pd.DataFrame(rows)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Belum ada data.")
