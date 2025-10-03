#!/bin/bash

# Absolutes Projektverzeichnis anpassen
REPO_DIR="/home/arthur/Schreibtisch/VSC/Coding-Giants"

# Ins Projektverzeichnis wechseln
cd "$REPO_DIR" || { echo "Fehler: Repository-Verzeichnis nicht gefunden!"; exit 1; }

# Prüfen, ob Git-Repo vorhanden
if [ ! -d ".git" ]; then
    echo "Fehler: Kein Git-Repository hier!"
    exit 1
fi

# Aktuellen Branch erkennen
BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Prüfen, ob Änderungen vorhanden sind
if [ -z "$(git status --porcelain)" ]; then
    echo "Keine Änderungen vorhanden – nichts zu committen."
    exit 0
fi

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

# Commit erstellen
git commit -m "$COMMIT_NAME - ($(date '+%Y-%m-%d | %H:%M:%S'))"

# Push zum Remote
git push -u origin "$BRANCH"

echo "Alles erfolgreich gepusht auf '$BRANCH'."

