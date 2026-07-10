#!/usr/bin/env bash
# Hammer the app homepage to probabilistically trigger errors (HTTP 500).
# Press Ctrl+C to stop.

URL="http://localhost:5000"
COUNT=${1:-100}

echo "Hitting ${URL} ${COUNT} times…"
for i in $(seq 1 $COUNT); do
  code=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
  echo "[$(date '+%H:%M:%S')] #$i -> HTTP $code"
  sleep 0.3
done
