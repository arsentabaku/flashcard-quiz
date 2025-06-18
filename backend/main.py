from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

flashcards = []

class Flashcard(BaseModel):
    question: str
    correct_answer: str
    wrong_answers: List[str]

@app.post("/flashcards")
def add_card(card: Flashcard):
    flashcards.append(card)
    return {"message": "Card added"}

@app.get("/quiz")
def get_quiz():
    shuffled = random.sample(flashcards, min(10, len(flashcards)))
    return shuffled
