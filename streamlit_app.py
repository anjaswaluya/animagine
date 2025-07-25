import streamlit as st
import google.generativeai as genai

# Konfigurasi API dari secrets.toml
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

# 🧱 Konfigurasi Streamlit UI
st.set_page_config(page_title="Animagine Prompt Generator", page_icon="✨")
st.title("✨ Animagine - Prompt Generator")
st.markdown("Bikin karakter anime 3D stylized ala Genshin Impact & Naruto hanya dengan deskripsi!")

st.divider()

# 📥 Form Input
with st.form("anime_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Nama Karakter", placeholder="Contoh: Kalea")
        gender = st.selectbox("🚻 Gender", ["Laki-laki", "Perempuan"])
    with col2:
        skill = st.text_input("🔥 Skill Utama", placeholder="Contoh: Rasengan")
        ultimate = st.text_input("💥 Ultimate Technique", placeholder="Contoh: Kuchiyose Edo Tensei")
    vibe = st.text_area("🎭 Karakter / Personality", placeholder="Contoh: tenang, setia, perhitungan")
    generate = st.form_submit_button("🚀 Generate Prompt")

# 🔮 Prompt Generator
if generate:
    if not name or not skill or not ultimate:
        st.warning("Lengkapi minimal Nama, Skill, dan Ultimate-nya ya brodi.")
    else:
        full_prompt = f"""/imagine prompt:
Generate a 3D anime-style character named {name}, a {gender.lower()} who controls Api.
Their main skill is {skill}. Their ultimate technique is {ultimate}.
{"They are described as " + vibe + "." if vibe else ""}
Use cel-shading and dynamic lighting, inspired by anime like Genshin Impact and Naruto Storm.
"""

        with st.spinner("Menghubungi Gemini API..."):
            try:
                response = model.generate_content(full_prompt)
                st.success("✅ Prompt berhasil dibuat!")

                st.markdown("### 🎨 /imagine Prompt")
                st.code(full_prompt, language="markdown")

                st.markdown("### 🤖 Output Gemini")
                st.write(response.text)

            except Exception as e:
                st.error("Gagal generate dari Gemini. Cek API Key atau koneksi.")
                st.exception(e)
