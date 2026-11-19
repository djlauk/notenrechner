# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Daniel J. Lauk

"""Kommandozeilen-Huelle: liest Argumente und Umgebung, gibt einen Exit-Code zurueck."""

import argparse
import os
import sys

from notenrechner.rechnen import berechne_note

ENV_RUNDUNG = "NOTENRECHNER_RUNDUNG"
EXIT_OK = 0
EXIT_EINGABEFEHLER = 2


def _formatiere(note: float) -> str:
    text = f"{note:.2f}"
    return text[:-1] if text.endswith("0") else text  # 5.50 -> 5.5, 6.00 -> 6.0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="notenrechner",
        description="Rechnet Punkte in eine Note (Skala 1-6) um.",
        epilog=f"Umgebungsvariable {ENV_RUNDUNG}: Standard fuer --rundung (z. B. 0.5).",
    )
    parser.add_argument("punkte", type=float, help="erreichte Punkte")
    parser.add_argument("--max", dest="maximum", type=float, default=50.0,
                        help="maximale Punktzahl (Standard: 50)")
    parser.add_argument("--rundung", type=float, default=None,
                        help=f"Rundungsschritt, z. B. 0.1 oder 0.5 (Standard: ${ENV_RUNDUNG} oder 0.1)")
    args = parser.parse_args(argv)  # bei ungueltiger Eingabe: Exit-Code 2

    rundung = args.rundung
    if rundung is None:
        try:
            rundung = float(os.environ.get(ENV_RUNDUNG, "0.1"))
        except ValueError:
            print(f"Fehler: {ENV_RUNDUNG} ist keine Zahl.", file=sys.stderr)
            return EXIT_EINGABEFEHLER

    try:
        note = berechne_note(args.punkte, args.maximum, rundung)
    except ValueError as fehler:
        print(f"Fehler: {fehler}", file=sys.stderr)
        return EXIT_EINGABEFEHLER

    print(_formatiere(note))
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
