# app.py
import streamlit as st
import random
import json
from datetime import datetime
from PIL import Image

# ---------------------- Setup ----------------------
st.set_page_config(page_title="ElPrompt — Human Realism Edition (Deluxe)", layout="centered", page_icon="✨")

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------------- CSS & Animations ----------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&family=Poppins:wght@300;400;600&display=swap');

    :root{
        --bg1: #050608;
        --bg2: #081018;
        --glass: rgba(255,255,255,0.04);
        --accent1: #00ffe0;
        --accent2: #7c4dff;
        --muted: #9aa3a8;
    }

    html, body, [class*="css"]  {
        background: radial-gradient(1200px 600px at 10% 10%, rgba(12,30,40,0.25), transparent),
                    linear-gradient(180deg, var(--bg1), var(--bg2));
        color: #e8f6f4;
        font-family: Poppins, Montserrat, sans-serif;
    }

    .title {
        font-family: Montserrat, sans-serif;
        font-size: 48px;
        font-weight: 800;
        text-align: center;
        color: var(--accent1);
        letter-spacing: 1px;
        margin-top: 18px;
        margin-bottom: 4px;
        text-shadow: 0 6px 20px rgba(0,255,224,0.06);
    }

    .subtitle {
        text-align:center;
        color: var(--muted);
        margin-bottom: 16px;
        font-size:14px;
    }

    .card {
        background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
        border: 1px solid rgba(255,255,255,0.04);
        border-radius: 14px;
        padding: 18px;
        box-shadow: 0 8px 30px rgba(2,8,15,0.6), inset 0 1px 0 rgba(255,255,255,0.02);
        backdrop-filter: blur(6px) saturate(120%);
    }

    .row { display:flex; gap:12px; }
    .col-2 { width:66%; }
    .col-1 { width:34%; }

    .input-label { font-size:13px; color: var(--muted); margin-bottom:6px; }
    .muted { color: var(--muted); font-size:13px; }

    .ghost {
        background: transparent;
        border: 1px dashed rgba(255,255,255,0.03);
        padding:10px;
        border-radius:8px;
        text-align:center;
        color:var(--muted);
        font-size:13px;
    }

    .output-box {
        margin-top:16px;
        padding:18px;
        border-radius:12px;
        border: 1px solid rgba(0,255,224,0.06);
        background: linear-gradient(180deg, rgba(0,255,224,0.015), rgba(124,77,255,0.01));
    }

    .btn {
        background: linear-gradient(90deg, var(--accent1), #00a7d1);
        color: #021017;
        padding: 10px 16px;
        border-radius:10px;
        font-weight:700;
        border:none;
        cursor:pointer;
    }

    .btn-ghost {
        background: transparent;
        border: 1px solid rgba(255,255,255,0.06);
        color: var(--muted);
        padding:10px 14px;
        border-radius:10px;
        cursor:pointer;
    }

    .small-btn {
        padding:8px 10px;
        border-radius:8px;
        border:none;
        font-weight:700;
        cursor:pointer;
    }

    .preset {
        background: linear-gradient(90deg, #7c4dff, #00ffe0);
        color: #021017;
        padding:8px 10px;
        border-radius:8px;
        border:none;
        font-weight:700;
        cursor:pointer;
    }

    /* simple fade/slide animations */
    .fade-in { animation: fadeIn 0.45s ease both; }
    .slide-up { animation: slideUp 0.4s cubic-bezier(.2,.9,.3,1) both; }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(8px); }
        to { opacity:1; transform: translateY(0); }
    }
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(14px); }
        to { opacity:1; transform: translateY(0); }
    }

    textarea#elprompt_text {
        background: transparent;
        color: #e8f6f4;
        border: none;
        resize: vertical;
        font-family: monospace;
        font-size:13px;
    }

    .signature { text-align:center; color:var(--accent1); font-family: monospace; margin-top:14px; font-size:13px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------- Header ----------------------
st.markdown('<div class="title">ElPrompt</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Human Realism Edition (Deluxe) — ultra realistic prompts, skin detail, presets & photo-aware</div>', unsafe_allow_html=True)

# ---------------------- Utilities & Random samples ----------------------
def rand_theme():
    return random.choice([
        "seorang tukang bangunan minum kopi di atap saat golden hour",
        "workshop kayu dengan cahaya sore menerobos jendela",
        "etalase toko bahan bangunan dengan lampu neon senja",
        "pekerja memperbaiki atap di bawah gerimis halus",
        "interior toko rapi dengan produk tersusun, mood hangat"
    ])

def rand_style():
    return random.choice(["cinematic ultra realistic", "moody realism", "photo-realistic editorial", "magazine cover quality", "retro-futurism cinematic"])

def rand_vibe():
    return random.choice(["calm but powerful", "gloomy yet beautiful", "energetic and gritty", "melancholy with warmth", "mysterious and cinematic"])

# ---------------------- Preset buttons (set session_state and rerun) ----------------------
def set_preset(preset):
    if preset == "billboard":
        st.session_state.preset_tema = "besar, dramatis: poster billboard produk diskon, model memegang produk, lighting bold"
        st.session_state.preset_gaya = "magazine cover quality"
        st.session_state.preset_vibe = "energetic and gritty"
        st.session_state.preset_gender = "Netral"
    elif preset == "product":
        st.session_state.preset_tema = "close-up produk material bangunan di studio, shallow depth of field"
        st.session_state.preset_gaya = "photo-realistic editorial"
        st.session_state.preset_vibe = "calm but powerful"
        st.session_state.preset_gender = "Netral"
    elif preset == "portrait":
        st.session_state.preset_tema = "portrait pekerja bahan bangunan saat bekerja, fokus wajah dan tangan"
        st.session_state.preset_gaya = "cinematic ultra realistic"
        st.session_state.preset_vibe = "mysterious and cinematic"
        st.session_state.preset_gender = "Netral"
    st.experimental_rerun()

# ---------------------- Layout: inputs & quick actions ----------------------
left_col, right_col = st.columns([3,1])

with left_col:
    with st.form("elprompt_form"):
        st.markdown('<div class="card fade-in">', unsafe_allow_html=True)
        st.markdown('<div class="input-label">🧠 Tema / Ide (isi singkat, contoh di placeholder)</div>', unsafe_allow_html=True)
        # prefill from preset if present
        tema_default = st.session_state.pop("preset_tema", "")
        tema = st.text_input("", value=tema_default, placeholder="contoh: tukang bangunan santai minum kopi di atap saat senja")

        st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
        st.markdown('<div class="row">', unsafe_allow_html=True)

        # style & vibe side-by-side
        gaya_default = st.session_state.pop("preset_gaya", None)
        vibe_default = st.session_state.pop("preset_vibe", None)

        gaya = st.selectbox("🎨 Gaya / Style", ["cinematic ultra realistic","moody realism","brutalist","magazine cover quality","playful modern","retro-futurism"], index=0 if not gaya_default else ["cinematic ultra realistic","moody realism","brutalist","magazine cover quality","playful modern","retro-futurism"].index(gaya_default))
        vibe = st.selectbox("💫 Vibe / Emosi", ["calm but powerful","gloomy yet beautiful","energetic and gritty","melancholy with warmth","mysterious and cinematic"], index=0 if not vibe_default else ["calm but powerful","gloomy yet beautiful","energetic and gritty","melancholy with warmth","mysterious and cinematic"].index(vibe_default))
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="height:8px;"></div>', unsafe_allow_html=True)
        st.markdown('<div class="input-label">👤 Fokus Gender (opsional)</div>', unsafe_allow_html=True)
        gender_default = st.session_state.pop("preset_gender", "Netral")
        gender = st.radio("", options=["Netral","Pria","Wanita"], index=["Netral","Pria","Wanita"].index(gender_default), horizontal=True)

        st.markdown('<div style="height:8px;"></div>', unsafe_allow_html=True)
        st.markdown('<div class="input-label">📸 Pakai Foto Referensi? (opsional)</div>', unsafe_allow_html=True)
        use_photo = st.checkbox("Ya, saya mau pake foto referensi (upload setelah ini)", value=False)

        uploaded_file = None
        if use_photo:
            uploaded_file = st.file_uploader("Upload foto referensi (jpg/png) — wajah & tubuh sesuai referensi", type=["jpg","jpeg","png"])

        st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)

        # skin intensity slider
        st.markdown('<div class="input-label">🔬 Skin Detail Intensity</div>', unsafe_allow_html=True)
        skin_slider = st.slider("", min_value=0, max_value=2, value=1, format="%d")
        # map slider to words
        skin_level_map = {0: "subtle", 1: "medium", 2: "intense"}
        skin_level = skin_level_map.get(skin_slider, "medium")
        st.markdown(f'<div class="muted">Intensity: <strong>{skin_level}</strong> — kontrol strength untuk pori/imperfection detail</div>', unsafe_allow_html=True)

        st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
        submit = st.form_submit_button("✨ Summon ElPrompt")
        st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="card fade-in">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:14px;font-weight:700;color:var(--accent1)">Quick Actions / Presets</div>', unsafe_allow_html=True)
    st.markdown('<div style="height:8px;"></div>', unsafe_allow_html=True)

    if st.button("🎲 I'm bored — randomize"):
        st.session_state.temp_tema = rand_theme()
        st.session_state.temp_gaya = rand_style()
        st.session_state.temp_vibe = rand_vibe()
        # set as presets for form to pick up
        st.session_state.preset_tema = st.session_state.temp_tema
        st.session_state.preset_gaya = st.session_state.temp_gaya
        st.session_state.preset_vibe = st.session_state.temp_vibe
        st.experimental_rerun()

    st.markdown('<div style="height:8px;"></div>', unsafe_allow_html=True)

    # Preset buttons
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        if st.button("🏙️ Billboard"):
            set_preset("billboard")
    with col_b:
        if st.button("📸 Product"):
            set_preset("product")
    with col_c:
        if st.button("🧑 Portrait"):
            set_preset("portrait")

    st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)
    if st.button("🧾 Clear History"):
        st.session_state.history = []
        st.success("History cleared.")

    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="muted">Tips: upload foto untuk hasil mirip, atur skin intensity untuk seberapa nyata tekstur kulitnya.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------- Build Prompt Logic ----------------------
