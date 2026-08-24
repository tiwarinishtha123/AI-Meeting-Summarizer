from fastapi import FastAPI, UploadFile, File
from google.colab import userdata
from google import genai
import whisper
import os


# =========================
# Gemini Configuration
# =========================

api_key = userdata.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


# =========================
# Whisper Configuration
# =========================

model = whisper.load_model("base")


# =========================
# FastAPI Application
# =========================

app = FastAPI(
    title="AI Meeting Summarizer",
    description="API for transcribing meeting audio and generating structured meeting summaries.",
    version="1.0.0"
)


# =========================
# Home Endpoint
# =========================

@app.get("/")
def home():
    return {
        "message": "AI Meeting Summarizer Backend is running!"
    }


# =========================
# Health Check
# =========================

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# =========================
# Gemini Summary Function
# =========================

def generate_summary(transcript):

    prompt = f"""
You are a professional meeting assistant.

Analyze this meeting transcript and provide:

1. Meeting Summary
2. Key Discussion Points
3. Decisions Made
4. Action Items
5. Important Deadlines

Make the output clear, concise, and well structured.

Transcript:
{transcript}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


# =========================
# Audio Upload Endpoint
# =========================

@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):

    audio_path = "/content/" + file.filename

    # Save uploaded audio
    with open(audio_path, "wb") as f:
        f.write(await file.read())

    # Transcribe audio using Whisper
    result = model.transcribe(audio_path)

    transcript = result["text"]

    # Generate summary using Gemini
    summary = generate_summary(transcript)

    # Return result
    return {
        "filename": file.filename,
        "transcript": transcript,
        "summary": summary
    }
