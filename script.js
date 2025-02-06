const socket = io.connect("http://localhost:5000");

// Send message to server
function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value;
    if (message.trim()) {
        addMessage(`You: ${message}`);
        socket.emit("user_message", { message });
        input.value = ""; // Clear input field
    }
}

// Add message to chat box
function addMessage(message) {
    const messagesDiv = document.getElementById("messages");
    const newMessage = document.createElement("div");
    newMessage.textContent = message;
    messagesDiv.appendChild(newMessage);
    messagesDiv.scrollTop = messagesDiv.scrollHeight; // Auto-scroll
}

// Receive response from server
socket.on("server_message", (data) => {
    const assistantMessage = `Assistant: ${data.message}`;
    addMessage(assistantMessage);
    speakText(data.message);
});

// Convert text-to-speech
function speakText(message) {
    const speech = new SpeechSynthesisUtterance(message);
    speech.lang = "en-US";
    window.speechSynthesis.speak(speech);
}

// Speech-to-text (Web Speech API)
function startVoiceInput() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";
    recognition.onstart = () => console.log("Listening...");
    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        document.getElementById("user-input").value = transcript; // Autofill input field
        sendMessage();
    };
    recognition.onerror = (event) => console.error("Speech recognition error", event);
    recognition.start();
}
