#!/bin/bash

# Wechsle ins Projektverzeichnis (optional anpassen)
cd "$(dirname "$0")"

# Alle Änderungen hinzufügen
git add .

# Commit mit Zeitstempel
git commit -m "Update am $(date '+%Y-%m-%d %H:%M:%S')"

# Änderungen hochladen
git push origin main


