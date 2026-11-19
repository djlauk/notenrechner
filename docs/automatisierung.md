# Automatisierung

Alle Workflows liegen in `.github/workflows/`. Jeder Step ist ein Kommandozeilen-Aufruf;
ob er grün oder rot wird, entscheidet allein der Exit-Code.

| Workflow | Auslöser | Zweck |
|----------|----------|-------|
| `test.yml` | Push, Pull Request | Tests ausführen, bei Fehler auf `main` ein Issue erstellen |
| `release.yml` | Tag `v*` | ZIP und Windows-EXE bauen, Release veröffentlichen |
| `docs.yml` | Push auf `main` | Diese Doku bauen und auf Pages veröffentlichen |
