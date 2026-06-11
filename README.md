# 🏰 Monggo Pinarak - Portal Wisata Kota Solo

Halo teman-teman SMA! 👋 Selamat datang di repositori proyek **Monggo Pinarak**. 

Aplikasi ini adalah portal informasi pariwisata, kuliner, dan kebudayaan Kota Surakarta (Solo). Proyek ini dibangun menggunakan bahasa pemrograman **Python** dan framework **Streamlit**, sangat cocok buat kamu yang lagi belajar pemrograman web interaktif tanpa ribet!

---

## 🌟 Fitur Utama Aplikasi

Web ini punya banyak fitur seru yang saling terintegrasi:
1. **🏠 Beranda Interaktif (`app.py`)**: Menampilkan statistik jumlah tempat wisata, kuliner, dan coffeeshop secara otomatis dari database JSON.
2. **🏰 Informasi & Peta Solo (`pages/1_Informasi_Solo.py`)**: Profil geografis kota, timeline sejarah, panduan transportasi, dan peta lokasi interaktif.
3. **🗺️ Galeri Informasi Wisata, Kuliner, & Budaya**: Menyajikan daftar objek seru lengkap dengan foto, ulasan singkat, alamat, dan jam buka.
4. **🧳 Rancang Paket Liburan (`pages/7_Paket_Jalan_Jalan.py`)**: Sistem cerdas yang bisa merekomendasikan rute perjalanan liburan di Solo berdasarkan pilihan durasi hari kamu.
5. **🔑 Admin Panel Rahasia (`pages/8_Admin_Panel.py`)**: Dapur pengelolaan konten yang aman. Kamu bisa tambah data wisata/kuliner baru langsung ke database JSON jika tahu password-nya!
6. **🎓 Kuis Interaktif Solo (`pages/10_Kuis_Solo.py`)**: Uji pengetahuanmu seputar Kota Solo lewat 10 soal pilihan ganda interaktif dengan skor dinamis dan perayaan balon.
7. **⚙️ Penjelasan Alur Program (`pages/9_Alur_Program.py`)**: Halaman khusus yang memvisualisasikan arsitektur web dan mencantumkan *pseudocode* lengkap untuk bahan belajar tugas sekolah.

---

## 🛠️ Tech Stack (Teknologi yang Dipakai)
* **Bahasa Utama:** Python 🐍
* **Framework Web:** Streamlit (bikin web interaktif super cepat)
* **Database:** Berkas JSON di folder `data/` (database sederhana yang mudah dibaca manusia)
* **Peta Interaktif:** Folium & Streamlit Folium
* **Styling (CSS):** Desain kustom keraton Jawa (palet cokelat-krem-emas) di `assets/style.css`

---

## 🚀 Cara Menjalankan Aplikasi di Komputermu

Ikuti langkah-langkah mudah berikut ini di command prompt (cmd) atau terminal editor:

### 1. Masuk ke Folder Proyek
Buka CMD di folder proyek ini. Pastikan kamu berada di dalam direktori `monggo-pinarak`:
```bash
cd monggo-pinarak
```

### 2. Membuat Virtual Environment (Opsional tapi Direkomendasikan)
Agar library project ini tidak bentrok dengan project lain di komputermu:
```bash
python -m venv venv
```
Lalu aktifkan:
* **Windows:**
  ```bash
  venv\Scripts\activate
  ```
* **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Library yang Dibutuhkan
Unduh semua kebutuhan framework dengan mengetik:
```bash
pip install -r requirements.txt
```

### 4. Nyalakan Server Aplikasi
Jalankan perintah ajaib ini untuk membuka website di browsermu secara otomatis:
```bash
streamlit run app.py
```
*Web akan otomatis terbuka di browser pada alamat `http://localhost:8501`*

---

## 📁 Struktur Folder Penting
* `app.py`: Pintu gerbang utama web.
* `pages/`: Folder berisi halaman-halaman sub-menu.
* `utils.py`: Berisi fungsi asisten untuk membaca file data JSON dan memuat CSS.
* `data/`: Folder penyimpanan file `.json` (database).
* `assets/`: Tempat menyimpan logo, stylesheet CSS, dan gambar-gambar pariwisata.

---

💡 **Friendly Note:**
Belajar koding itu seperti bermain lego. Susun logikamu baris demi baris, jangan takut mencoba dan eror. Jika ada bagian alur program yang membingungkan, silakan buka menu **Alur Program** di sidebar aplikasi untuk membaca penjelasan dan *pseudocode*-nya. Selamat belajar dan berkarya! 🚀
