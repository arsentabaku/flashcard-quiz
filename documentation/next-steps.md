# Implemented Features & Upcoming Enhancements

## Implemented Features

* __Core Features__
    - [x] Add flashcards via form with question, one correct answer and three incorrect answers
    - [x] Store flashcards in SQLite using SQLAlchemy
    - [x] REST API (FastAPI) for:
        - Flashcard creation (`POST /flashcards`)
        - Quiz generation (`GET /quiz`)
    - [x] Randomized Question Quiz
    - [x] Track Score during quiz
    - [x] Result Page with final score
    - [x] Client-Side Routing using Svelte SPA Router
*  __Frontend & UX Enhancements__
    - [x] Quiz and result screens styled for readability
    - [x] UI feedback on submission and answer selection
    - [x] Score passed via URL hash (`#score=...`)
    - [x] Dynamically shows correct total number of questions on result screen
* __Backend & Persistence__
    - [x] SQLite-based local DB (`flashcards.db`)
    - [x] SQLAlchemy ORM for clean model definitions
    - [x] FastAPI CORS enabled for frontend-backend communication
    - [x] Endpoint to clear flashcards from database
- [x] Virtual environment setup for Python
* __Developer Experience__
    - [x] Clear folder structure: `frontend/` and `backend/`
    - [x] Full project setup guide (`README.md`)
    - [x] Git-friendly commits grouped by logical units
    - [x] Sample flashcard db payloads for testing

<br><br>
---
<br><br>

## Next Steps (if having more time)

### Flashcards & Learning
- [ ] Group flashcards into decks or topics
- [ ] Add edit/delete functionality for flashcards
- [ ] Add difficulty levels and adaptive learning logic

### Quiz & UX Enhancements
- [ ] Add progress bar and live score counter
- [ ] Show feedback after each answer
- [ ] Make it fully responsive
- [ ] Form validation for all flashcard inputs
- [ ] Error prevention for blank or invalid forms
- [ ] End-of-quiz review page: show correct vs incorrect answers

### User Management
- [ ] Add login/signup with session-based flashcard storage
- [ ] Track quiz history and performance over time

### Technical Roadmap
- [ ] Add unit & integration tests (Pytest, Playwright)
- [ ] Deploy frontend (Vercel) and backend (Render/Fly.io)
- [ ] Add Docker support and CI/CD with GitHub Actions
