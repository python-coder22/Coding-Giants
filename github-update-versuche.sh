#!/bin/bash

# Absolutes Projektverzeichnis anpassen
REPO_DIR="/home/arthur/Schreibtisch/VSC/Coding Giants"

cd "$REPO_DIR" || { echo "Fehler: Repository-Verzeichnis nicht gefunden!"; exit 1; }

# Prüfen, ob Git-Repo vorhanden
if [ ! -d ".git" ]; then
    echo "Fehler: Kein Git-Repository hier!"
    exit 1
fi

# Aktuellen Branch erkennen
BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Änderungen von GitHub holen
git pull --rebase origin "$BRANCH"

# Alle Änderungen hinzufügen
git add .

# Prüfen, ob es Änderungen gibt
if git diff --cached --quiet; then
    echo "Keine Änderungen zum Commit."
    exit 0
fi

# Commit-Nachricht abfragen
read -p "Gib den Commit-Namen ein (oder Enter für automatischen Commit): " COMMIT_NAME

# Standard-Commit-Nachricht, falls leer
if [ -z "$COMMIT_NAME" ]; then
    COMMIT_NAME="Automatischer Commit"
fi

# Commit mit Datum und Uhrzeit
git commit -m "$COMMIT_NAME - $(date '+%Y-%m-%d %H:%M:%S')"

# Push zum Remote
git push -u origin "$BRANCH"

echo "✅ Änderungen erfolgreich gepusht auf '$BRANCH'."

