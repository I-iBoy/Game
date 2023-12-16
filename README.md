# Winter Game 

Winter Game ist ein einfaches Pygame-basiertes Spiel, das einen winterlichen Level darstellt. Der Code ist aufgeteilt in verschiedene Module und Klassen, um die Struktur und Lesbarkeit zu verbessern.

## Inhaltsverzeichnis

1. [Allgemeine Informationen](https://chat.openai.com/c/f2111107-fd8a-498f-8735-58d4c02a251d#allgemeine-informationen)
2. [Installation](https://chat.openai.com/c/f2111107-fd8a-498f-8735-58d4c02a251d#installation)
3. [Anwendung](https://chat.openai.com/c/f2111107-fd8a-498f-8735-58d4c02a251d#anwendung)
4. [Anpassung](https://chat.openai.com/c/f2111107-fd8a-498f-8735-58d4c02a251d#anpassung)
5. [Spieler-Klasse](https://chat.openai.com/c/f2111107-fd8a-498f-8735-58d4c02a251d#spieler-klasse)
6. [Tile-Klassen](https://chat.openai.com/c/f2111107-fd8a-498f-8735-58d4c02a251d#tile-klassen)
7. [Hilfsfunktionen](https://chat.openai.com/c/f2111107-fd8a-498f-8735-58d4c02a251d#hilfsfunktionen)
8. [Test-Level](https://chat.openai.com/c/f2111107-fd8a-498f-8735-58d4c02a251d#test-level)

## Allgemeine Informationen

Das Winter Game ist ein Pygame-Projekt, das einen Spieler durch eine winterliche Umgebung steuern lässt. Der Code ist in mehrere Dateien aufgeteilt, die verschiedene Aspekte des Spiels behandeln, wie den Spieler, Level-Fliesen, Animationen und mehr.

## Installation

1. Installiere Python von [python.org](https://www.python.org/).
2. Installiere Pygame mit dem Befehl: `pip install pygame`.

## Anwendung

Führe die `main.py`-Datei aus, um das Spiel zu starten. Verlasse das Spiel durch Drücken der Escape-Taste oder des Schließen-Knopfs des Fensters.

## Anpassung

* Die Spiel-Einstellungen befinden sich in der Datei `setting.py`.
* Das Level kann in der `main.py`-Datei in der Variable `level_map` angepasst werden.

## Spieler-Klasse

Die `Player`-Klasse repräsentiert den Spieler im Winter Game. Sie bietet Funktionen für die Steuerung des Spielers, die Anwendung der Schwerkraft und die Aktualisierung der Spielerposition.

### Steuerung

* **Rechts** : Pfeiltaste rechts oder `D`
* **Links** : Pfeiltaste links oder `A`
* **Sprung** : Leertaste, `W` oder Pfeiltaste nach oben (nur wenn der Spieler auf dem Boden steht)

## Tile-Klassen

Die `Tile`-Klassen repräsentieren Bodenfliesen im Spiel. Es gibt eine einfache `Tile`-Klasse und eine erweiterte `AnimatedTile`-Klasse, die animierte Fliesen ermöglicht. Die `Coin`-Klasse erbt von `AnimatedTile` und repräsentiert Münzen.

## Hilfsfunktionen

Es gibt mehrere Hilfsfunktionen, darunter `import_folder`, `import_csv_layout` und `import_cut_graphics`, die das Importieren von Bildern, Levelinformationen und Grafiken erleichtern.

## Test-Level

Das Test-Level ist eine Beispiel-Levelkarte, die im Spiel verwendet wird. Du kannst es nach Belieben anpassen, um verschiedene Herausforderungen und Strukturen für dein Spiel zu erstellen. Die allgemeinen Einstellungen für das Level und das Spiel sind ebenfalls in der `setting.py`-Datei festgelegt.
