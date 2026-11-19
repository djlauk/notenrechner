# Benutzung

## Aufruf

```text
notenrechner PUNKTE [--max MAXIMUM] [--rundung SCHRITT]
```

- `PUNKTE`: erreichte Punkte
- `--max`: maximale Punktzahl (Standard: 50)
- `--rundung`: Rundungsschritt, z. B. `0.1` oder `0.5` (Standard: `0.1`)

Formel: **Note = Punkte / Maximum × 5 + 1**

## Konfiguration über die Umgebung

| Variable | Wirkung | Standard |
|----------|---------|----------|
| `NOTENRECHNER_RUNDUNG` | Rundungsschritt | `0.1` |

Die Option `--rundung` hat Vorrang vor der Umgebungsvariable.

## Exit-Codes

| Code | Bedeutung |
|------|-----------|
| 0 | Erfolg |
| 2 | Ungültige Eingabe |

Der Exit-Code ist die Antwort des Tools an alle, die es aufrufen – auch an GitHub Actions.
