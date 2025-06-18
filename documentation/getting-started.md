# Getting Started

> **Requirements:**  
> - Python 3.10+  
> - Node.js 18+  
> - npm (comes with Node.js)

**Flashcard** is a full-stack flashcard quiz app powered by FastAPI and Svelte. This guide walks you through setting up the app locally on your machine.

---

## Backend Setup – FastAPI + SQLite

```bash
# 1. Navigate to the backend folder
cd backend

# 2. Create a virtual environment
python3 -m venv venv

# 3. Activate the virtual environment
source venv/bin/activate

# 4. Install backend dependencies
pip install fastapi uvicorn sqlalchemy

# 5. Start the FastAPI server
uvicorn main:app --reload
```


## Frontend Setup – Svelte + Tailwind CSS

```bash
# 1. Navigate to the frontend app folder
cd frontend/flashcard-frontend

# 2. Install frontend dependencies
npm install

# 3. Start the development server
npm run dev
```