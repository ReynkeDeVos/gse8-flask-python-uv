# Flask-Deployment-Labor mit UV

Das Projekt enthält zwei kleine Programme:

- `main.py`: ein Kommandozeilenprogramm mit Typer
- `app.py`: eine Webanwendung mit Flask

UV übernimmt die virtuelle Umgebung und installiert die Pakete. Dafür braucht
das Projekt zwei Dateien:

- `pyproject.toml` enthält die direkten Abhängigkeiten.
- `uv.lock` hält die genauen Paketversionen fest.

Eine `requirements.txt` ist nicht mehr nötig.

## 1. UV installieren

Unter Linux oder macOS in Bash:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Öffne danach ein neues Terminal und prüfe die Installation:

```bash
uv --version
```

## 2. Projekt einrichten

Wechsle in das Projektverzeichnis:

```bash
cd cli-project-uv
```

Richte das Projekt ein:

```bash
uv sync
```

UV erstellt dabei den Ordner `.venv` und installiert alle Pakete. Du musst die
virtuelle Umgebung nicht selbst erstellen oder aktivieren.

## 3. Webanwendung starten

```bash
uv run flask --app app run --debug
```

Öffne anschließend <http://127.0.0.1:5000>.

Beende den Server mit `Strg+C`.

## 4. Tests und CLI ausprobieren

Tests starten:

```bash
uv run python -m unittest -v
```

Das Kommandozeilenprogramm starten:

```bash
uv run python main.py Ada Lovelace
```

## 5. Projekt auf GitHub hochladen

Liegt das Projekt bereits auf GitHub, kannst du diesen Abschnitt überspringen.

Initialisiere Git im Projektordner:

```bash
git init -b main
git add .
git commit -m "Stelle das Projekt auf UV um"
```

Erstelle auf GitHub ein leeres Repository. Füge danach dessen Adresse ein:

```bash
git remote add origin git@github.com:DEIN-NAME/DEIN-REPOSITORY.git
git push -u origin main
```

## 6. Auf Render deployen

Wähle im Render-Dashboard **New > Web Service** und verbinde das
GitHub-Repository.

Trage folgende Werte ein:

| Render-Feld | Wert |
| --- | --- |
| Name | `gse8-flask-python-uv` oder ein freier Name |
| Language | `Python 3` |
| Branch | `main` |
| Root Directory | leer lassen |
| Build Command | `uv sync` |
| Start Command | `uv run gunicorn app:app` |
| Instance Type | `Free` |
| Health Check Path | `/health` |

Du brauchst keine zusätzlichen Environment Variables. Render erkennt UV an
der Datei `uv.lock`. Die Datei `.python-version` legt Python 3.14 fest.

Klicke auf **Create Web Service**. Render baut und startet die Anwendung. Die
öffentliche Adresse endet auf `.onrender.com`.

## Alternative: Render Blueprint

Die Datei `render.yaml` enthält dieselben Einstellungen. Wähle auf Render
**New > Blueprint**, verbinde das Repository und klicke auf **Apply**.

## Später ein Paket hinzufügen

Zum Beispiel:

```bash
uv add requests
```

UV trägt das Paket in `pyproject.toml` ein und aktualisiert `uv.lock`.
