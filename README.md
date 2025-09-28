# Urlaubsantrags-Tool – Übersicht & technische Umsetzung
##1. Use-Case:##
Das Urlaubsantrags-Tool ermöglicht es, Urlaubsanträge in einer CSV-Datei zu verwalten, Konflikte zwischen Urlaubszeiten zu prüfen und neue Anträge hinzuzufügen. Es bietet eine einfache Möglichkeit zur Verwaltung von Urlaubsanträgen für kleine Teams und Unternehmen und hilft dabei, Überschneidungen von genehmigten Urlaubsanträgen zu erkennen.

##2. Technologien und Tools:##

•	Python 3.x: Die Hauptprogrammiersprache für die Erstellung des Tools.

•	pandas: Für die Datenmanipulation und -verarbeitung, insbesondere das Laden, Bearbeiten und Speichern der CSV-Datei.

•	datetime: Zur Arbeit mit Datumswerten und deren Validierung.

##3. Installation und Setup:##

Voraussetzungen:

•	Python 3.x muss installiert sein.
[Python herunterladen](https://www.python.org/downloads/)

•	Die folgenden Python-Pakete müssen installiert werden:

o	pandas

Installation:
1.	Die folgenden Python-Pakete müssen installiert werden:

o	Pandas

2.	Lade das Projekt herunter und speichere die Datei urlaub.csv im selben Ordner wie das Skript.

3.	Führe das Skript aus:

python main.py

##4. Verwendung:##

Neue Urlaubsanträge hinzufügen:

1.	Starte das Skript.

2.	Das Tool fragt dich, ob du einen neuen Urlaubsantrag hinzufügen möchtest.

3.	Gib die folgenden Informationen ein:

o	Name des Mitarbeiters

o	Start- und Enddatum des Urlaubs (im Format YYYY-MM-DD)

o	Status des Antrags (offen/genehmigt/abgelehnt)

Konfliktprüfung:

•	Das Tool prüft automatisch, ob es Überschneidungen mit bestehenden genehmigten Urlaubsanträgen gibt. Falls Konflikte erkannt werden, wird eine Warnung angezeigt.

##5. Funktionsweise:##

•	CSV Laden:

Das Skript lädt eine CSV-Datei mit den Spalten: Name, Startdatum, Enddatum, Status. Falls die Datei nicht existiert, wird sie automatisch erstellt.

 ![grafik](https://github.com/user-attachments/assets/4596ef44-fe3d-4241-9936-8a12ee5418cf)

•	Neue Anträge:

Neue Urlaubsanträge werden per Konsoleneingabe hinzugefügt und in der CSV gespeichert.

 ![grafik](https://github.com/user-attachments/assets/80136d64-b71f-4352-a424-be89982d75b6)

•	Konfliktprüfung:

Wenn ein neuer Antrag hinzugefügt wird, prüft das Tool, ob er sich mit einem bereits genehmigten Antrag überschneidet. Falls Konflikte festgestellt werden, wird eine Liste der überschneidenden Anträge angezeigt.

 ![grafik](https://github.com/user-attachments/assets/d673b3bb-ae00-47dc-a2ee-2aaf9aff4483)

##6. Zukunft und Erweiterungen:##

Erweiterungen:

•	Benachrichtigungssystem: Eine E-Mail-Benachrichtigung könnte versendet werden, wenn Konflikte erkannt werden.

•	Datenexport als Excel: Anstelle einer CSV könnte der Export auch direkt als Excel-Datei erfolgen, um mehr Flexibilität zu bieten.

•	Webinterface: Für eine erweiterte Nutzung könnte das Tool in eine Web-App integriert werden, um eine benutzerfreundlichere Oberfläche zu bieten.
