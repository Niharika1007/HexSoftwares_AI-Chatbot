# AI Chatbot Development

## Project Overview
This project is an AI-powered chatbot that can handle customer inquiries, provide support, and engage users in human-like conversations. The chatbot leverages **Natural Language Processing (NLP)** using Python's `nltk` library and is served via a **Flask API**.  

It can be accessed via **terminal (PowerShell / curl / Postman)** or through a simple **web frontend** (`index.html`).  

---

## Features
- Conversational AI capable of responding to greetings, queries, and support requests.  
- Rule-based NLP responses using `nltk.chat.util.Chat`.  
- Flask backend API for handling messages.  
- Optional HTML frontend for interactive chat.  
- Easily extendable to handle more patterns and integrations.  

---

## Project Structure
AI_Chatbot/
│── app.py # Backend Flask application
│── index.html # Frontend chat UI (optional)
│── requirements.txt
│── README.md
│── venv/ # (Optional virtual environment)

---

## Installation & Setup

### 1. Clone the Repository
git clone https://github.com/<USERNAME>/AI_Chatbot.git
cd AI_Chatbot
#Virtual Environment
python -m venv venv
# Activate it:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
pip install -r requirements.txt     #Dependencies

Example Queries & Responses
User Input	Bot Response
hello / hi / hey	- Hello! How can I assist you today?
who created you?	- I was created as part of an AI Chatbot Development project!
how are you?	- I'm doing well, thank you! How about you?
I need help / support	- I am here to support you. What do you need help with?
bye / exit	- Goodbye! Have a great day.
unrecognized input	- Sorry, I didn’t understand that. Can you rephrase?

# Technologies Used
Python 3.x
Flask – backend API
NLTK – Natural Language Processing
HTML/CSS/JavaScript – optional frontend

# Future Enhancements
Integrate machine learning-based NLP for smarter responses.
Deploy chatbot on websites, messaging apps, or social media.
Add database support to remember user interactions.


---

If you want, I can also make a **version with embedded screenshots + step-by-step execution guide** ready for your internship report so it looks very professional.  

Do you want me to create that too?
