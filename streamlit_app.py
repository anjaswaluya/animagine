import streamlit as st
import google.generativeai as genai

# Konfigurasi API Key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Inisialisasi model Gemini (v1)
model = genai.GenerativeModel("models/gemini-pro")

# Streamlit App UI
st.set_page_config(page_title="Animagine: Create Your Anime Character!", page_icon="✨")

st.markdown("""
    <style>
        .big-title {
            font-size:42px;
            font-weight:700;
            color:#FF4B4B;
            text-align:center;
            margin-bottom:20px;
        }
        .subtext {
            font-size:18px;
            color:#ccc;
            text-align:center;
            margin-bottom:40px;
        }
        .prompt-box {
            background-color:#1e1e1e;
            padding:20px;
            border-radius:10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">Animagine 🎨</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Create a 3D-style anime character with AI!</div>', unsafe_allow_html=True)

with st.form("anime_form"):
    name = st.text_input("👤 Character Name", "Anjay Gurinjay")
    gender = st.selectbox("⚧️ Gender", ["Laki-laki", "Perempuan"])
    skill = st.text_input("🌀 Main Skill", "Rasengan")
    ultimate = st.text_input("💥 Ultimate Move", "Kuchiyose Edo Tensei")
    reference = st.text_area("🧠 Gaya visual (inspirasi visual)", "Genshin Impact, Naruto Storm")
    submit = st.form_submit_button("🔮 Generate Prompt")

if submit:
    with st.spinner("Menciptakan prompt..."):
        full_prompt = f"""
        /imagine prompt:
        Generate a 3D anime-style character named {name}, a {gender.lower()} who controls API.
        Their main skill is {skill}. Their ultimate technique is {ultimate}.
        Use cel-shading and dynamic lighting, inspired by anime like {reference}.
        """

        try:
            response = model.generate_content(full_prompt)
            st.success("✅ Prompt berhasil dibuat!")
            st.markdown("### ✨ Prompt Final:")
            st.code(full_prompt.strip(), language="markdown")

            st.markdown("### 🧠 Respon AI:")
            st.write(response.text)

        except Exception as e:
            st.error("❌ Terjadi kesalahan saat menghubungi Gemini API.")
            st.exception(e)

st.markdown("---")
st.caption("Animagine - Powered by Gemini & Streamlit ✨")
