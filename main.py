from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests

from personality import build_prompt

app = FastAPI()

API_URL = "http://localhost:11434/api/generate"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

chat_history = []

@app.get("/")
def home():
    return {"message": "AI Personality Clone Running"}


@app.post("/chat")
def chat(req: ChatRequest):
    try:
        user_msg = req.message.strip().lower()

        # ✅ SMART FIXES (important)
        if user_msg in ["hi", "hello"]:
            return {"response": "Hey, how are you?"}

        if user_msg in ["bye", "goodbye"]:
            return {"response": "Goodbye, have a great day."}

        if user_msg in ["thanks", "thank you"]:
            return {"response": "You're welcome."}

        if "who are you" in user_msg:
            return {"response": "I'm Deepti, a computer science student who enjoys AI and coding."}

        if "remember" in user_msg:
            if chat_history:
                return {"response": f"You said: {chat_history[-1]}"}
            else:
                return {"response": "I don’t have anything to remember yet."}

        # Store user message
        chat_history.append(user_msg)

        # Keep last 5 messages
        context = "\n".join(chat_history[-5:])

        prompt = build_prompt(context)

        response = requests.post(API_URL, json={
            "model": "phi",
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": 80,
                "temperature": 0.6
            }
        })

        data = response.json()
        raw_reply = data.get("response", "").strip()

        # Clean output
        reply = raw_reply

        for tag in ["Deepti:", "AI:", "Assistant:"]:
            if tag in reply:
                reply = reply.split(tag)[-1].strip()

        if "." in reply:
            reply = reply.split(".")[0].strip() + "."

        chat_history.append(reply)

    except Exception as e:
        print("ERROR:", e)
        reply = "Something went wrong."

    return {"response": reply}