def skin_detail_phrase(level):
    if level == "subtle":
        return (
            "Maintain exact facial features and body proportions. Preserve identity and do not alter facial structure or body shape. "
            "Add subtle skin realism: fine visible pores, very light natural texture, minimal imperfections, slight natural dimples, and soft under-eye texture. "
            "Avoid smoothing; keep natural tone variations."
        )
    elif level == "medium":
        return (
            "Maintain exact facial features and body proportions. Preserve identity and do not alter facial structure or body shape. "
            "Enhance skin realism: visible pores, realistic fine texture, slight acne marks, natural dimples, and subtle under-eye bags — visible but tasteful. "
            "Avoid over-smoothing; preserve freckles and small scars if present."
        )
    else:  # intense
        return (
            "Maintain exact facial features and body proportions. Preserve identity and do not alter facial structure or body shape. "
            "Strong skin realism: pronounced pores, detailed skin texture, visible small acne marks, noticeable dimples/lesung pipi, clear under-eye texture, and natural scars/freckles. "
            "Do not change identity; keep all facial proportions intact."
        )

def build_prompt(tema, gaya, vibe, gender, uploaded_file, skin_level):
    base_openings = [
        "An ultra realistic photographic depiction of",
        "A hyper-detailed ultra realistic portrait/scene of",
        "A cinematic, photo-realistic capture of",
        "A studio-grade ultra realistic image of",
        "A high-fidelity, ultra realistic scene showing"
    ]
    opening = random.choice(base_openings)

    # gender phrase if specified
    gender_phrase = ""
    if gender == "Pria":
        gender_phrase = "a handsome man"
    elif gender == "Wanita":
        gender_phrase = "a beautiful woman"
    else:
        gender_phrase = "a person"

    skin_detail = skin_detail_phrase(skin_level)

    lighting_and_style = (
        "Photographic lighting, realistic shadows, natural reflections, depth of field, and cinematic color grading. "
        "Highly detailed textures, realistic hair strands, cloth detail, and environmental atmosphere."
    )

    if uploaded_file:
        prompt = (
            f"{opening} the {tema.strip()}. Use the uploaded reference photo for exact facial features, expression and lighting. "
            f"{skin_detail} {lighting_and_style} "
            f"Style: {gaya}. Mood/vibe: {vibe}. Match the reference person's identity and proportions — do not change identity. "
            "Output: ultra realistic, high-resolution, photographic render suitable for professional use."
        )
    else:
        prompt = (
            f"{opening} {gender_phrase} in scene: {tema.strip()}. {skin_detail} {lighting_and_style} "
            f"Style: {gaya}. Mood/vibe: {vibe}. Ensure ultra realistic human detail and natural imperfections. "
            "Output: ultra realistic, high-resolution, photographic result."
        )

    prompt = prompt.strip() + "\n\n✨ elprompt style has comin."
    return prompt

