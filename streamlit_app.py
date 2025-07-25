import streamlit as st
from prompt_generator import generate_prompt

st.set_page_config(page_title="Animagine", layout="centered")

st.title("🎌 Animagine – /imagine Prompt Generator")
st.markdown("Buat karakter anime kamu dan hasilkan prompt siap pakai untuk Gemini AI.")

character_name = st.text_input("Nama Karakter")
gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
element = st.selectbox("Elemen Utama", ["Api", "Air", "Bumi", "Angin", "Petir"])
skill1 = st.text_input("Skill 1")
ultimate = st.text_input("Ultimate Move")

if st.button("🎨 Generate Prompt"):
    prompt = generate_prompt(character_name, gender, element, skill1, ultimate)
    st.text_area("✨ Hasil Prompt", value=prompt, height=400)
