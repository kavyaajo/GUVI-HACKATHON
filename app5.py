from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

responses = {
    "hello": "Hi there! How can I assist you?",
    "help": "I am here to help! Please describe your situation.",
    "how are you": "I'm just a chatbot, but I'm here to help!",
    "good morning": "Good morning! Stay safe and have a great day!",
    "good night": "Good night! Take care and stay safe!"

}
responses.update({
    "help": "I am here to help! Please describe your situation.",
    "emergency": "If you're in danger, call emergency services immediately!",
    "lost": "Stay calm! Can you share your location so I can guide you?",
    "stalking": "Stay in a safe place and reach out to someone you trust!",
})


@app.route("/")  # Add this route
def home():
    return render_template("indexh.html")  # Ensure "indexh.html" is in the "templates" folder

@app.route("/chat", methods=["POST"])  
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()
    bot_response = responses.get(user_message, "I'm here to help. Please describe your situation.")
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
