import streamlit as st
import google.generativeai as genai
import os

# Retrieve API Key from streamlit secrets or environment variable
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

# Sidebar setup for API Key if not already configured
if not api_key:
    st.sidebar.subheader("Configuration")
    api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")
    if not api_key:
        st.sidebar.warning("🔑 Gemini API Key is required. You can get one from Google AI Studio.")

# Configure the Gemini SDK if key is available
if api_key:
    genai.configure(api_key=api_key)

def generate_email_reply(user_email, tone="polite", opinion="", api_key=None):
    if not api_key:
        return "⚠️ Error: Gemini API Key is missing. Please provide it in the sidebar or via secrets."
    
    try:
        model = genai.GenerativeModel("gemini-3.6-flash")
        
        full_prompt = (
            f"You are a smart and helpful email assistant. Your task is to generate a clear, {tone} reply to the email below.\n\n"
            f"{f'Reflect this decision in your response: {opinion}\n\n' if opinion else ''}"
            f"--- Example ---\n"
            f"Email: Hi, can we move the meeting to Friday?\n"
            f"Reply: Sure, Friday works for me. Thanks for the update.\n\n"
            f"--- Incoming Email ---\n{user_email}\n\n"
            f"--- Your Reply ---"
        )
        
        response = model.generate_content(
            full_prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.8,
                max_output_tokens=300,
            )
        )
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error generating reply: {str(e)}"

# --- Streamlit UI ---
st.set_page_config(page_title="Smart Email Reply Assistant", page_icon="📧")
st.title("📧 Smart Email Reply Assistant")
st.write("Generate professional, polite, or assertive replies to emails using Google Gemini.")

email_input = st.text_area("✉️ Paste the incoming email:", height=200)
tone = st.selectbox("🎯 Choose reply tone:", ["polite", "friendly", "formal", "assertive"])
opinion_input = st.text_area("🗣️ Optional: Add your stance or decision (e.g., 'Yes, I’m okay with rescheduling.')", height=100)

if st.button("🚀 Generate Reply"):
    if not email_input.strip():
        st.warning("Please enter an email to generate a reply.")
    elif not api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
    else:
        with st.spinner("Generating reply..."):
            reply = generate_email_reply(email_input, tone, opinion_input.strip(), api_key)
        st.subheader("📝 Suggested Reply")
        st.success(reply)


