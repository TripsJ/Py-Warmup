- [Intro](#orga0362ce)
- [🚀 Willkommen zurück in der Welt von Python! 🐍](#org81447fd)
  - [📚 1. Grundlagen-Auffrischung](#org6f9b586)
  - [🧠 2. Übungen zur Auffrischung](#orgc5093a4)
- [Mein Plan](#orgcad185c)
- [Emacs und Environment Setup](#org2a7bd39)
  - [Template Org File](#orgbbc4ec9)
  - [Git](#orga63069f)




<a id="orga0362ce"></a>

# Intro

Nach einiger Zeit weg von Python, möchte ich nun Django lernen, habe aber das Gefühl, das mir die Grundlagen etwas abhanden gekommen sind. Also hab ich gemacht was alle machen, ich hab Chat GPT gefragt. Wonach, Nach übungen. Im folgenden die Antwort von ChatGPT:


<a id="org81447fd"></a>

# 🚀 Willkommen zurück in der Welt von Python! 🐍

Zwei Monate Pause sind kein Problem – das Programmieren ist wie Fahrradfahren. Lass uns Schritt für Schritt dein Wissen auffrischen und dich wieder in Schwung bringen.


<a id="org6f9b586"></a>

## 📚 1. Grundlagen-Auffrischung

Wir starten mit den wichtigsten Konzepten:

-   Variablen und Datentypen
-   Kontrollstrukturen (if-else, for, while)
-   Funktionen
-   Listen, Dictionaries, Tupel, Mengen
-   Dateioperationen (lesen/schreiben)
-   Fehlerbehandlung (try-except)


<a id="orgc5093a4"></a>

## 🧠 2. Übungen zur Auffrischung


### Übung 1: Zahlenraten-Spiel

Ziel: Programmiere ein kleines Zahlenraten-Spiel.

-   Das Programm wählt eine zufällige Zahl zwischen 1 und 100.
-   Der Nutzer muss raten.
-   Das Programm gibt Hinweise (zu hoch/zu niedrig).
-   Bonus: Zähle die Versuche und gib das Ergebnis aus.


### Übung 2: Textanalyse

Ziel: Analysiere eine Zeichenkette.

-   Frage den Nutzer nach einem Text.
-   Zähle Wörter, Zeichen und die Häufigkeit jedes Buchstabens.
-   Gib das Ergebnis aus.


### Übung 3: To-Do-Liste

Ziel: Erstelle ein einfaches To-Do-Listen-Programm.

-   Nutzer kann Aufgaben hinzufügen, entfernen und anzeigen lassen.
-   Speichere die Liste in einer Textdatei.


<a id="orgcad185c"></a>

# Mein Plan

Das klang für den Anfang ganz gut, also machen wir das so. Ich löse die vorgeschlagenen aufgaben der Reihe nach und bediene mich an W3Shool Resourcen wenn ich was nicht weiß oder unsicher bin. Verwenden werde ich dafür Emacs und ich schreibe den code in Org-Dateien, die ich dann in Python Files umwandeln lasse. So gewöhne ich mich an Org und hab nachher eine Saubere Dokumentation.

Sowohl die Org Dateien als auch den reinen Quellcode lade ich hier Hoch. und mehr übungen folgen wenn ich deke das ich noch was brauche.


<a id="org2a7bd39"></a>

# Emacs und Environment Setup


<a id="orgbbc4ec9"></a>

## Template Org File

Ich habe für den Anfang eine Org Datei erstellt mit einer reihe an Property Definitionen die als Template genutzt wird. Diese definitionen wurden gesetzt:

```
:PROPERTIES:
#+TITLE: Insert Title
#+AUTHOR: J. Trips
#+DATE: <2025-01-09 jeu>
#+LANGUAGE: en
#+EXPORT_FILE_NAME: target_file_name
#+DESCRIPTION: Description
#+STARTUP: show2levels
#+OPTIONS: toc:2
:END:

```

der Zweck dieser Datei ist nur das ich die Properties nicht vergesse, Die Inhalte werden dann geändert oder entfernt wie nötig. Zusätzlich lassen sich noch standard Argumente für code blöcke setzen, wie zum Beispiel:

```
#+PROPERTY: header-args: python -n


```

was alle Code Blöcke auf Python code einstellt und durchnummeriert.


<a id="orga63069f"></a>

## Git

Dieses Git repo wurde mit von Github erstellt und dann per **SSH** auf gecloned, da Gitub den support für https Authentifizierung eingestellt hat.

Ich habe des weiteren eine .gitignore Datei erstellt mit dem folgenden Inhalt

```.gitignore
*.org~
```

das sorgt dafür das die von Emacs erstellten Backups von git Ignioriert werden, auch diese Datei wird wie benötigt erweitert
