# Persona AI Assistant

> AI chatbot with personality, voice interaction, and custom UI built using FastAPI and a local LLM.

---

## Features

- Conversational AI chatbot with memory
- Personalized AI personality (Deepti)
- Clean and interactive chat UI
- Sidebar with chat controls
- Download chat as text file
- Typing animation for better UX
- Female voice playback option
- Error handling for smooth experience

---

##  Tech Stack

- Backend: FastAPI (Python)
- Frontend: HTML, CSS, JavaScript
- AI Model: Local LLM (Ollama - Phi)
- API Communication: REST API

---

##  How It Works

1. User sends a message from the frontend
2. Backend processes it using a custom personality prompt
3. AI generates a response using a local LLM
4. Response is displayed in the UI
5. Optional voice playback is available

---

##  How to Run Locally

### 1. Install dependencies
```bash
pip install fastapi uvicorn requests

### 2. Install and start Ollama (IMPORTANT)

Make sure Ollama is installed on your system.

3.Run the AI model:
ollama run phi
4.

cd backend
uvicorn main:app --reload
5.
cd frontend
python -m http.server 5500

6.website working
http://127.0.0.1:5500/index.html














































