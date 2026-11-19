# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Daniel J. Lauk

import pytest

from notenrechner.rechnen import berechne_note


def test_volle_punktzahl_ist_6():
    assert berechne_note(50, 50) == 6.0


def test_null_punkte_ist_1():
    assert berechne_note(0, 50) == 1.0


def test_normalfall():
    assert berechne_note(42, 50) == 5.2


def test_halbe_noten():
    assert berechne_note(42, 50, rundung=0.5) == 5.0
    assert berechne_note(45, 50, rundung=0.5) == 5.5


def test_aufrunden_bei_genau_halb():
    # 5.25 liegt genau zwischen 5.0 und 5.5 -> kaufmaennisch aufrunden
    assert berechne_note(42.5, 50, rundung=0.5) == 5.5


@pytest.mark.parametrize("punkte, maximum", [(60, 50), (-1, 50), (10, 0)])
def test_ungueltige_eingaben(punkte, maximum):
    with pytest.raises(ValueError):
        berechne_note(punkte, maximum)
