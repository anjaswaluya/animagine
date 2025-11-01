import streamlit as st
import random

# ⚙️ Setup
st.set_page_config(page_title="Design Story Builder", layout="centered")

# 🎨 CSS biar vibe-nya chill
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #1e1e1e, #0d0d0d);
    color: white;
    font-family: 'Poppins', sans-serif;
}
.title {
    font-size: 44px;
    font-weight: bold;
    text-align: center;
    color: #00E5FF;
    text-shadow: 0 0 20px #00E5FF;
    margin-bottom: 10px;
}
.subtitle {
    text-align: center;
    color: #aaa;
    margin-bottom: 40px;
}
.form-box {
    background-color: rgba(255,255,255,0.05);
    padding: 30px;
    border-radius: 14px;
}
.stButton>button {
    background: linear-gradient(90deg, #00E5FF, #18FFFF);
    color: black;
    border-radius: 10px;
    padding: 0.7em 2em;
    font-weight: 600;
    border: none;
    transition: 0.2s;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 15px #00E5FF;
}
</style>
""", unsafe_allow_html=True)

# 🧠 Header
st.markdown('<div class="title">🎨 Design Story Builder</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ngobrol santai bareng ide desain. Output-nya? Cerita yang ngasih feel visual lo 🎭</div>', unsafe_allow_html=True)

# 🎯 Form
with st.form("design_form"):
    st.markdown('<div class="form-box">', unsafe_allow_html=True)

    theme = st.text_input("🎯 Ceritain dulu, temanya apa bro?", "Promo Akhir Tahun")
    vibe = st.selectbox("😎 Kesan apa yang mau lo munculin?", ["Hangat", "Megah", "Enerjik", "Kalem", "Elegan", "Rame tapi rapi"])
    color = st.text_input("🌈 Warna yang pengen dominan?", "Merah dan Kuning")
    object_focus = st.text_input("🧱 Fokus utamanya apa?", "Produk utama dan tulisan diskon besar")
    mood = st.selectbox("💫 Kalau desain ini orang, dia kayak gimana?", ["Ramah tapi pede", "Cool dan profesional", "Lincah dan heboh", "Tenang tapi kuat"])
    bg = st.selectbox("🪄 Background-nya lo bayangin kayak gimana?", ["Cerahan", "Gelap elegan", "Gradasi lembut", "Polos minimalis", "Bokeh modern"])

    submit = st.form_submit_button("✨ Ceritain Desain Gue")
    st.markdown("</div>", unsafe_allow_html=True)

# 🖋️ Output Cerita
if submit:
    hook = random.choice([
        "Bayangin lo lagi buka file Photoshop, terus warna pertama yang muncul langsung bikin senyum.",
        "Desain ini kayak punya napas sendiri, tenang tapi bener-bener nyentuh mata yang ngelihat.",
        "Begitu layout-nya muncul, rasanya kayak poster ini udah siap naik billboard.",
        "Satu layer demi layer dibuka, tiap elemen kayak ngomong hal yang sama: ‘ini keren’.",
        "Pas udah jadi, desainnya tuh bukan cuma visual — tapi vibe."
    ])

    ending = random.choice([
        "Kalau ini naik di IG Mitra Bangunan, pasti langsung banyak yang berhenti scroll.",
        "Desainnya simple, tapi punya karisma yang bikin orang pengen liat dua kali.",
        "Kayak ada energi yang gak bisa dijelasin, tapi kerasa banget di mata.",
        "Ini bukan sekadar promo, tapi perasaan visual yang lo bisa rasain.",
        "Cocok banget buat konten yang pengen keliatan niat tapi gak ribet."
    ])

    story = f"""
## 🎨 Cerita di Balik Desain: *{theme}*

{hook}  
Konsep ini berangkat dari nuansa **{vibe.lower()}**, dengan warna dominan **{color.lower()}** yang langsung narik perhatian.  
Fokusnya ada di **{object_focus.lower()}**, disusun dengan komposisi yang {bg.lower()}.  

Kalau desain ini jadi orang, dia bakal keliatan **{mood.lower()}** — bukan cuma gaya, tapi punya karakter yang kuat.  

{ending}
"""

    st.markdown(story)
    st.success("🖌️ Cerita desain lo udah jadi, bro!")

