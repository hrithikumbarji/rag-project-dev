import streamlit as st
import requests

# 1. Page Config
st.set_page_config(
    page_title="GitaGPT - Divine Wisdom",
    page_icon="🕉️",
    layout="centered"
)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Inter:wght@400;500&display=swap" rel="stylesheet">
<style>
    /* Global Styles */
    .stApp {
        background: radial-gradient(circle at center, #2D1B08 0%, #0F0904 100%) !important;
    }
    
    [data-testid="stHeader"] {
        background: rgba(0,0,0,0) !important;
    }

    /* Typography */
    h1, h2, h3, p, div {
        color: #FDF4E3 !important;
        font-family: 'Inter', sans-serif;
    }

    /* Input & Button Styling */
    div[data-baseweb="input"] {
        background-color: rgba(253, 244, 227, 0.05) !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        border-radius: 20px !important;
    }
    
    .stButton>button {
        background: linear-gradient(90deg, #FF8C00, #FFD700) !important;
        color: #2D1B08 !important;
        font-family: 'Playfair Display', serif !important;
        font-weight: 700 !important;
        border-radius: 20px !important;
        border: none !important;
        width: 100%;
    }

    /* Q&A Chat Bubbles */
    .spiritual-card {
        background: rgba(45, 27, 8, 0.6);
        backdrop-filter: blur(12px);
        border-radius: 18px;
        padding: 1.5rem;
        margin-top: 1rem;
        border: 1px solid rgba(212, 175, 55, 0.15);
        line-height: 1.6;
    }
    
    .user-border { border-left: 5px solid #FF9933; }
    .assistant-border { border-left: 5px solid #FFD700; background: rgba(255, 215, 0, 0.03); }
    
    .role-label {
        font-family: 'Playfair Display', serif;
        color: #FF9933;
        font-weight: bold;
        text-transform: uppercase;
        font-size: 0.8rem;
        margin-bottom: 5px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🕉️ GitaGPT", text_alignment="center")
st.markdown("<p style='text-align: center; font-family: Playfair Display; font-style: italic; color: #D4AF37;'>Ground your curiosity in the eternal verses of the Bhagavad Gita</p>", unsafe_allow_html=True)


import streamlit as st
import requests


# 2. API & Logic
API_URL = "http://127.0.0.1:8000/ask"

if "qa_result" not in st.session_state:
    st.session_state.qa_result = None
if "input_key" not in st.session_state:
    st.session_state.input_key = 0

# 5. Interaction UI
question = st.text_input(
    "Ask the Gita", 
    placeholder="Seek guidance from the Lord...", 
    label_visibility="collapsed",
    key=f"q_{st.session_state.input_key}"
)

if st.button("Seek Wisdom") and question.strip():
    with st.spinner("Meditating on the verses..."):
        try:
            res = requests.post(API_URL, params={"question": question}, timeout=60)
            if res.status_code == 200:
                st.session_state.qa_result = res.json()
            else:
                st.error("The temple is currently closed (API Error).")
        except Exception as e:
            st.error(f"Connection error: {e}")
    st.session_state.input_key += 1
    st.rerun()

# 3. Results Section
if st.session_state.qa_result:
    data = st.session_state.qa_result
    
    # User's Question
    st.markdown(f"<div class='spiritual-card user-border'><div class='role-label'>Seeker</div>{question}</div>", unsafe_allow_html=True)

# 4. The HyDE Expansion (Reasoning)
    if "hyde_expansion" in data:
        with st.expander("✨ Divine Interpretation (Internal Reasoning)"):
            st.write(data["hyde_expansion"])
            st.caption("This paragraph was generated to bridge the gap between your modern query and ancient wisdom.")

# 5. The Final Answer
    st.markdown(f"""
        <div class='spiritual-card assistant-border'>
            <div class='role-label'>Eternal Wisdom</div>
            {data.get('answer')}
        </div>
    """, unsafe_allow_html=True)

# 6. Source Attribution
    if data.get("sources"):
        st.markdown("<div style='margin-top:10px; font-weight:bold; color:#FFD700;'>📜 Sources:</div>", unsafe_allow_html=True)
        st.write(", ".join([f"`{s}`" for s in data["sources"]]))

# 7. Spiritual Footer
st.markdown(
    """
    <br>
    <hr style='border-color: rgba(212, 175, 55, 0.1);'>
    <p style='text-align: center; color: #D4AF37; font-size: 0.8rem;'>
        Humbly crafted by 
        <a href="https://github.com/hrithikumbarji" 
           target="_blank" 
           style="color:#D4AF37; text-decoration:none; font-weight:600;">
           Hrithik Umbarji
        </a>
    </p>
    """,
    unsafe_allow_html=True
)