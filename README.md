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

## Live-Demo im Unterricht

1. Source code clonen oder herunterladen
2. venv einrichten: `pip install -e ".[dev]"` oder `uv sync --extras dev`
3. venv aktivieren: `.venv\Scripts\activate` (Windows Terminal) oder `. .venv/Scripts/activate` (bash)
4. Tests demonstrieren: `pytest`
5. Funktionsweise und Errolevel demonstrieren:
    - `notenrechner 42; echo $?` (bash)
    - `notenrechner 60 --max 50; echo $?` (bash)
6. workflow files ansehen: Name, Trigger, Jobs und Steps (runs und uses)
7. Repo auf GitHub einrichten
    - Neues Repo zu Demo-Zwecken anlegen
    - Settings → Pages → Build and Deployment → Source → GitHub Actions
8. Repo auf Git pushen → Actions ansehen
    - `git add origin <URL vom Repo> && git push`
    - Gehostete Website zeigen
9.  Fehler zeigen
    - `src/notenrechner/rechnen.py` Berechnungsformel kaputt machen (z. B. `+ 5` statt `+ 1` am Ende)
    - `pytest` lokal ausführen lassen
    - `git add src/notenrechner/rechnen.py && git commit -m 'demo: break calculation on purpose' && git push`
    - GitHub Action → wird rot → Issue angelegt → Link zum konkreten Lauf → Link zum commit und diff
10. Fehler beheben
    - `src/notenrechner/rechnen.py` Berechnungsformel kaputt machen (z. B. `+ 5` statt `+ 1` am Ende)
    - `pytest` lokal ausführen lassen
    - `git add src/notenrechner/rechnen.py && git commit`
    - Commit-Message im Editor eingeben (Issue-ID überprüfen)
      ```
      fix: calculation

      closes #1
      ```
    - `git push`
    - GitHub Action → wird grün → Issue grün → Link zum commit und diff
11. Release zeigen: `git tag v1.0.0; git push origin v1.0.0`

## Entstehung

Dieses Beispielprojekt wurde für eine Unterrichts-Session erstellt, mit Unterstützung
von KI (Claude von Anthropic, November 2026): Entwurf von Code, Tests, Workflows und
Dokumentation.

Inhaltlich geprüft und angepasst von Daniel J. Lauk.

## Lizenz

MIT-Lizenz, siehe [LICENSE](LICENSE). Copyright © 2026 Daniel J. Lauk
