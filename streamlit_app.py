import streamlit as st
import random

# 🧠 Setup
st.set_page_config(page_title="ElPrompt — The Art of Lazy Creativity", layout="centered")

# 🎨 Custom CSS
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #111, #000);
    color: #fff;
    font-family: 'Poppins', sans-serif;
}
.title {
    font-size: 50px;
    font-weight: 800;
    text-align: center;
    color: #00FFE0;
    letter-spacing: 2px;
    text-shadow: 0 0 20px #00FFE0;
    margin-top: 40px;
}
.subtitle {
    text-align: center;
    color: #aaa;
    font-size: 16px;
    margin-bottom: 50px;
    font-style: italic;
}
.form-box {
    background-color: rgba(255,255,255,0.05);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 0 15px rgba(0,0,0,0.4);
    backdrop-filter: blur(10px);
}
.stButton>button {
    background: linear-gradient(90deg, #00FFE0, #00B8D4);
    color: #000;
    border-radius: 12px;
    padding: 0.8em 2em;
    font-weight: 600;
    border: none;
    transition: 0.3s;
    font-size: 16px;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px #00FFE0;
}
.output-box {
    background-color: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 15px;
    margin-top: 30px;
    box-shadow: inset 0 0 15px rgba(0,255,224,0.3);
}
.signature {
    text-align: center;
    color: #00FFE0;
    font-size: 14px;
    margin-top: 40px;
    font-family: monospace;
}
</style>
""", unsafe_allow_html=True)

# 🪄 Header
st.markdown('<div class="title">ElPrompt</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">the art of lazy creativity — when boredom meets style</div>', unsafe_allow_html=True)

# 🎛️ Input form
with st.form("elprompt_form"):
    st.markdown('<div class="form-box">', unsafe_allow_html=True)

    tema = st.text_input("🧠 Tema / Ide dasar", "nostalgia warnet tahun 2000an")
    gaya = st.selectbox("🎨 Gaya / Nuansa", ["cinematic", "dreamy", "brutalist", "magazine style", "moody realism", "playful modern", "retro-futurism"])
    vibe = st.selectbox("💫 Vibe / Emosi", ["gloomy", "energetic", "calm", "chaotic", "romantic", "mysterious", "absurd", "melancholy"])

    submit = st.form_submit_button("🚀 summon elprompt")
    st.markdown("</div>", unsafe_allow_html=True)

# ⚡ Output
if submit:
    openings = [
        "A detailed visual concept of",
        "An artistic representation of",
        "A surreal yet realistic depiction of",
        "A cinematic frame capturing",
        "A concept art describing"
    ]

    extras = [
        "Focus on atmosphere, subtle textures, and emotion-driven lighting.",
        "Include rich composition, depth, and mood harmony.",
        "Stylized but grounded — visually poetic yet modern.",
        "Balanced between realism and creative abstraction.",
        "Should evoke a feeling of stillness and storytelling."
    ]

    prompt = f"""/imagine prompt: {random.choice(openings)} {tema.lower()} — styled in {gaya} aesthetic with a {vibe} mood. {random.choice(extras)}"""

    st.markdown('<div class="output-box">', unsafe_allow_html=True)
    st.markdown("### 💎 Your ElPrompt:")
    st.code(prompt, language="markdown")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="signature">✨ elprompt style has comin.</div>', unsafe_allow_html=True)
