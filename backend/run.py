import os
from app import app

def _int(val, default):
    try:
        return int(val)
    except Exception:
        return default

# PUBLIC_INTERFACE
def run():
    """Start the Flask app bound to HOST:PORT from env (defaults 0.0.0.0:3010)."""
    host = os.getenv("HOST", "0.0.0.0")
    port = _int(os.getenv("PORT", "3010"), 3010)
    print(f"[dance-portfolio-backend] Flask app starting on http://{host}:{port}")
    print("[dance-portfolio-backend] Health: GET /")
    print("[dance-portfolio-backend] Gallery: GET /api/gallery/")
    app.run(host=host, port=port)

if __name__ == "__main__":
    run()
