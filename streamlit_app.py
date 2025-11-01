import streamlit as st
import random
import base64

# 🧠 Setup
st.set_page_config(page_title="ElPrompt v2 — White Edition", layout="centered")

# 🌈 CSS STYLE — Clean, Animated, Elegant
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Inter:wght@400;600&display=swap');

body {
    background: #fafafa;
    color: #111;
    font-family: 'Inter', sans-serif;
    animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.title {
    font-family: 'Poppins', sans-serif;
    font-size: 44px;
    font-weight: 700;
    text-align: center;
    background: linear-gradient(90deg, #6C63FF, #00BFA6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 1px;
    margin-top: 40px;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #555;
    font-size: 16px;
    margin-bottom: 40px;
    font-style: italic;
}

.card {
    background: white;
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.05);
    animation: slideUp 0.8s ease;
}

@keyframes slideUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.stButton>button {
    background: linear-gradient(90deg, #6C63FF, #00BFA6);
    color: white;
    font-weight: 600;
    border-radius: 10px;
    padding: 0.8em 2em;
    font-size: 16px;
    border: none;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    transform: scale(1.03);
    box-shadow: 0 4px 15px rgba(108,99,255,0.3);
}

.output-box {
    background: #fff;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 5px 25px rgba(0,0,0,0.07);
    margin-top: 30px;
    animation: fadeIn 1s ease-in-out;
}

.copy-btn {
    display: inline-block;
    margin-top: 10px;
    background: linear-gradient(90deg, #6C63FF, #00BFA6);
    border: none;
    color: white;
    font-weight: 600;
    border-radius: 8px;
    padding: 10px 20px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.copy-btn:hover {
    transform: scale(1.03);
    box-shadow: 0 4px 12px rgba(0,191,166,0.3);
}

.signature {
    text-align: center;
    color: #6C63FF;
    font-size: 14px;
    margin-top: 50px;
    font-family: monospace;
}
</style>
""", unsafe_allow_html=True)

# 🪄 Header
st.markdown('<div class="title">ElPrompt v2</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">where minimalism meets imagination 💭</div>', unsafe_allow_html=True)

# 🎛️ Input Form
with st.form("prompt_form"):
    st.markdown('<div class="card">', unsafe_allow_html=True)

    tema = st.text_input("💡 Tema / Ide dasar", placeholder="contoh: ruang kerja dengan cahaya senja")
    gaya = st.selectbox("🎨 Gaya / Style", [
        "cinematic ultra realistic", "minimal modern", "dreamy tone", 
        "fashion editorial", "product showcase", "brutalist contrast", "moody aesthetic"
    ])
    vibe = st.selectbox("💫 Vibe / Emosi", [
        "calm but powerful", "lonely yet peaceful", "energetic and bold", 
        "mysterious and elegant", "romantic and nostalgic", "chaotic creative"
    ])
    
    use_photo = st.checkbox("📷 Pakai Foto Referensi (opsional)")
    detail_level = st.slider("🧴 Skin Detail Intensity", 0, 10, 5)
    
    submitted = st.form_submit_button("✨ Summon ElPrompt")
    st.markdown("</div>", unsafe_allow_html=True)

# ⚡ Output
if submitted:
    openings = [
        "An ultra realistic cinematic depiction of",
        "A high-quality concept of",
        "A photo-realistic masterpiece showing",
        "A detailed, emotional and realistic scene of",
        "A soft-lit yet powerful depiction of"
    ]

    extras = [
        "with cinematic lighting, realistic skin textures, natural imperfections, and mood-driven tone.",
        "captured with photo-like realism, perfect balance of light and depth.",
        "emphasizing storytelling through natural light, skin pores, and subtle reflections.",
        "immersed in soft realistic detail, vivid tone, and balanced contrast.",
        "featuring emotional depth, natural glow, and artistic shadow play."
    ]
    
    prompt = f"""/imagine prompt: {random.choice(openings)} {tema.lower()}, styled in {gaya} with {vibe} atmosphere. {random.choice(extras)}"""

    if use_photo:
        prompt += " Make sure to match face structure, lighting, and realism to the uploaded reference photo."

    prompt += f" Detail intensity level: {detail_level}/10."

    st.markdown('<div class="output-box">', unsafe_allow_html=True)
    st.markdown("### 💎 Prompt Siap Copy ke Gemini:")
    st.code(prompt, language="markdown")
    
    # Copy button
    copy_html = f"""
    <button class="copy-btn" onclick="navigator.clipboard.writeText(`{prompt}`)">📋 Salin Prompt</button>
    """
    st.markdown(copy_html, unsafe_allow_html=True)

    # Download file
    b64 = base64.b64encode(prompt.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="ElPrompt.txt"><button class="copy-btn">💾 Download .txt</button></a>'
    st.markdown(href, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="signature">crafted by Kael — elegance in every line.</div>', unsafe_allow_html=True)
