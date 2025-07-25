import streamlit as st
import google.generativeai as genai

# ✅ Konfigurasi API Key (dari secrets.toml)
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# ✅ Inisialisasi model Gemini
model = genai.GenerativeModel("gemini-pro")

# ✅ UI setup
st.set_page_config(page_title="Animagine: Create Your Anime Character", layout="centered")

# ✅ CSS Styling
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #F48FB1;
            margin-bottom: 5px;
        }
        .subtitle {
            text-align: center;
            color: #aaa;
            margin-bottom: 30px;
        }
        .form-box {
            background-color: #1e1e1e;
            padding: 30px;
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🎨 Animagine</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Create your own anime-style character powered by Gemini AI</div>', unsafe_allow_html=True)

# ✅ Form UI
with st.form("anime_form"):
    st.markdown('<div class="form-box">', unsafe_allow_html=True)

    name = st.text_input("🧑‍🎤 Character Name", "Anjay Gurinjay")
    gender = st.selectbox("⚧️ Gender", ["Laki-laki", "Perempuan"])
    skill = st.text_input("🔥 Main Skill", "Rasengan")
    ultimate = st.text_input("💥 Ultimate Move", "Kuchiyose Edo Tensei")
    reference = st.text_area("🎨 Visual Style Reference", "Genshin Impact and Naruto Storm")
    action = st.selectbox("🎭 Pose", ["Berdiri", "Melompat", "Menyerang", "Meditasi"])
    effect = st.selectbox("💫 Effect", ["Api", "Es", "Petir", "Aura gelap"])

    submit = st.form_submit_button("🚀 Generate Prompt")
    st.markdown("</div>", unsafe_allow_html=True)

# ✅ Generate Prompt dan Tampilkan Output
if submit:
    full_prompt = f"""/imagine prompt:
Generate a 3D anime-style character named {name}, a {gender.lower()} who controls {skill}.
Their ultimate technique is {ultimate}.
Use cel-shading and dynamic lighting, inspired by anime like {reference}.
Pose the character in a {action} stance with {effect} effects."""

    st.markdown("### ✨ Prompt Output")
    st.code(full_prompt, language="markdown")

    try:
        response = model.generate_content(full_prompt)
        st.markdown("### 🧠 Gemini Output")
        st.write(response.text)
    except Exception as e:
        st.error("❌ Gagal menghubungi Gemini API.")
        st.exception(e)
