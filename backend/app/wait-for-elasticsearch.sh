#!/bin/sh

set -e

echo "Waiting for Elasticsearch at $1..."

until curl -s "$1" >/dev/null; do
  sleep 2
done

echo "Elasticsearch is up!"
exec uvicorn main:app --host 0.0.0.0 --port 9567
