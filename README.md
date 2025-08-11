# 🎙️ ElevenLabs Conversational AI Assistant

This project is a **Python voice assistant** built using the [ElevenLabs Conversational AI API](https://elevenlabs.io/) with real-time voice interaction.  
It uses environment-based configuration, a dynamic conversation setup, and custom callbacks to handle assistant and user responses.

---

## 📌 Features
- **Real-time voice interaction** with ElevenLabs' conversational AI.
- **Custom prompts** and first messages tailored to your needs.
- **Dynamic variables** (e.g., user's name, schedule).
- **Callback functions** for:
  - Assistant responses
  - Interrupted responses
  - User transcripts
- **Environment-based credentials** via `.env` file.

---

## 📂 Project Structure
.
├── main.py # Main script for running the assistant
├── .env # Environment variables (not tracked in Git)
└── va_notes.txt # how the program works

Make sure to install ElevenLabs library:
```
pip install elevenlabs elevenlabs[pyaudio] python-dotenv
```

🔑 Environment Variables
Create a .env file in the project root with your ElevenLabs credentials:
```
AGENT_ID=your_agent_id_here
API_KEY=your_api_key_here
```
You can get these from your ElevenLabs account dashboard.

🛠️ How It Works
Configuration Override
Custom prompt, first message, and dynamic variables are injected into ConversationConfig.

Monkey-Patching
Adds a user_id attribute to ConversationConfig dynamically.

Callbacks

print_agent_response → Prints AI responses.

print_interrupted_response → Handles interrupted messages.

print_user_transcript → Displays what the user said.

Session Start
Uses conversation.start_session() to begin a live session with your ElevenLabs agent.