# ---------------------- Generate & Show Output ----------------------
generated = False
if "submit" in locals():
    pass  # placeholder to satisfy linters

if st.session_state.get("temp_tema") and not tema:
    tema = st.session_state.pop("temp_tema")
    gaya = st.session_state.pop("temp_gaya")
    vibe = st.session_state.pop("temp_vibe")

if st.session_state.get("preset_tema") and not tema:
    tema = st.session_state.pop("preset_tema")
    gaya = st.session_state.pop("preset_gaya")
    vibe = st.session_state.pop("preset_vibe")
    gender = st.session_state.pop("preset_gender")

# If the form was submitted:
if st.form_submit_button("noop"):  # dummy to avoid linter issues; actual submit managed above
    pass

# We check whether the user pressed the real submit by tracking the session state of form - use hidden workaround:
# Simpler: we rely on the actual submit variable from earlier (it exists because form_submit_button assigned to 'submit')
try:
    submit_pressed = submit
except NameError:
    submit_pressed = False

if submit_pressed:
    tema_val = tema if tema and tema.strip() else rand_theme()
    # determine skin_level string
    prompt_text = build_prompt(tema_val, gaya, vibe, gender, uploaded_file, skin_level)
    generated = True
else:
    prompt_text = ""

if generated:
    # preview uploaded image if exists
    if uploaded_file:
        try:
            img = Image.open(uploaded_file)
            st.markdown('<div class="card slide-up">', unsafe_allow_html=True)
            st.markdown('<div style="display:flex;gap:12px;align-items:center">', unsafe_allow_html=True)
            st.image(img, caption="📷 Reference Photo (uploaded)", use_column_width=False, width=220)
            st.markdown('<div style="flex:1;margin-left:8px">', unsafe_allow_html=True)
            st.markdown('<div class="muted">Reference detected — prompt will instruct to match facial features & lighting precisely.</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        except Exception:
            st.warning("Uploaded file could not be displayed (unsupported).")

    # store to history
    st.session_state.history.insert(0, {"prompt": prompt_text, "time": datetime.now().isoformat()})
    st.session_state.history = st.session_state.history[:50]

    # Output area
    st.markdown('<div class="card slide-up">', unsafe_allow_html=True)
    st.markdown('<div class="output-box">', unsafe_allow_html=True)
    st.markdown("### 💎 Prompt Siap (Gemini-ready & Ultra Realistic):")
    safe_prompt = prompt_text.replace("`", "'")
    st.markdown(f'<textarea id="elprompt_text" style="width:100%;height:180px;border:none;background:transparent;color:#e8f6f4;resize:vertical;font-family:monospace;padding:6px;">{safe_prompt}</textarea>', unsafe_allow_html=True)

    # JS copy function
    st.markdown(
        f"""
        <script>
        function el_copy() {{
            const el = document.getElementById('elprompt_text');
            if (!el) return;
            navigator.clipboard.writeText(el.value).then(()=>{{
                const btn = document.getElementById('el_copy_btn');
                btn.innerText = '✅ Copied';
                setTimeout(()=> btn.innerText = '📋 Copy Prompt', 1400);
            }});
        }}
        </script>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div style="display:flex;gap:10px;margin-top:8px">', unsafe_allow_html=True)
    st.markdown('<button id="el_copy_btn" class="btn" onclick="el_copy()">📋 Copy Prompt</button>', unsafe_allow_html=True)

    st.download_button(
        label="💾 Download Prompt (.txt)",
        data=prompt_text,
        file_name=f"elprompt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        mime="text/plain"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)  # close output-box
    st.markdown('</div>', unsafe_allow_html=True)  # close card

# ---------------------- History ----------------------
if st.session_state.history:
    st.markdown('<div class="card fade-in">', unsafe_allow_html=True)
    st.markdown("### 📚 Recent Prompts")
    for item in st.session_state.history[:8]:
        tstr = datetime.fromisoformat(item["time"]).strftime("%Y-%m-%d %H:%M:%S")
        short = item["prompt"].replace("\n"," ")[:180]
        st.markdown(f"- `{tstr}` — {short}...")
    # download all history
    if st.button("⬇️ Download All (JSON)"):
        st.download_button(
            label="Download JSON",
            data=json.dumps(st.session_state.history, ensure_ascii=False, indent=2),
            file_name=f"elprompt_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------- Footer ----------------------
st.markdown('<div class="signature">crafted with taste — elprompt style has comin.</div>', unsafe_allow_html=True)
