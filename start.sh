#!/usr/bin/env bash
set -e

ROOT="$(cd "$(dirname "$0")" && pwd)"

if [ ! -f "$ROOT/backend/.env" ]; then
  echo "ERROR: backend/.env not found. Create it with your ANTHROPIC_API_KEY."
  exit 1
fi

cleanup() {
  echo ""
  echo "Stopping servers..."
  kill 0
}
trap cleanup EXIT INT TERM

echo "Starting backend on http://localhost:8000 ..."
(cd "$ROOT/backend" && ./venv/bin/uvicorn main:app --port 8000) &

echo "Starting frontend on http://localhost:3000 (and your LAN IP) ..."
(cd "$ROOT/frontend" && npm run dev -- -H 0.0.0.0) &

IP="$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo localhost)"
echo ""
echo "================================================"
echo "  Local:    http://localhost:3000"
echo "  Network:  http://$IP:3000  (share with team)"
echo "  Stop:     Ctrl+C"
echo "================================================"

wait
