import os
from app import app

def _int(val, default):
    try:
        return int(val)
    except Exception:
        return default

if __name__ == "__main__":
    # Determine host and port from environment, with sensible defaults
    host = os.getenv("HOST", "0.0.0.0")
    port = _int(os.getenv("PORT", "3010"), 3010)

    # Log startup details
    print(f"[dance-portfolio-backend] Flask app starting on http://{host}:{port}")
    print("[dance-portfolio-backend] Health: GET /")
    print("[dance-portfolio-backend] Gallery: GET /api/gallery/")

    # Run app
    app.run(host=host, port=port)
