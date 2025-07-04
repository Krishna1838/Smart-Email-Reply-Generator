import streamlit as st
import requests
import json

API_KEY = st.secrets["API_KEY"]
PROJECT_ID = st.secrets["PROJECT_ID"]
REGION = "us-south"
API_VERSION = "2023-05-29"
MODEL_ID = "google/flan-t5-xxl"
ENDPOINT = f"https://{REGION}.ml.cloud.ibm.com/ml/v1/text/generation?version={API_VERSION}"

def get_iam_token(api_key):
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": api_key
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]

def generate_email_reply(prompt, tone="polite"):
    access_token = get_iam_token(API_KEY)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    full_prompt = (
        f"Here is an example of how to respond to an email in a {tone} and professional tone:\n"
        f"Email: Can we move our meeting to Friday?\n"
        f"Reply: Sure, Friday works for me. Looking forward to it.\n\n"
        f"Now respond to this email:\n"
        f"Email: {prompt}\n"
        f"Reply:"
    )

    payload = {
        "model_id": MODEL_ID,
        "project_id": PROJECT_ID,
        "input": full_prompt,
        "parameters": {
            "decoding_method": "sample",
            "temperature": 0.9,
            "top_p": 0.9,
            "max_new_tokens": 300
        }
    }

    response = requests.post(ENDPOINT, headers=headers, json=payload)
    result = response.json()

    if "results" in result:
        return result["results"][0]["generated_text"]
    else:
        return "⚠️ Error: " + result.get("errors", [{}])[0].get("message", "Unknown error.")

st.title("📧 Smart Email Reply Assistant")

email_input = st.text_area("Paste the incoming email:")
tone = st.selectbox("Choose reply tone:", ["polite", "friendly", "formal", "assertive"])

if st.button("Generate Reply"):
    if not email_input.strip():
        st.warning("Please paste an email first.")
    else:
        with st.spinner("Generating reply..."):
            reply = generate_email_reply(email_input, tone)
        st.subheader("✉️ Suggested Reply")
        st.write(reply)
