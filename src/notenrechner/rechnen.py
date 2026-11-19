# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Daniel J. Lauk

"""Die eigentliche Logik: Punkte -> Note. Kennt weder Kommandozeile noch Umgebung."""

import math


def berechne_note(punkte: float, maximum: float, rundung: float = 0.1) -> float:
    """Schweizer Notenskala: Note = Punkte / Maximum * 5 + 1.

    `rundung` ist die Schrittweite (z. B. 0.1 oder 0.5); es wird kaufmaennisch gerundet.
    """
    if maximum <= 0:
        raise ValueError("Das Maximum muss groesser als 0 sein.")
    if punkte < 0:
        raise ValueError("Die Punkte duerfen nicht negativ sein.")
    if punkte > maximum:
        raise ValueError(f"Punkte ({punkte:g}) uebersteigen das Maximum ({maximum:g}).")
    if rundung <= 0:
        raise ValueError("Die Rundung muss groesser als 0 sein.")

    note = punkte / maximum * 5 + 1
    gerundet = math.floor(note / rundung + 0.5) * rundung
    return round(gerundet, 2)
