#!/bin/bash

REPO="/home/batman/python code with harry"

cd "$REPO" || exit 1

echo "🚀 Auto-push started..."
echo "Watching: $REPO"
echo "Press Ctrl+C to stop."

while true
do
    inotifywait -r -e close_write,create,delete,move \
        --exclude '(^|/)\.git(/|$)' \
        "$REPO" >/dev/null 2>&1

    sleep 3

    if [[ -n "$(git status --porcelain)" ]]; then
        git add -A
        git commit -m "Update Python practice"
        git push
        echo "✅ Changes pushed to GitHub!"
    fi
done
