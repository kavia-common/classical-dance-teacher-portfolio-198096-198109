# Dance Portfolio Backend (Flask)

This is the backend API for the Classical Dance Teacher Portfolio. It is a Flask app exposing health and gallery endpoints with OpenAPI docs via flask-smorest.

## Quick start

1. Create and activate a virtual environment:
   python3 -m venv .venv
   source .venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Start the server (defaults to 0.0.0.0:3010):
   ./start.sh
   # or
   HOST=0.0.0.0 PORT=3010 python backend/run.py

4. Verify:
   - Health:      GET http://localhost:3010/
   - Gallery:     GET http://localhost:3010/api/gallery/
   - Swagger UI:  GET http://localhost:3010/docs/

## Configuration

Environment variables:
- PORT: Port to bind (default 3010)
- HOST: Host IP to bind (default 0.0.0.0)
