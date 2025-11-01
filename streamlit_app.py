import streamlit as st
import random
import html as html_lib

st.set_page_config(page_title="ElPrompt — The Art of Lazy Creativity", layout="centered")

# (CSS + header same as before — dipersingkat di contoh ini)
st.markdown("""
<style>
body { background: radial-gradient(circle at top, #111, #000); color: #fff; font-family: 'Poppins', sans-serif; }
.title { font-size: 50px; font-weight: 800; text-align: center; color: #00FFE0; letter-spacing: 2px; text-shadow: 0 0 20px #00FFE0; margin-top: 40px; }
.subtitle { text-align: center; color: #aaa; font-size: 16px; margin-bottom: 50px; font-style: italic; }
.form-box { background-color: rgba(255,255,255,0.05); padding: 30px; border-radius: 20px; box-shadow: 0 0 15px rgba(0,0,0,0.4); backdrop-filter: blur(10px); }
.output-box { background-color: rgba(255,255,255,0.08); padding: 25px; border-radius: 15px; margin-top: 30px; box-shadow: inset 0 0 15px rgba(0,255,224,0.3); position: relative; }
.copy-button { display:block; width:100%; margin-top:12px; background: linear-gradient(90deg,#00FFE0,#00B8D4); color:#000; font-weight:700; font-size:15px; border-radius:8px; padding:10px; border:none; cursor:pointer; }
.copy-button:hover { transform: scale(1.02); box-shadow:0 0 15px #00FFE0; }
.signature { text-align:center; color:#00FFE0; font-size:14px; margin-top:24px; font-family:monospace; }
pre { white-space: pre-wrap; word-wrap: break-word; font-family: inherit; background: transparent; color: #e6fff9; padding:0; margin:0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">ElPrompt</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">the art of lazy creativity — when boredom meets style</div>', unsafe_allow_html=True)

# Input form (3 fields)
with st.form("elprompt_form"):
    st.markdown('<div class="form-box">', unsafe_allow_html=True)
    tema = st.text_input(
        "🧠 Tema / Ide dasar",
        placeholder="contoh: suasana pagi di toko bangunan, burnout di kantor, sunset di atap gedung"
    )
    gaya = st.selectbox(
        "🎨 Gaya / Nuansa",
        ["cinematic", "dreamy", "brutalist", "magazine style", "moody realism", "playful modern", "retro-futurism"]
    )
    vibe = st.selectbox(
        "💫 Vibe / Emosi",
        ["gloomy", "energetic", "calm", "chaotic", "romantic", "mysterious", "absurd", "melancholy"]
    )
    submit = st.form_submit_button("🚀 summon elprompt")
    st.markdown("</div>", unsafe_allow_html=True)

# Build prompt and show with a real-copy button
if submit:
    openings = [
        "An ultra realistic cinematic depiction of",
        "A high-quality ultra realistic concept of",
        "A masterpiece ultra realistic photo showing",
        "A hyper-detailed ultra realistic scene of",
        "A photo-realistic, finely detailed image describing"
    ]

    extras = [
        "Cinematic color grading, realistic textures, natural lighting, deep composition, and storytelling atmosphere.",
        "Hyper-detailed lighting, balanced shadows, soft reflections, emotional depth, and lifelike realism.",
        "Atmospheric realism with photographic precision and cinematic tones.",
        "Rich composition with dynamic light and ultra-clear definition.",
        "Immersive depth of field, soft light, and mood-driven realism."
    ]

    prompt = f"""/imagine prompt: {random.choice(openings)} {tema.lower()}, in {gaya} style with {vibe} mood. {random.choice(extras)}"""

    # Escape prompt text for safe HTML insertion
    prompt_html = html_lib.escape(prompt)

    # Render output box + a proper JS copy button that reads the prompt text from the <pre> element
    html_block = f"""
    <div class="output-box">
      <h3>💎 Prompt Siap Copy ke Gemini:</h3>
      <pre id="elprompt_text">{prompt_html}</pre>

      <button class="copy-button" id="elprompt_copy_btn">💾 Salin Prompt ke Gemini</button>

      <script>
        const btn = document.getElementById('elprompt_copy_btn');
        const pre = document.getElementById('elprompt_text');
        btn.addEventListener('click', async () => {{
          try {{
            await navigator.clipboard.writeText(pre.innerText);
            const old = btn.innerText;
            btn.innerText = '✓ Copied';
            setTimeout(() => {{ btn.innerText = old; }}, 1400);
          }} catch (err) {{
            // fallback: select text and alert
            const range = document.createRange();
            range.selectNodeContents(pre);
            const sel = window.getSelection();
            sel.removeAllRanges();
            sel.addRange(range);
            document.execCommand('copy');
            sel.removeAllRanges();
            const old = btn.innerText;
            btn.innerText = '✓ Copied';
            setTimeout(() => {{ btn.innerText = old; }}, 1400);
          }}
        }});
      </script>
    </div>
    <div class="signature">✨ elprompt style has comin.</div>
    """

    st.markdown(html_block, unsafe_allow_html=True)
