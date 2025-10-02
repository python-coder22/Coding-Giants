#!/bin/bash

# Absolutes Projektverzeichnis anpassen
REPO_DIR="/home/arthur/Schreibtisch/VSC/Coding Giants"

# Ins Projektverzeichnis wechseln
cd "$REPO_DIR" || { echo "Fehler: Repository-Verzeichnis nicht gefunden!"; exit 1; }

# Prüfen, ob Git-Repo vorhanden
if [ ! -d ".git" ]; then
    echo "Fehler: Kein Git-Repository hier!"
    exit 1
fi

# Aktuellen Branch erkennen
BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Zeige die Dateien, die geändert wurden
echo "Folgende Dateien werden zum Commit hinzugefügt:"
git status -s

# Alle Änderungen hinzufügen
git add -A

# Commit-Nachricht abfragen
read -p "Gib den Commit-Namen ein (oder Enter für automatischen Commit): " COMMIT_NAME

# Standard-Commit-Nachricht, falls leer
if [ -z "$COMMIT_NAME" ]; then
    COMMIT_NAME="Automatischer Commit"
fi

# Commit erstellen, auch wenn keine Änderungen vorhanden
git commit --allow-empty -m "$(date '+%Y-%m-%d %H:%M:%S') - $COMMIT_NAME"

# Push zum Remote
git push -u origin "$BRANCH"

echo "Alles erfolgreich gepusht auf '$BRANCH'."

