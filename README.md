# classical-dance-teacher-portfolio-198096-198109

## Backend (Flask)

Run locally:
1. Create venv and install requirements
   - python3 -m venv .venv && source .venv/bin/activate
   - pip install -r backend/requirements.txt
2. Start server
   - export FLASK_APP=backend/run.py
   - python backend/run.py
   - Server defaults to http://127.0.0.1:5000

OpenAPI/Docs:
- Swagger UI: http://localhost:5000/docs/
- Health: GET http://localhost:5000/
- Gallery: GET http://localhost:5000/api/gallery/

## Frontend (React)

- Copy frontend/.env.example to frontend/.env and set REACT_APP_API_BASE to point to the backend origin (e.g., http://localhost:5000).
- Start: cd frontend && npm install && npm start
- Navigate to Gallery via the top-left nav to verify the API.