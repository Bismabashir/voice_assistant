# Voice Assistant with Web Interface

## 📌 Overview
This project is a **voice assistant with a web interface** that allows users to interact via both **text chat and voice commands**. It utilizes **Flask**, **Flask-SocketIO**, **OpenAI GPT-4o-mini**, and **Wikipedia API** to respond to user queries in real-time.

---
## 🚀 Features
✅ **Real-time Chat & Voice Interaction**: Users can send messages or use voice commands.  
✅ **Wikipedia Integration**: Fetches short summaries from Wikipedia for queries.  
✅ **Time & Web Control**: Can tell the current time and open popular websites like YouTube or Google.  
✅ **AI-Powered Responses**: Uses OpenAI GPT-4o-mini for natural language responses.  
✅ **WebSocket Communication**: Ensures seamless real-time updates between the server and the frontend.

---
## 🛠️ Technologies Used
- **Python** (Flask, Flask-SocketIO)
- **JavaScript, HTML, CSS** (Frontend for chat & voice commands)
- **Wikipedia API** (For fetching information)
- **OpenAI API** (For intelligent responses)
- **WebSockets** (For real-time communication)

---
## 📂 Project Structure
```
voice-assistant/
│── static/
│   ├── styles.css       # Frontend styling
│   ├── script.js        # JavaScript for voice & chat interaction
│── templates/
│   ├── index.html       # Web interface
│── app.py               # Main Flask application
│── .env                 # Stores OpenAI API key
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
```

---
## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up OpenAI API Key
Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_actual_api_key
```

### 4️⃣ Run the Flask Application
```bash
python app.py
```
The server will start at **http://127.0.0.1:5000/**.

---
## ⚡ How It Works
1️⃣ Open the web interface (`index.html`) in a browser.
2️⃣ Type or speak your query (e.g., *"Tell me about Python"*).
3️⃣ The assistant processes the request and responds in real-time.
4️⃣ For Wikipedia queries, it fetches relevant information.
5️⃣ For general queries, it uses OpenAI's GPT to generate responses.
6️⃣ It can also **open Google, YouTube, and tell the current time.**

---
## 🛠️ Troubleshooting
**Issue:** WebSocket is not connecting properly.  
**Solution:** Ensure Flask-SocketIO is installed and run with `eventlet`:
```bash
pip install eventlet
python -m eventlet app.py
```

**Issue:** API key not found.  
**Solution:** Double-check the `.env` file and reload the environment variables.

---
## 📜 License
This project is open-source. Feel free to modify and improve it!

---
## ✨ Future Enhancements
- 🎤 **Better Speech Recognition**
- 🌍 **Multi-language Support**
- 🧠 **Memory for Contextual Conversations**
- 📱 **Mobile Compatibility**



