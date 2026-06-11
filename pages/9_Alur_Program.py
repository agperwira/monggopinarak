import streamlit as st
import sys
import streamlit.components.v1 as components
from pathlib import Path

# Membuka akses ke folder utama agar bisa import utils
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import load_css, page_header, gold_divider

# Set konfigurasi halaman
st.set_page_config(
    page_title="Alur Program — Monggo Pinarak",
    page_icon="⚙️",
    layout="wide"
)

# Load CSS custom dari repositori
load_css()

# Menu kembali ke beranda di sidebar
st.sidebar.page_link("app.py", label="🏠 Kembali ke Beranda")
st.sidebar.markdown("---")

# Header Halaman
page_header("⚙️ Penjelasan Alur Program", "Pelajari bagaimana kode pemrograman di belakang layar Monggo Pinarak bekerja!")

# Deskripsi singkat pembuka
st.markdown("""
<div class="info-box" style="margin-bottom: 1.5rem;">
    <h3 style="color:#8B4513; margin-top:0;">👋 Halo Programmer Muda!</h3>
    <p style="color:#5D4037; line-height:1.7;">
        Apakah kamu penasaran bagaimana tombol-tombol yang kamu klik di website ini bisa memunculkan rekomendasi wisata, 
        atau bagaimana halaman admin menjaga data agar tetap aman? Di halaman ini, kita akan bedah semuanya memakai 
        <b>Flowchart (Diagram Alir)</b> dan penjelasan sederhana yang seru!
    </p>
</div>
""", unsafe_allow_html=True)

