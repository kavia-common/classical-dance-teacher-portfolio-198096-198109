#!/usr/bin/env bash
set -euo pipefail

# Determine port (default 3010 if not provided)
PORT="${PORT:-3010}"
HOST="${HOST:-0.0.0.0}"

echo "[dance-portfolio-backend] Starting Flask server on ${HOST}:${PORT} ..."
echo "[dance-portfolio-backend] Environment:"
echo "  - PORT=${PORT}"
echo "  - HOST=${HOST}"

# Use Python run script which imports the Flask app and runs it.
# Ensure Python uses UTF-8
export PYTHONUNBUFFERED=1

python -m pip show flask >/dev/null 2>&1 || true

# Start the server
exec python run.py
