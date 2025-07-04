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

## Example

**Input:**  
Hi,
I hope you're doing well. I wanted to follow up on the budget report we discussed in last week's meeting. We were initially aiming to finalize and submit it by this Friday, but due to a few unforeseen delays in data collection and analysis, we might need some extra time.
Would it be possible to extend the deadline to next Wednesday? This would give the team sufficient time to double-check the figures and ensure the report is as accurate and comprehensive as possible.
Please let me know if this works for you or if we need to explore other alternatives.
Thanks in advance for your understanding and support.

Best regards,  
Ananya

**Generated Reply:**  
Hi Ananya,
I can certainly understand the need for extra time to complete the report. However, I need to ask you a couple of questions.
Does the PAC have a weekly meeting on Thursdays? Do you have any conflicts?
Also, we need to discuss some alternative strategies for the budget process.
For example, if we can turn this report into a presentation for the PAC, could we use a portion of the presentation to address other topics and perhaps have an impact analysis?
Your reply is greatly appreciated.
Thanks,
---

## Screenshots  
**App Home Page**

![App Input Screenshot](https://github.com/Krishna1838/smart-email-reply-assisstant/blob/main/INPUT.png?raw=true)

**Generated Reply Example**

![App Output Screenshot](https://github.com/Krishna1838/smart-email-reply-assisstant/blob/main/OUTPUT.png?raw=true)

---

## Project Structure

- `smart_email_reply_assisstant.py` – Main Streamlit application  
- `requirements.txt` – Python dependencies  
- `README.md` – Project documentation

---

## Results

- The assistant generates short, clear, and appropriate email replies.
- Supports any casual, professional, or generic email messages.
- Fast response with seamless UI.

---

## Author

- **Student Name:** Krishna Vardhan Baratam 
- **College Name:** VIT-AP  
- **Email:** vardhanbaratam@gmail.com

---

## License

This project is for educational purposes.

