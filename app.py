from flask import Flask, request, jsonify
import random
import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (only first run)
nltk.download('punkt')

app = Flask(__name__)

# Define chatbot pairs (pattern → response)
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! How may I help you?"]
    ],
    [
        r"(.*) your name?",
        ["I am your AI Chatbot.", "You can call me Virtual Assistant!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you! How about you?", "Great! Thanks for asking."]
    ],
    [
        r"(.*) (help|support)",
        ["Sure! Please tell me your issue.", "I am here to support you. What do you need help with?"]
    ],
    [
        r"(.*) created you?",
        ["I was created as part of an AI Chatbot Development project!", "My creator is a developer like you."]
    ],
    [
        r"(.*) (bye|exit)",
        ["Goodbye! Have a great day.", "See you soon!"]
    ],
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

@app.route("/")
def home():
    return "AI Chatbot is running! Send requests to /chat"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chatbot.respond(user_input)
    if not response:
        response = "Sorry, I didn’t understand that. Can you rephrase?"
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
