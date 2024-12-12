# Anleitung: Virtuelle Umgebung in Python

## 1. **VU erstellen**

1. Öffnen Sie ein Terminal
2. folgenden Befehl ausführen um eine VU zu erstellen:
   ```bash
   python -m venv venv
   ```
   _Dadurch wird ein Ordner `venv` im aktuellen Verzeichnis erstellt._

## 2. **VU aktivieren**

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

Nach der Aktivierung, sollte der Name in der Shell zu sehen sein -> `(venv)`.

## 3. **Abhängigkeiten installieren**

```bash
pip install -r requirements.txt
```

## 4. **Skript ausführen**

```bash
python md2html.py
```

## 5. **VU deaktivieren**

Um die VU zu verlassen:

```bash
deactivate
```
