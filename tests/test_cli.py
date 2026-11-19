# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Daniel J. Lauk

from notenrechner.cli import main


def test_erfolg_exit_code_0(capsys):
    assert main(["42", "--max", "50"]) == 0
    assert capsys.readouterr().out.strip() == "5.2"


def test_zu_viele_punkte_exit_code_2(capsys):
    assert main(["60", "--max", "50"]) == 2
    assert "uebersteigen" in capsys.readouterr().err


def test_rundung_aus_umgebungsvariable(monkeypatch, capsys):
    monkeypatch.setenv("NOTENRECHNER_RUNDUNG", "0.5")
    assert main(["42", "--max", "50"]) == 0
    assert capsys.readouterr().out.strip() == "5.0"


def test_option_schlaegt_umgebungsvariable(monkeypatch, capsys):
    monkeypatch.setenv("NOTENRECHNER_RUNDUNG", "0.5")
    assert main(["42", "--max", "50", "--rundung", "0.1"]) == 0
    assert capsys.readouterr().out.strip() == "5.2"


def test_ungueltige_umgebungsvariable_exit_code_2(monkeypatch):
    monkeypatch.setenv("NOTENRECHNER_RUNDUNG", "abc")
    assert main(["42"]) == 2
