#!/usr/bin/env sh
# Start the API and Vite development servers in a reusable tmux session.

set -eu

session_name="seadots-concept-editor"
app_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)

if ! command -v tmux >/dev/null 2>&1; then
  echo "tmux is required. Install it first (for example: brew install tmux)." >&2
  exit 1
fi

if ! tmux has-session -t "$session_name" 2>/dev/null; then
  tmux new-session -d -s "$session_name" -c "$app_dir" "npm run dev:server"
  tmux split-window -h -t "$session_name":0 -c "$app_dir" "npm run dev"
  tmux select-layout -t "$session_name":0 even-horizontal
  tmux select-pane -t "$session_name":0.0
fi

exec tmux attach-session -t "$session_name"
