from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import random

from models import Flashcard as DBFlashcard, SessionLocal, init_db

init_db()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Flashcard(BaseModel):
    question: str
    correct_answer: str
    wrong_answers: List[str]

@app.post("/flashcards")
def add_card(card: Flashcard, db: Session = Depends(get_db)):
    db_card = DBFlashcard(
        question=card.question,
        correct_answer=card.correct_answer,
        wrong_1=card.wrong_answers[0],
        wrong_2=card.wrong_answers[1],
        wrong_3=card.wrong_answers[2]
    )
    db.add(db_card)
    db.commit()
    return {"message": "Card added"}

@app.get("/quiz")
def get_quiz(db: Session = Depends(get_db)):
    cards = db.query(DBFlashcard).all()
    selected = random.sample(cards, min(10, len(cards)))
    return [
        {
            "question": c.question,
            "correct_answer": c.correct_answer,
            "wrong_answers": [c.wrong_1, c.wrong_2, c.wrong_3]
        }
        for c in selected
    ]
