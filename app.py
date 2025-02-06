from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import datetime
import wikipedia
import openai
import os
from openai import OpenAI
from dotenv import load_dotenv
import webbrowser

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# Flask and SocketIO setup
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Greet the user
def greet_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        return "Good Morning! How can I assist you today?"
    elif 12 <= hour < 18:
        return "Good Afternoon! How can I assist you today?"
    else:
        return "Good Evening! How can I assist you today?"

# Process user commands
@socketio.on("user_message")
def handle_user_message(data):
    query = data.get("message", "").lower()
    
    if "wikipedia" in query:
        try:
            query = query.replace("wikipedia", "").strip()
            result = wikipedia.summary(query, sentences=2)
            response = f"According to Wikipedia: {result}"
        except:
            response = "Sorry, I couldn't fetch information from Wikipedia."
    
    elif "time" in query:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The time is {now}."

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif "goodbye" in query or "bye" in query:
        response = "Goodbye! Have a great day!"
        emit("server_message", {"message": response})
        return
    
    else:
        # Use OpenAI GPT for responses
        try:
            ai_response = client.chat.completions.create(
                model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Be precise and to the point."},
                {"role": "user", "content": query},
            ],
            temperature=0.2,
        )
            response = ai_response.choices[0].message.content
            
        except Exception:
            response = "I'm sorry, I couldn't process that request."

    emit("server_message", {"message": response})

# Main route for the frontend
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, debug=True)






