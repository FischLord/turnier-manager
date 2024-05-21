# Turnier-Manager

Turnier-Manager ist eine umfassende Webanwendung zur effizienten Verwaltung von Reitsportveranstaltungen, die sich speziell auf Disziplinen wie Marathon, Dressur und Hindernisfahren konzentriert. Diese Anwendung bietet Veranstaltern die notwendigen Werkzeuge zur Verwaltung von Teilnehmern, Berechnung von Startzeiten und Auswertung von Ergebnissen, um einen reibungslosen Ablauf der Veranstaltung zu gewährleisten.

## Funktionen

### Teilnehmerverwaltung
- Eingabe und Verwaltung von Teilnehmerdetails, einschließlich einzigartiger Startnummern und Pferdeinformationen.

### Veranstaltungsmanagement
- Konfiguration und Verwaltung mehrerer Veranstaltungen mit spezifischen Details wie Startintervallen und Pausen.

### Prüfungsmanagement
- Verwaltung und Planung der Startzeiten für verschiedene Disziplinen wie Dressur, Hindernisfahren und Marathon.
- Verwaltung kombinierter Prüfungen, die Ergebnisse aus mehreren Disziplinen zusammenfassen.

### Automatisierte Startzeitberechnung
- Automatische Berechnung der Startzeiten unter Berücksichtigung von Klasse, teilnehmerspezifischen Abständen und Pausen.

### Ergebnisauswertung
- Eingabe und Auswertung von Ergebnissen für Dressur (Wertnoten und Punkte) und Hindernisfahren (Zeit und Strafpunkte).
- Zusammenrechnung der Strafpunkte für kombinierte Prüfungen zur Bestimmung des Gesamtsiegers.

### Manuelle Anpassungen
- Ermöglicht Veranstaltern manuelle Anpassungen der Startlisten vor dem Export.

### Live-Ergebnislisten
- Live-Anzeige der vorläufigen Ergebnisse für Teilnehmer.

### Benutzeranmeldung
- Sicherer Login für Veranstalter zur Verwaltung von Veranstaltungsdetails und Teilnehmern.

### Export/Import-Funktionen
- Export von Start- und Ergebnislisten als PDF zur Dokumentation und Analyse.
- Import von Teilnehmer- und Veranstaltungsdaten für eine schnelle Einrichtung.

## Verwendete Technologien

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript (Flowbite)
- **Datenbank**: SQLite
- **Containerisierung**: Docker für Entwicklungs- und Produktionsumgebungen
- **Versionskontrolle**: Git

## Installation

### Voraussetzungen
- Python 3.8+
- Docker (optional für Container-Setup)

### Installationsanweisungen

1. **Repository klonen**
   ```bash
   git clone https://github.com/your-username/turnier-manager.git
   cd turnier-manager
   ```

2. **Virtuelle Umgebung erstellen und aktivieren**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

4. **Datenbank einrichten**
   ```bash
   flask db upgrade
   ```

5. **Anwendung starten**
   ```bash
   flask run
   ```

### Docker-Setup

1. **Docker-Image erstellen**
   ```bash
   docker build -t turnier-manager .
   ```

2. **Docker-Container ausführen**
   ```bash
   docker run -d -p 5000:5000 turnier-manager
   ```

## Nutzung

- Greifen Sie auf die Anwendung unter `http://localhost:5000` zu.
- Melden Sie sich mit Veranstalter-Anmeldedaten an, um Veranstaltungen und Teilnehmer zu verwalten.
- Teilnehmer können die aktuellen Startlisten und Live-Ergebnisse einsehen.

## Beitrag

Beiträge sind willkommen! Bitte forken Sie das Repository und senden Sie Pull Requests für Verbesserungen oder Fehlerbehebungen.
