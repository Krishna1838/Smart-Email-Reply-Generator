import streamlit as st
import requests
import json

API_KEY = "jdaEaORCg7SJI_zmhCPIW2D9DT80wyY3_PtLMkTeV-Ab"
PROJECT_ID = "cd9e377c-3c7a-4c55-93b3-9f7c0d2f103a"
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
        f"You are a helpful AI assistant. Write a professional and {tone} reply to the following email:\n\n{prompt}"
    )

    payload = {
        "model_id": MODEL_ID,
        "project_id": PROJECT_ID,
        "input": full_prompt,
        "parameters": {
            "decoding_method": "greedy",
            "temperature": 0.7,
            "max_new_tokens": 150
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
