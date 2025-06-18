from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Flashcard(Base):
    __tablename__ = 'flashcards'

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    correct_answer = Column(String, nullable=False)
    wrong_1 = Column(String, nullable=False)
    wrong_2 = Column(String, nullable=False)
    wrong_3 = Column(String, nullable=False)

# Database setup
engine = create_engine("sqlite:///./flashcards.db")
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
