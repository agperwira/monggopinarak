import json
import os
import base64
from pathlib import Path
from PIL import Image
import streamlit as st
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
UPLOAD_DIR = BASE_DIR / "assets" / "uploads"

# Load .env
load_dotenv(BASE_DIR / ".env")

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "monggo2024")
APP_NAME       = os.getenv("APP_NAME", "Monggo Pinarak")
APP_TAGLINE    = os.getenv("APP_TAGLINE", "Portal Wisata Kota Surakarta")


# ── Path helpers ──────────────────────────────────────────────

def to_relative(abs_path: str) -> str:
    """Konversi path absolut ke path relatif terhadap BASE_DIR."""
    try:
        return str(Path(abs_path).relative_to(BASE_DIR))
    except ValueError:
        return abs_path  # sudah relatif atau beda drive

def resolve(rel_path: str) -> Path:
    """Kembalikan Path absolut dari path relatif maupun absolut.
    Kembalikan None jika path kosong atau tidak valid.
    """
    if not rel_path or not rel_path.strip():
        return None
    p = Path(rel_path)
    if p.is_absolute():
        return p
    return BASE_DIR / p


# ── Data ──────────────────────────────────────────────────────

def load_data(filename: str) -> list:
    path = DATA_DIR / filename
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_data(filename: str, data: list):
    DATA_DIR.mkdir(exist_ok=True)
    path = DATA_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ── Image ─────────────────────────────────────────────────────

def save_uploaded_image(uploaded_file, category: str) -> str:
    """Simpan gambar upload, kembalikan path RELATIF terhadap BASE_DIR."""
    save_dir = UPLOAD_DIR / category
    save_dir.mkdir(parents=True, exist_ok=True)
    file_path = save_dir / uploaded_file.name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    # Simpan sebagai relatif path (pakai forward slash agar lintas OS)
    return to_relative(str(file_path)).replace("\\", "/")


def _img_to_b64(image_path: str) -> str:
    full = resolve(image_path)
    if not full or not full.is_file():
        return ""
    try:
        with open(full, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return ""


def display_image(image_path: str, width: int = 300):
    full = resolve(image_path)
    if full and full.is_file():
        st.image(Image.open(full), width=width)


# ── UI helpers ────────────────────────────────────────────────

def load_css():
    css_path = BASE_DIR / "assets" / "style.css"
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def page_header(title: str, subtitle: str = ""):
    sub = (f"<p style='color:rgba(255,248,231,.9);margin:.5rem 0 0;"
           f"font-size:.95rem;'>{subtitle}</p>") if subtitle else ""
    st.markdown(
        f"<div class='page-header'>"
        f"<h1 style='color:white;margin:0;font-size:1.9rem;font-weight:800;"
        f"letter-spacing:-.5px;'>{title}</h1>{sub}</div>",
        unsafe_allow_html=True
    )


def gold_divider():
    st.markdown("<hr class='gold-divider'>", unsafe_allow_html=True)


def render_card(title: str, desc: str, img_path: str = "", badge: str = "",
                meta: list = None):
    """Card dengan gambar, badge, judul, deskripsi, dan metadata."""
    with st.container(border=True):
        # Gambar
        full = resolve(img_path)
        if full and full.is_file():
            b64 = _img_to_b64(img_path)
            st.markdown(
                f"<div style='height:170px;overflow:hidden;border-radius:6px;"
                f"margin:-1px -1px 10px;'>"
                f"<img src='data:image/jpeg;base64,{b64}' "
                f"style='width:100%;height:170px;object-fit:cover;display:block;'>"
                f"</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div style='height:120px;background:linear-gradient(135deg,#F5E6D0,#EDD5B0);"
                "border-radius:6px;display:flex;align-items:center;justify-content:center;"
                "color:#A0826D;font-size:13px;margin:-1px -1px 10px;flex-direction:column;gap:4px;'>"
                "<span style='font-size:1.8rem;'>🖼️</span><span>Belum ada foto</span></div>",
                unsafe_allow_html=True
            )
        # Badge
        if badge:
            st.markdown(
                f"<span style='background:#D4AF37;color:#2C1810;font-size:.68rem;"
                f"font-weight:700;padding:2px 12px;border-radius:20px;"
                f"display:inline-block;margin-bottom:6px;'>{badge}</span>",
                unsafe_allow_html=True
            )
        st.markdown(f"**{title}**")
        short = desc[:125] + "..." if len(desc) > 125 else desc
        st.caption(short)
        if meta:
            st.markdown(
                "<hr style='margin:8px 0 6px;border:none;border-top:1px solid #E8D5B0;'>",
                unsafe_allow_html=True
            )
            for m in meta:
                st.caption(m)
