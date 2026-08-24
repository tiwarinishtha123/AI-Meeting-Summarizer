# AI-Meeting-Summarizer
AI-powered meeting summarizer using Whisper, FastAPI, and Google Gemini.

## 📌 Overview
What the project does and why you built it.

## 🎯 Objective
The problem you're solving.

## ✨ Features
- Audio upload
- Speech-to-text transcription
- AI meeting summary
- Key discussion points
- Decisions made
- Action items
- Deadlines

## 🛠️ Tech Stack
- Python
- FastAPI
- OpenAI Whisper
- Google Gemini
- Google Colab

## 🏗️ System Architecture
Audio → Whisper → Transcript → Gemini → Structured Summary

## ⚙️ How It Works
The AI Meeting Summarizer processes a meeting audio file through a speech-to-text and AI summarization pipeline.

1. **Audio Upload**  
   The user uploads a meeting audio file through the FastAPI `/upload-audio` endpoint.

2. **Speech-to-Text Transcription**  
   The uploaded audio is processed using **OpenAI Whisper**, which converts the spoken conversation into a text transcript.

3. **Transcript Processing**  
   The generated transcript is passed to the Google Gemini model for analysis.

4. **AI Summarization**  
   Google Gemini analyzes the transcript and generates a structured meeting summary.

5. **Information Extraction**  
   The system identifies and organizes:
   - Meeting Summary
   - Key Discussion Points
   - Decisions Made
   - Action Items
   - Important Deadlines

6. **API Response**  
   FastAPI returns the filename, complete transcript, and generated summary as a structured JSON response.

## 🚀 Setup & Installation
1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Meeting-Summarizer.git
cd AI-Meeting-Summarizer
pip install -r requirements.txt
set GEMINI_API_KEY=your_api_key
For Windows, install FFmpeg and add it to the system PATH
Start the FastAPI server using:

uvicorn app:app --host 0.0.0.0 --port 8000
The application will run at:

http://localhost:8000
Open the following URL in a browser:

http://localhost:8000/docs


## 🔌 API Endpoints
GET /
GET /health
POST /upload-audio


## 🔮 Future Enhancements
Future improvements include developing a web-based interface for easier audio upload and result visualization, adding speaker identification to distinguish between meeting participants, improving action-item extraction by identifying assignees and priorities, supporting real-time and multilingual transcription, and enabling meeting history, downloadable reports, calendar integration, and cloud deployment for easier access and scalability.

## 👩‍💻 Author
Nishtha Tiwari / tiwarinishtha123
