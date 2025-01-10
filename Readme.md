- [Intro](#orgf57d020)
- [🚀 Willkommen zurück in der Welt von Python! 🐍](#orgbcf1e4d)
  - [📚 1. Grundlagen-Auffrischung](#org438acc2)
  - [🧠 2. Übungen zur Auffrischung](#org99f30a7)
- [Mein Plan](#org9035fd4)
- [Emacs und Environment Setup](#orgac1cf50)
  - [Template Org File](#org210247a)
  - [Git](#org37ad1cc)




<a id="orgf57d020"></a>

# Intro

Nach einiger Zeit weg von Python, möchte ich nun Django lernen, habe aber das Gefühl, das mir die Grundlagen etwas abhanden gekommen sind. Also hab ich gemacht was alle machen, ich hab Chat GPT gefragt. Wonach, Nach übungen. Im folgenden die Antwort von ChatGPT:


<a id="orgbcf1e4d"></a>

# 🚀 Willkommen zurück in der Welt von Python! 🐍

Zwei Monate Pause sind kein Problem – das Programmieren ist wie Fahrradfahren. Lass uns Schritt für Schritt dein Wissen auffrischen und dich wieder in Schwung bringen.


<a id="org438acc2"></a>

## 📚 1. Grundlagen-Auffrischung

Wir starten mit den wichtigsten Konzepten:

-   Variablen und Datentypen
-   Kontrollstrukturen (if-else, for, while)
-   Funktionen
-   Listen, Dictionaries, Tupel, Mengen
-   Dateioperationen (lesen/schreiben)
-   Fehlerbehandlung (try-except)


<a id="org99f30a7"></a>

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


<a id="org9035fd4"></a>

# Mein Plan

Das klang für den Anfang ganz gut, also machen wir das so. Ich löse die vorgeschlagenen aufgaben der Reihe nach und bediene mich an W3Shool Resourcen wenn ich was nicht weiß oder unsicher bin. Verwenden werde ich dafür Emacs und ich schreibe den code in Org-Dateien, die ich dann in Python Files umwandeln lasse. So gewöhne ich mich an Org und hab nachher eine Saubere Dokumentation.

Sowohl die Org Dateien als auch den reinen Quellcode lade ich hier Hoch. und mehr übungen folgen wenn ich deke das ich noch was brauche.


<a id="orgac1cf50"></a>

# Emacs und Environment Setup


<a id="org210247a"></a>

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


<a id="org37ad1cc"></a>

## Git

Dieses Git repo wurde mit von Github erstellt und dann per **SSH** auf gecloned, da Gitub den support für https Authentifizierung eingestellt hat.

Ich habe des weiteren eine .gitignore Datei erstellt mit dem folgenden Inhalt

```.gitignore
*.org~
```

das sorgt dafür das die von Emacs erstellten Backups von git Ignioriert werden, auch diese Datei wird wie benötigt erweitert
