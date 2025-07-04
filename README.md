# 📧 Smart Email Reply Assistant 

This project is a Streamlit-based AI assistant that generates smart, context-aware email replies using IBM Watsonx foundation models via the `/ml/v1/text/generation` endpoint. It simulates a human-like email response experience and is designed for students and professionals who want quick, polite replies.

---

## 🚀 Live Demo

🌐 [Click here to try the app](https://smartemailreplygenerator.streamlit.app/)

---

## 🎯 Features

- 📝 Accepts any incoming email content
- 🤖 Calls IBM Watsonx AI models like `flan-ul2` or `flan-t5-xxl`
- ✉️ Generates a professional, relevant reply
- 🧠 Context-aware and polite responses
- 🔐 Secures credentials via Streamlit secrets

---

## 🔧 How It Works

1. User pastes or types an incoming email into the text box.
2. The app constructs a prompt and sends it to the IBM Watsonx `/generation` API.
3. The API returns a natural language reply.
4. The app displays the reply instantly to the user.

---
