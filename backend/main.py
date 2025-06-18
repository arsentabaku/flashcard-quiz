from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import random

app = FastAPI()

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