# Fungsi pembantu untuk menggambar Mermaid diagram menggunakan iframe & CDN secara aman
def draw_flowchart(mermaid_code: str, height: int = 400):
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                margin: 0;
                background-color: transparent;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: sans-serif;
            }}
            #container {{
                display: flex;
                justify-content: center;
                align-items: center;
                width: 100%;
                min-height: {height - 20}px;
            }}
            .mermaid {{
                display: block;
                margin: 0;
            }}
            .error-box {{
                font-family: sans-serif;
                font-size: 14px;
                color: #721c24;
                background-color: #f8d7da;
                border: 1px solid #f5c6cb;
                padding: 15px;
                border-radius: 4px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div id="container">
            <div class="mermaid">
{mermaid_code}
            </div>
        </div>

        <script>
            function loadScript(url, callback, errorCallback) {{
                var script = document.createElement("script");
                script.type = "text/javascript";
                script.src = url;
                script.onload = callback;
                script.onerror = errorCallback;
                document.head.appendChild(script);
            }}

            function startRendering() {{
                try {{
                    mermaid.initialize({{
                        startOnLoad: true,
                        theme: 'forest',
                        securityLevel: 'loose'
                    }});
                    // Jalankan inisialisasi manual jika DOM sudah selesai dimuat
                    mermaid.init(undefined, document.querySelectorAll('.mermaid'));
                }} catch (e) {{
                    console.error("Gagal merender diagram: ", e);
                    document.getElementById('container').innerHTML = 
                        "<div class='error-box'><b>Gagal Merender Diagram:</b><br>" + e.message + "</div>";
                }}
            }}

            // Coba muat dari CDN 1 (jsDelivr)
            loadScript("https://cdn.jsdelivr.net/npm/mermaid@9.4.3/dist/mermaid.min.js", function() {{
                startRendering();
            }}, function() {{
                console.warn("jsDelivr gagal dimuat, mencoba cdnjs...");
                // Coba muat dari CDN 2 (cdnjs)
                loadScript("https://cdnjs.cloudflare.com/ajax/libs/mermaid/9.4.3/mermaid.min.js", function() {{
                    startRendering();
                }}, function() {{
                    console.warn("cdnjs gagal dimuat, mencoba unpkg...");
                    // Coba muat dari CDN 3 (unpkg)
                    loadScript("https://unpkg.com/mermaid@9.4.3/dist/mermaid.min.js", function() {{
                        startRendering();
                    }}, function() {{
                        document.getElementById('container').innerHTML = 
                            "<div class='error-box'><b>Gagal Memuat Diagram:</b><br>Tidak bisa memuat library diagram dari CDN. Hubungkan ke internet untuk melihat flowchart secara visual.</div>";
                    }});
                }});
            }});
        </script>
    </body>
    </html>
    """
    components.html(html_template, height=height, scrolling=True)

# Menggunakan Tabs untuk membagi penjelasan
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📂 Struktur & Aliran Data", 
    "🏠 Alur Beranda (app.py)", 
    "🧳 Rencana Perjalanan", 
    "🔑 Dapur Admin (Admin Panel)",
    "🎓 Kuis Solo (10_Kuis_Solo.py)"
])

# ── TAB 1: STRUKTUR & ALIRAN DATA ─────────────────────────────────
with tab1:
    st.markdown("### 📂 Hubungan Antar Berkas di Aplikasi")
    st.write(
        "Aplikasi Monggo Pinarak menggunakan sistem multi-halaman. Halaman utama berada di "
        "`app.py`, sedangkan sub-halamannya berada di folder `pages/`. Semua data disimpan di file JSON."
    )
    
    # Diagram Relasi
    relasi_code = """
    graph TD
        A["Pengunjung Web"] -->|Buka Link| B("app.py - Halaman Utama")
        B -->|Membaca Data| C[("data/*.json")]
        B -->|Akses Halaman Lain| D["pages/1_Informasi_Solo.py"]
        B -->|Akses Paket Perjalanan| E["pages/7_Paket_Jalan_Jalan.py"]
        B -->|Kelola Konten Admin| F["pages/8_Admin_Panel.py"]
        F -->|Menulis & Update Data| C
        
        style A fill:#E1F5FE,stroke:#039BE5,stroke-width:2px;
        style B fill:#FFF8E1,stroke:#FFB300,stroke-width:2px;
        style C fill:#E8F5E9,stroke:#43A047,stroke-width:2px;
        style D fill:#FFF3E0,stroke:#F57C00,stroke-width:2px;
        style E fill:#FFF3E0,stroke:#F57C00,stroke-width:2px;
        style F fill:#FFEBEE,stroke:#E53935,stroke-width:2px;
    """
    draw_flowchart(relasi_code, height=350)
    
    st.markdown("""
    **Penjelasan Sederhana:**
    1. **Pengunjung** datang ke halaman **Beranda (`app.py`)**.
    2. Beranda memanggil asisten di **`utils.py`** untuk membaca gudang data di folder **`data/`** (seperti `wisata.json` dan `kuliner.json`).
    3. Pengunjung bisa berpindah ruangan/halaman menggunakan menu sidebar (halaman 1 sampai 10).
    4. Jika data di gudang (`data/*.json`) diubah oleh Admin di halaman **Admin Panel (`8_Admin_Panel.py`)**, maka perubahan tersebut langsung tampil di beranda dan halaman lainnya!
    """)

# ── TAB 2: ALUR BERANDA (app.py) ─────────────────────────────────
with tab2:
    st.markdown("### 🏠 Langkah demi Langkah Jalannya Halaman Utama (Beranda)")
    st.write(
        "Ketika pengguna membuka website pertama kali, program di `app.py` "
        "menjalankan urutan logika berikut secara berurutan dari atas ke bawah:"
    )
    
    st.markdown("""
    1. **Inisialisasi Halaman**: Program mengatur judul browser menjadi *"Monggo Pinarak"* dan memasukkan desain/tampilan CSS khusus agar website terlihat rapi dan estetik.
    2. **Tampilkan Banner Utama (Hero Banner)**: Program mencetak bagian tulisan sambutan besar di paling atas web.
    3. **Memuat Data JSON**: Program memanggil fungsi `load_data()` untuk membaca file database dari `data/wisata.json` dan `data/kuliner.json`.
    4. **Menghitung Total Konten**: Program menghitung total jumlah item (misal: jumlah lokasi wisata dan menu kuliner yang terdaftar di database).
    5. **Tampilkan Statistik Konten**: Program menggambar info box (kartu statistik) di layar untuk menampilkan jumlah konten tersebut kepada pengguna.
    6. **Tampilkan Navigasi Menu**: Program membuat tombol-tombol link halaman agar pengguna bisa berpindah ke halaman lain (seperti Informasi Solo, Wisata, Kuliner, dll).
    """)

    st.markdown("### 📝 Pseudocode Alur Beranda")
    st.code("""
MULAI
    ATUR KONFIGURASI LAYAR ("Monggo Pinarak", Tampilan Lebar)
    MUAT_GAYA_CSS()
    TAMPILKAN SPANDUK_HERO ("Selamat Datang di Kota Surakarta")
    
    BACA_FILE "data/wisata.json" -> SIMPAN DI variabel 'wisata'
    BACA_FILE "data/kuliner.json" -> SIMPAN DI variabel 'kuliner'
    
    JUMLAH_WISATA = HITUNG_BANYAK_ITEM(wisata)
    JUMLAH_KULINER = HITUNG_BANYAK_ITEM(kuliner)
    
    TAMPILKAN KARTU_STATISTIK ("Destinasi Wisata", JUMLAH_WISATA)
    TAMPILKAN KARTU_STATISTIK ("Menu Kuliner", JUMLAH_KULINER)
    
    TAMPILKAN PILIHAN_TOMBOL_NAVIGASI()
SELESAI
    """, language="text")

# ── TAB 3: RENCANA PERJALANAN (7_Paket_Jalan_Jalan.py) ─────────────────────────────────
with tab3:
    st.markdown("### 🧳 Alur Logika Sistem Pembuat Jadwal Piknik")
    st.write(
        "Halaman paket perjalanan menggunakan sistem interaktif. Berikut adalah alur logikanya "
        "saat pengguna memilih paket wisata:"
    )
    
    st.markdown("""
    1. **Menerima Masukan Pilihan Hari**: Program menampilkan pilihan tombol dropdown untuk durasi liburan (misal: 1 Hari atau 2 Hari).
    2. **Mengecek Pilihan Durasi**: Program memeriksa angka hari yang dipilih oleh pengguna menggunakan logika percabangan (`if-elif-else`):
        * **Jika Durasi = 1 Hari**: Program akan langsung mencetak rencana perjalanan kilat seperti mengunjungi *Keraton Surakarta*, lalu lanjut makan siang *Selat Solo*, dan belanja sore di *Pasar Klewer*.
        * **Jika Durasi = 2 Hari**: Program menyusun rute dua hari (Hari 1 keliling pusat budaya, Hari 2 wisata alam seperti *Grojogan Sewu* di Tawangmangu).
        * **Jika Belum Memilih**: Program menampilkan tulisan pengingat *"Silakan pilih durasi perjalanan Anda terlebih dahulu di atas"*.
    3. **Menampilkan Hasil Rute**: Informasi jadwal yang sesuai dengan durasi terpilih langsung dicetak di layar secara real-time.
    """)

    st.markdown("### 📝 Pseudocode Rencana Perjalanan")
    st.code("""
MULAI
    TAMPILKAN JUDUL ("Rancang Paket Jalan-Jalanmu")
    DURASI = INPUT_PILIHAN ("Mau liburan berapa hari?", [1, 2])
    
    JIKA DURASI == 1 MAKA:
        TAMPILKAN RUTE ("Pagi: Keraton Kasunanan, Siang: Kuliner, Sore: Pasar Klewer")
    SELAIN ITU JIKA DURASI == 2 MAKA:
        TAMPILKAN RUTE ("Hari 1: Budaya Kota Solo, Hari 2: Rekreasi Alam Tawangmangu")
    JIKA TIDAK:
        TAMPILKAN PERINGATAN ("Silakan pilih durasi perjalanan terlebih dahulu!")
SELESAI
    """, language="text")

# ── TAB 4: DAPUR ADMIN (8_Admin_Panel.py) ─────────────────────────────────
with tab4:
    st.markdown("### 🔑 Alur Validasi Keamanan dan Manipulasi Database")
    st.write(
        "Halaman Admin Panel berfungsi untuk mengamankan data dan memproses data baru. "
        "Berikut langkah logikanya:"
    )
    
    st.markdown("""
    1. **Meminta Sandi Masuk**: Sistem menampilkan kolom input khusus kata sandi yang disembunyikan.
    2. **Melakukan Pemeriksaan Kata Sandi**:
        * **Kondisi Salah**: Jika sandi yang diinputkan tidak cocok dengan sandi rahasia di file konfigurasi, program akan langsung menampilkan pesan peringatan merah *"Akses Ditolak/Sandi Salah"* dan menyembunyikan semua menu kelola.
        * **Kondisi Benar**: Jika sandi cocok, program membuka akses penuh dan memunculkan formulir isian data wisata baru (Nama Wisata, Alamat, Deskripsi, dan tombol upload foto).
    3. **Penyimpanan Data Permanen (CRUD)**:
        * Ketika Admin mengisi form dan menekan tombol **Simpan**:
        * Program akan membaca database file `wisata.json` yang lama.
        * Program menambahkan data wisata baru tersebut ke dalam list data.
        * Program menulis ulang dan menutup file `wisata.json` agar tersimpan secara permanen di server.
        * Tampilan web di-refresh otomatis, sehingga destinasi baru langsung muncul di halaman depan.
    """)

    st.markdown("### 📝 Pseudocode Dapur Admin")
    st.code("""
MULAI
    TAMPILKAN JUDUL ("Halaman Kelola Admin")
    SANDI_INPUT = INPUT_PASSWORD ("Masukkan Sandi:")
    
    JIKA SANDI_INPUT == "solo-sakti-123" MAKA:
        TAMPILKAN NOTIFIKASI_SUKSES ("Akses Diterima!")
        TAMPILKAN FORMULIR_DATA_BARU()
        
        NAMA = INPUT_TEKS ("Nama Wisata:")
        ALAMAT = INPUT_TEKS ("Alamat Lokasi:")
        
        JIKA TOMBOL_SIMPAN ditekan MAKA:
            WISATA_BARU = BUAT_STRUKTUR_DATA (NAMA, ALAMAT)
            BACA file "data/wisata.json" -> TAMBAH WISATA_BARU -> TULIS KEMBALI
            TAMPILKAN NOTIFIKASI ("Sukses! Tempat wisata berhasil disimpan.")
    JIKA TIDAK:
        TAMPILKAN NOTIFIKASI_EROR ("Password Salah! Akses Ditolak.")
SELESAI
    """, language="text")

# ── TAB 5: KUIS SOLO (10_Kuis_Solo.py) ─────────────────────────────────
with tab5:
    st.markdown("### 🎓 Alur Logika Jalannya Kuis Interaktif")
    st.write(
        "Halaman Kuis Solo mencatat skor dan memandu pengguna menjawab 10 pertanyaan "
        "menggunakan status variabel dinamis (session state):"
    )
    
    st.markdown("""
    1. **Fase Mulai (Start Screen)**: Menampilkan tombol Mulai Kuis. Saat ditekan, status `quiz_started` diatur menjadi `True`.
    2. **Fase Pertanyaan (Quiz Loop)**:
       * Mengambil soal ke-*i* dari daftar 10 pertanyaan.
       * Menggambar tombol radio pilihan ganda di layar.
       * Ketika pengguna menekan tombol *"Pertanyaan Berikutnya"*, pilihan disimpan, skor diperbarui jika jawaban benar, dan indeks soal bertambah 1.
    3. **Fase Selesai (Result Screen)**:
       * Jika indeks mencapai soal ke-10, kuis selesai (`quiz_finished` = `True`).
       * Menampilkan presentase skor akhir (Benar / 10 * 100).
       * Menampilkan evaluasi per-soal dan tombol Ulangi Kuis untuk mengulang dari soal pertama.
    """)

    st.markdown("### 📝 Pseudocode Kuis Solo")
    st.code("""
MULAI
    JIKA STATUS_MULAI == False MAKA:
        TAMPILKAN TOMBOL ("Mulai Kuis")
        JIKA TOMBOL DITEKAN MAKA:
            STATUS_MULAI = True
            PANGGIL REFRESH()
            
    SELAIN ITU JIKA STATUS_SELESAI == False MAKA:
        INDERS_SOAL = AMBIL_INDEX_SOAL_SEKARANG()
        TAMPILKAN_SOAL(SOAL_DAFTAR[INDERS_SOAL])
        JAWABAN = INPUT_RADIO_PILIHAN()
        
        JIKA TOMBOL_SUBMIT DITEKAN MAKA:
            JIKA JAWABAN == JAWABAN_BENAR MAKA:
                SKOR = SKOR + 1
            
            JIKA INDERS_SOAL < 9 MAKA:
                INDERS_SOAL = INDERS_SOAL + 1
            JIKA TIDAK:
                STATUS_SELESAI = True
            PANGGIL REFRESH()
            
    SELAIN ITU:
        PERSEN_SKOR = (SKOR / 10) * 100
        TAMPILKAN SKOR (PERSEN_SKOR)
        JIKA PERSEN_SKOR >= 80 MAKA:
            TAMPILKAN BALON_ANIMASI()
            
        JIKA TOMBOL_RESET DITEKAN MAKA:
            SKOR = 0
            STATUS_MULAI = True
            STATUS_SELESAI = False
            INDERS_SOAL = 0
            PANGGIL REFRESH()
SELESAI
    """, language="text")

# Footer Halaman
gold_divider()
st.markdown("""
<div style="text-align: center; color: #A0826D; font-size: 0.85rem; margin-top: 1rem;">
    Belajar coding itu menyenangkan! Dengan memahami alur logika di atas, kamu sudah selangkah lebih dekat menjadi programmer hebat. 🚀
</div>
""", unsafe_allow_html=True)
