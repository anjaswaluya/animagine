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
    position: relative;
}
.copy-btn {
    display: inline-block;
    background: linear-gradient(90deg, #00FFE0, #00B8D4);
    color: black;
    border: none;
    border-radius: 10px;
    padding: 10px 16px;
    cursor: pointer;
    font-weight: 600;
    font-size: 14px;
    margin-bottom: 10px;
}
.copy-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 0 15px #00FFE0;
}
.signature {
    text-align: center;
    color: #00FFE0;
    font-size: 14px;
    margin-top: 40px;
    font-family: monospace;
}
.example {
    font-size: 12px;
    color: #aaa;
    font-style: italic;
    margin-top: -8px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# 🪄 Header
st.markdown('<div class="title">ElPrompt</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">the art of lazy creativity — when boredom meets style</div>', unsafe_allow_html=True)

# 🎛️ Input form
with st.form("elprompt_form"):
    st.markdown('<div class="form-box">', unsafe_allow_html=True)

    st.markdown('<div class="example">Contoh: “pagi berkabut di atap gedung”, “seorang pekerja duduk sendiri di gudang cat”, atau “jalan kosong di tengah hujan neon”.</div>', unsafe_allow_html=True)
    tema = st.text_input("🧠 Tema / Ide dasar", "nostalgia warnet tahun 2000an")

    gaya = st.selectbox("🎨 Gaya / Nuansa", [
        "cinematic", "dreamy", "brutalist", "magazine style",
        "moody realism", "playful modern", "retro-futurism"
    ])

    vibe = st.selectbox("💫 Vibe / Emosi", [
        "gloomy", "energetic", "calm", "chaotic",
        "romantic", "mysterious", "absurd", "melancholy"
    ])

    submit = st.form_submit_button("🚀 summon elprompt")
    st.markdown("</div>", unsafe_allow_html=True)

# ⚡ Output
if submit:
    openings = [
        "An ultra realistic depiction of",
        "A cinematic ultra detailed representation of",
        "A hyper-realistic photo concept showing",
        "A detailed and immersive ultra realistic scene of",
        "An artfully composed ultra realistic visual of"
    ]

    extras = [
        "Perfect lighting, natural reflections, cinematic depth, and moody realism.",
        "Sharp focus, rich texture, soft atmospheric haze, and authentic tone mapping.",
        "Balanced lighting, storytelling through visuals, lifelike proportions.",
        "High-detail realism with subtle photographic contrast and emotional tone.",
        "Emphasize realism, depth, and mood-driven lighting — cinematic precision."
    ]

    prompt = f"""/imagine prompt: {random.choice(openings)} {tema.lower()}, in {gaya} style with {vibe} mood. {random.choice(extras)}"""

    # 🪄 Output Box with Copy Button
    st.markdown(f"""
    <div class="output-box">
        <button class="copy-btn" onclick="navigator.clipboard.writeText(`{prompt}`)">📋 Salin Prompt</button>
        <h3>💎 Your ElPrompt:</h3>
        <pre style="white-space: pre-wrap; word-wrap: break-word;">{prompt}</pre>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="signature">✨ elprompt style has comin.</div>', unsafe_allow_html=True)
