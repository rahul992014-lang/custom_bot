import streamlit as st
from groq import Groq

st.set_page_config(page_title="Rahul's Roast Bot", page_icon="🔥", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: #F7F7F8;
}
h1 {
    text-align: center;
    font-size: 2.2rem;
}
.subtitle {
    text-align: center;
    color: #6b6b6b;
    margin-bottom: 1.5rem;
}
[data-testid="stChatMessage"] {
    border-radius: 12px;
    padding: 0.6rem 1rem !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🔥 Rahul's Roast Bot")
st.markdown('<div class="subtitle">Paste your code and get roasted (then actually helped).</div>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Create client once instead of on every message
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

for msg in st.session_state.messages:
    avatar = "🔥" if msg["role"] == "assistant" else "🧑‍💻"
    with st.chat_message(msg["role"], avatar=avatar):
        st.write(msg["content"])

prompt = st.chat_input("Paste your code or ask something...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user", avatar="🧑‍💻"):
        st.write(prompt)

    with st.chat_message("assistant", avatar="🔥"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a hilarious, brutally sarcastic senior developer "
                                "who roasts code the user pastes in. Be funny and savage "
                                "about bad practices, naming, comments, and structure — "
                                "but ALWAYS follow up with genuinely useful, correct fixes. "
                                "Roast first, then help for real."
                            ),
                        },
                        *st.session_state.messages,
                    ],
                )
                reply = response.choices[0].message.content.strip()
            except Exception as e:
                reply = f"Oops, something broke: {e}"

        st.write(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})