# Rahul's Roast Bot 🔥

A Streamlit chatbot that roasts your code — brutally, sarcastically, and then actually helps you fix it. Powered by the [Groq API](https://groq.com/) running the `openai/gpt-oss-120b` model.

## What It Does

Paste in a code snippet (or ask it anything), and the bot responds as a savage, sarcastic senior developer who:
1. Roasts your naming, comments, structure, and bad practices — for laughs.
2. Follows up with genuinely correct, useful fixes.

## Features

- 💬 Persistent chat interface using Streamlit's native `st.chat_message` and `st.chat_input`
- 🧠 Maintains full conversation history across turns (sent to the model each time for context)
- 🔥 Custom roast-focused system prompt
- 🎨 Clean, minimal light-themed UI with custom avatars
- 🛡️ Error handling — a failed API call shows a friendly error instead of crashing the app
- ⚡ Powered by Groq's fast LLM inference

## Requirements

- Python 3.9+
- A [Groq API key](https://console.groq.com/keys)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Setup

This app requires a Groq API key stored securely using Streamlit's secrets management.

1. Create a folder named `.streamlit` in the project root (if it doesn't already exist).
2. Inside it, create a file named `secrets.toml`.
3. Add your API key:

   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```

> ⚠️ **Never commit `secrets.toml` to version control.** Add it to your `.gitignore`.

## Running the App

```bash
streamlit run llm_bot.py
```

This will open the app in your default browser (usually at `http://localhost:8501`).

## How It Works

1. Chat history is stored in `st.session_state.messages` so it persists across Streamlit reruns.
2. The Groq client is created once at startup rather than on every message.
3. Each time the user sends a message, it's appended to the history and displayed.
4. The full conversation, plus a system prompt instructing the model to roast-then-fix, is sent to the Groq API.
5. If the API call fails, the error is caught and shown as the bot's reply instead of crashing the app.
6. The model's reply is displayed and appended to history, so future requests include full context.

## Project Structure

```
.
├── llm_bot.py             # Main Streamlit app
├── requirements.txt        # Python dependencies
├── .streamlit/
│   └── secrets.toml        # API key (not committed to git)
└── README.md
```

## Customization

- **Change the model:** edit the `model` parameter in `client.chat.completions.create(...)`.
- **Change the bot's personality:** edit the `system` message content.
- **Change the theme:** edit the CSS block near the top of the file.

## License

This project is open source. Feel free to modify and use it for your own purposes.
