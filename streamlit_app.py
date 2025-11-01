import streamlit as st
import random

# ✅ Konfigurasi halaman
st.set_page_config(page_title="Design Prompt Builder", layout="centered")

# ✅ CSS
st.markdown("""
<style>
.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #00E5FF;
    margin-bottom: 5px;
}
.subtitle {
    text-align: center;
    color: #ccc;
    margin-bottom: 30px;
}
.form-box {
    background-color: #1e1e1e;
    padding: 30px;
    border-radius: 12px;
}
.stButton>button {
    background-color: #00E5FF;
    color: black;
    border-radius: 10px;
    padding: 0.6em 2em;
    font-weight: 600;
    transition: 0.2s;
}
.stButton>button:hover {
    background-color: #18FFFF;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# ✅ Header
st.markdown('<div class="title">🎨 Design Prompt Builder</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Generate creative visual ideas for posters, feeds, or campaign designs — offline & chill 😎</div>', unsafe_allow_html=True)

# ✅ Form input
with st.form("design_form"):
    st.markdown('<div class="form-box">', unsafe_allow_html=True)

    theme = st.text_input("🧩 Tema Utama", "Promo Akhir Tahun")
    color = st.text_input("🎨 Warna Dominan", "Merah, Kuning, Biru")
    mood = st.selectbox("💫 Mood Visual", ["Enerjik", "Elegan", "Minimalis", "Modern", "Hangat", "Industrial"])
    element = st.text_area("🧱 Elemen Desain", "Produk, Toko, Diskon Tag, Background Polos")
    layout = st.selectbox("📐 Komposisi Layout", ["Simetris", "Asimetris", "Grid", "Full Image", "Typography Fokus"])
    style = st.selectbox("🖌️ Gaya Desain", ["Flat Design", "3D Render", "Photo Manipulation", "Modern Corporate", "Artistic / Abstract"])

    submit = st.form_submit_button("🚀 Generate Ide Visual")
    st.markdown("</div>", unsafe_allow_html=True)

# ✅ Output offline
if submit:
    vibes = random.choice([
        "memberikan kesan profesional namun tetap menarik perhatian",
        "membuat audiens langsung tertarik pada produk utama",
        "menghadirkan nuansa yang segar dan mudah diingat",
        "menonjolkan brand image yang kuat dan konsisten",
        "menciptakan kesan visual yang simpel tapi impactful"
    ])

    prompt = f"""
### 💡 Ide Desain Visual

**Tema:** {theme}  
**Warna Dominan:** {color}  
**Mood:** {mood}  
**Elemen Desain:** {element}  
**Layout:** {layout}  
**Gaya:** {style}  

🧠 *Konsep:*  
Gunakan kombinasi warna {color.lower()} dengan gaya {style.lower()} untuk {vibes}.  
Susun elemen {element.lower()} dalam layout {layout.lower()} agar hasil akhir terasa {mood.lower()} dan selaras dengan tema **{theme}**.  
"""

    st.markdown(prompt)
    st.success("✅ Ide visual berhasil dibuat — offline mode aktif!")

    st.code(f"{theme}, {color}, {mood}, {element}, {layout}, {style}", language="markdown")
