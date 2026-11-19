# notenrechner

Kleines Python-CLI-Tool als Demo-Projekt für die Input-Session **GitHub Actions & GitHub Pages**.
Es rechnet Punkte in eine Note der Schweizer Skala (1–6) um.

```text
> notenrechner 42 --max 50
5.2
```

## Lokal ausprobieren

```text
python -m venv .venv          # Python venv erstellen in Verzeichnis .venv
.venv\Scripts\activate        # (Windows)   bzw.   source .venv/bin/activate   (Linux/macOS)
pip install -e ".[dev]"       # Tool und Test-Abhängigkeiten installieren
notenrechner 42               # Tool ausführen
pytest                        # Tests ausführen
```

Oder mit [uv](https://docs.astral.sh/uv/):

```text
uv sync --extra dev           # Python venv erstellen in Verzeichnis .venv und Tools installieren
.venv\Scripts\activate        # (Windows)   bzw.   source .venv/bin/activate   (Linux/macOS)
notenrechner 42               # Tool ausführen
pytest                        # Tests ausführen
```

## Exit-Codes

| Code | Bedeutung |
|------|-----------|
| 0 | Erfolg |
| 2 | Ungültige Eingabe (z. B. mehr Punkte als Maximum) |

## Konfiguration

Die Umgebungsvariable `NOTENRECHNER_RUNDUNG` setzt die Rundung (Standard `0.1`), z. B. `0.5` für halbe Noten.
Die Option `--rundung` hat Vorrang.

## Automatisierung (`.github/workflows/`)

| Datei | Auslöser | Was passiert |
|-------|----------|--------------|
| `test.yml` | Push, Pull Request | `pytest` ausführen; bei Fehler auf `main` automatisch ein Issue erstellen |
| `release.yml` | Tag `v*` | Tests, ZIP bauen, Windows-EXE bauen (PyInstaller), GitHub-Release erstellen |
| `docs.yml` | Push auf `main` (Docs) | Doku mit MkDocs bauen und auf GitHub Pages veröffentlichen |

**Einmalig nötig:** Settings → Pages → Source: *GitHub Actions*.

## Entstehung

Dieses Beispielprojekt wurde für eine Unterrichts-Session erstellt, mit Unterstützung
von KI (Claude von Anthropic, November 2026): Entwurf von Code, Tests, Workflows und
Dokumentation. 

## Lizenz

MIT-Lizenz, siehe [LICENSE](LICENSE). © 2026 Daniel J. Lauk
