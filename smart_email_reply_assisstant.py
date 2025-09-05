import streamlit as st
import requests
import json

API_KEY = st.secrets["API_KEY"]
PROJECT_ID = st.secrets["PROJECT_ID"]
REGION = "us-south"
MODEL_ID = "ibm/granite-13b-instruct-v2"
API_VERSION = "2023-05-29"
ENDPOINT = f"https://{REGION}.ml.cloud.ibm.com/ml/v1/text/generation?version={API_VERSION}"

def get_iam_token(api_key):
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": api_key
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]


def generate_email_reply(user_email, tone="polite", opinion=""):
    access_token = get_iam_token(API_KEY)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

   
    full_prompt = (
        f"You are a smart and helpful email assistant. Your task is to generate a clear, {tone} reply to the email below.\n\n"
        f"{f'Reflect this decision in your response: {opinion}\n\n' if opinion else ''}"
        f"--- Example ---\n"
        f"Email: Hi, can we move the meeting to Friday?\n"
        f"Reply: Sure, Friday works for me. Thanks for the update.\n\n"
        f"--- Incoming Email ---\n{user_email}\n\n"
        f"--- Your Reply ---"
    )

    payload = {
        "model_id": MODEL_ID,
        "project_id": PROJECT_ID,
        "input": full_prompt,
        "parameters": {
            "decoding_method": "sample",
            "temperature": 0.8,
            "top_p": 0.9,
            "max_new_tokens": 300,
            "repetition_penalty": 1.05
        }
    }

    response = requests.post(ENDPOINT, headers=headers, json=payload)
    result = response.json()

    if "results" in result:
        return result["results"][0]["generated_text"]
    else:
        return "⚠️ Error: " + result.get("errors", [{}])[0].get("message", "Unknown error.")

# --- Streamlit UI ---
st.set_page_config(page_title="Smart Email Reply Assistant", page_icon="📧")
st.title("📧 Smart Email Reply Assistant")
st.write("Generate professional, polite, or assertive replies to emails using IBM Watsonx.")

email_input = st.text_area("✉️ Paste the incoming email:", height=200)
tone = st.selectbox("🎯 Choose reply tone:", ["polite", "friendly", "formal", "assertive"])
opinion_input = st.text_area("🗣️ Optional: Add your stance or decision (e.g., 'Yes, I’m okay with rescheduling.')", height=100)

if st.button("🚀 Generate Reply"):
    if not email_input.strip():
        st.warning("Please enter an email to generate a reply.")
    else:
        with st.spinner("Generating reply..."):
            reply = generate_email_reply(email_input, tone, opinion_input.strip())
        st.subheader("📝 Suggested Reply")
        st.success(reply)

