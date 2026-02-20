import streamlit as st
import requests

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Bhagavad Gita Wisdom Portal",
    page_icon="🕉️",
    layout="centered"
)

# -----------------------------
# Modern CSS
# -----------------------------
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: Inter, system-ui, sans-serif;
    background: radial-gradient(circle at top, #111827, #030712 65%);
    color: #e5e7eb;
}

.block-container {
    max-width: 760px;
    padding-top: 2.5rem;
}

.title {
    text-align: center;
    font-size: 2.4rem;
    font-weight: 700;
    background: linear-gradient(90deg, #60a5fa, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    color: #9ca3af;
    font-size: 0.95rem;
    margin-bottom: 2rem;
}

/* Input */
.stTextInput input {
    border-radius: 14px;
    background: rgba(31, 41, 55, 0.85);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 0.7rem;
}

/* Button */
.stButton>button {
    width: 100%;
    border-radius: 14px;
    font-weight: 500;
    padding: 0.65rem;
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    border: none;
}

/* Q&A cards */
.chat {
    background: rgba(31, 41, 55, 0.75);
    backdrop-filter: blur(10px);
    border-radius: 14px;
    padding: 1rem 1.1rem;
    margin-top: 1.2rem;
    border: 1px solid rgba(255,255,255,0.04);
}

.user {
    box-shadow: inset 3px 0 0 #22c55e;
}

.assistant {
    box-shadow: inset 3px 0 0 #3b82f6;
}

.role {
    font-size: 0.75rem;
    color: #9ca3af;
    margin-bottom: 0.25rem;
}

/* Footer */
.footer {
    text-align: center;
    color: #6b7280;
    font-size: 0.8rem;
    margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("<div class='title'>🕉️ GitaGPT – Bhagavad Gita Knowledge Engine</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='subtitle'>AI-powered answers grounded strictly in the verses of the Bhagavad Gita</div>",
    unsafe_allow_html=True
)

# -----------------------------
# API
# -----------------------------
API_URL = "http://127.0.0.1:8000/ask"

# -----------------------------
# Session state (single-shot)
# -----------------------------
if "qa" not in st.session_state:
    st.session_state.qa = None

if "input_key" not in st.session_state:
    st.session_state.input_key = 0  # forces input reset

# -----------------------------
# Input
# -----------------------------
question = st.text_input(
    label="Question",
    placeholder="Ask a factual question (e.g. what  are core values mentioned?)",
    label_visibility="collapsed",
    key=f"question_{st.session_state.input_key}"
)

ask_button = st.button("Search Documents")

# -----------------------------
# Handle question
# -----------------------------
if ask_button and question.strip():
    # remove previous Q&A
    st.session_state.qa = None

    with st.spinner("Analyzing documents…"):
        try:
            response = requests.post(
                API_URL,
                params={"question": question},
                timeout=120
            )

            if response.status_code == 200:
                answer = response.json().get("answer", "")
            else:
                answer = "⚠️ Server error."

        except Exception as e:
            answer = f"⚠️ API connection failed: {e}"

    # store current Q&A only
    st.session_state.qa = (question, answer)

    # clear input box
    st.session_state.input_key += 1
    st.rerun()

# -----------------------------
# Display single Q&A
# -----------------------------
if st.session_state.qa:
    q, a = st.session_state.qa

    st.markdown(
        f"""
        <div class='chat user'>
            <div class='role'>Question</div>
            {q}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class='chat assistant'>
            <div class='role'>Answer</div>
            {a}
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        text-align: center;
        padding: 12px;
        background-color: #0f172a;
        color: #cbd5e1;
        font-size: 14px;
        font-family: 'Segoe UI', sans-serif;
    }

    .footer a {
        color: #60a5fa;
        text-decoration: none;
        font-weight: 600;
    }

    .footer a:hover {
        color: #3b82f6;
        text-shadow: 0 0 8px rgba(96,165,250,0.7);
    }
    </style>

    <div class='footer'>
        Made with ❤️ by 
        <a href="https://github.com/hrithikumbarji" target="_blank">
            Hrithik Umbarji
        </a>
    </div>
    """,
    unsafe_allow_html=True
)