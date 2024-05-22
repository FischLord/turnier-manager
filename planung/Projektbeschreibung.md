### Projektbeschreibung für den Turnier-Manager

#### 1. **Projektziel**
Entwicklung einer Web-Anwendung namens "Turnier-Manager" zur automatisierten Erstellung und Verwaltung von Startlisten und Ergebnisauswertung für verschiedene Disziplinen im Fahrsport, einschließlich Marathon, Dressur und Hindernisfahren. Die Anwendung soll sowohl für Veranstalter als auch für Teilnehmer zugänglich sein, wobei bestimmte Bereiche nur nach Login erreichbar sind.

#### 2. **Projektanforderungen**

**2.1 Funktionale Anforderungen**
- **Teilnehmerverwaltung**: Formular zur Eingabe und Verwaltung von Teilnehmerdaten (Name, Schwierigkeitsklasse, Gespannart, etc.).
- **Veranstaltungsmanagement**: Verwaltung mehrerer Veranstaltungen mit spezifischen Details (z.B. Starttaktung, Pausen).
- **Prüfungsmanagement**:
  - Eingabe und Verwaltung von Prüfungen mit Namen, Anspannungsart und zugelassener Pferdeart (Pony oder Pferd).
  - Zuordnung von Teilnehmern zu Prüfungen.
  - Verwaltung von Startzeittabellen für jede Prüfung (Dressur, Hindernisfahren, Marathon).
- **Kombinierte Prüfungen**:
  - Verwaltung kombinierter Prüfungen, die aus Dressur, Kegelfahren und Marathon bestehen.
  - Zusammenfassung der Strafpunkte einzelner Starter aus den kombinierten Prüfungen zur Bestimmung der Gesamtsieger.
- **Benutzerverwaltung**:
  - **Login-Bereich für Veranstalter**: Veranstalter können sich anmelden, um Startzeiten zu ändern, Teilnehmer zu Prüfungen zuzuordnen, Startlisten zu verwalten und Ergebnisse einzutragen.
  - **Öffentlicher Bereich für Teilnehmer**: Teilnehmer können die aktuellen Startlisten und vorläufigen Ergebnislisten einsehen.
- **Automatisierte Startzeitberechnung**:
  - **Marathon**: Berechnung der Startzeiten unter Berücksichtigung von Schwierigkeitsklassen, individuellen Abständen zwischen Teilnehmern, anpassbaren Starttaktungen (4, 5, oder 6 Minuten) und Pausen.
  - **Dressur und Hindernisfahren**: Berechnung der Startzeiten mit der Möglichkeit, fortlaufende Startfolgen oder feste Startzeiten mit individuell einstellbaren Abständen und Pausen zu definieren.
- **Ergebnisauswertung**:
  - **Dressur**:
    - Klasse E und A: Wertnote von 1 bis 10 in 0,1er Schritten, vergeben von 1 bis 3 Richtern.
    - Klasse M und S: Punkte von 0 bis 500 pro Richter, vergeben von 1 bis 3 Richtern.
    - Möglichkeit zur Zuordnung von Richtern zu den Buchstaben C, E oder B im Dressurviereck.
  - **Hindernisfahren**: Eingabe von Strafpunkten (positiver Float) und Zeit (Minuten, Sekunden, Millisekunden). Gewinner ist der Teilnehmer mit den wenigsten Strafpunkten und der niedrigsten Zeit.
  - **Marathon**: Eingabe von Zeiten pro Hindernis und zusätzliche Strafpunkte. Klasse E fährt maximal 3 Hindernisse, A 4, M 6 und S 8 Hindernisse. Möglichkeit zum Ausschluss.
  - **Kombinierte Prüfung**: Zusammenrechnung der Strafpunkte aus Dressur, Kegelfahren und Marathon, um den Gesamtsieger zu ermitteln.
- **Live-Ergebnislisten**: Vorläufige Ergebnislisten, die live für Teilnehmer einsehbar sind.
- **Benutzeroberfläche**: Intuitive Benutzeroberfläche zur Eingabe von Daten, Anzeige der berechneten Startzeiten, Verwaltung der Startzeiten durch Veranstalter, Zuordnung von Teilnehmern zu Prüfungen und Ergebniseingabe.
- **Fehlererkennung**: Anzeige von Gründen, warum bestimmte Startzeiten nicht möglich sind, und Angabe der maximal möglichen Zeitabstände.
- **Manuelle Anpassung**: Möglichkeit für Veranstalter, Teilnehmer innerhalb der Startlisten manuell zu verschieben, bevor diese exportiert werden.
- **Filter- und Sortieroptionen**: Nach Leistungsklassen (M, A, S, E) und nach Startzeiten.
- **Export/Import**: Möglichkeit, Startlisten und Ergebnislisten zu exportieren (z.B. als PDF) und zu importieren.
- **Eindeutige Identifikation**:
  - Jeder Teilnehmer erhält pro Turnier eine eindeutige Startnummer.
  - Jeder Teilnehmer hat ein oder mehrere Pferde, die ebenfalls eine eindeutige Nummer und einen Namen pro Turnier erhalten.
  - Jeder Richter erhält eine eindeutige ID zur Identifikation, da Namen mehrfach vorkommen können.

**2.2 Nicht-funktionale Anforderungen**
- **Benutzerfreundlichkeit**: Intuitive und leicht verständliche Benutzeroberfläche.
- **Leistungsfähigkeit**: Schnelle Berechnung der Startzeiten und Auswertung der Ergebnisse auch bei vielen Teilnehmern.
- **Skalierbarkeit**: Möglichkeit zur Verwaltung mehrerer Veranstaltungen gleichzeitig.
- **Sicherheit**: Schutz der gespeicherten Teilnehmer- und Richterdaten vor unberechtigtem Zugriff und sichere Benutzeranmeldung.
- **Entwicklungsumgebung**: Bereitstellung einer Entwicklungsumgebung mittels Docker oder WSL.

#### 3. **Technologien**

**3.1 Backend**
- **Programmiersprache**: Python
- **Web-Framework**: Flask (leichtgewichtig, flexibel)
- **Datenbank**: SQLite (für kleine bis mittlere Datenmengen) oder PostgreSQL (für größere Datenmengen und bessere Skalierbarkeit)
- **Authentifizierung**: Flask-Login für Benutzeranmeldung und -verwaltung

**3.2 Frontend**
- **HTML/CSS**: Struktur und Stil der Benutzeroberfläche
- **Tailwind CSS**: Für responsives und modernes Design
- **JavaScript**: Interaktive Funktionen (z.B. Formulareingaben, dynamische Listen)
- **Flowbite**: UI-Komponentenbibliothek auf Basis von Tailwind CSS

**3.3 Sonstige Technologien**
- **Git**: Versionskontrolle
- **Docker**: Containerisierung für Development und Production
- **WSL**: Alternativ zur Entwicklungsumgebung
- **Unit-Testing**: pytest (zur Sicherstellung der Code-Qualität)

#### 4. **Projektstruktur**

**4.1 Projektphasen**

**Planung**
- Anforderungsanalyse
- Erstellung eines Lastenhefts

**Design**
- Entwurf der Softwarearchitektur
- Datenbankdesign
- UI/UX-Design

**Entwicklung**
- Implementierung des Backends
- Entwicklung der Benutzeroberfläche
- Integration des Algorithmus zur Startzeitberechnung
- Implementierung der Ergebnisauswertung

**Testen**
- Unit-Tests
- Integrationstests
- Usability-Tests

**Deployment**
- Einrichtung der Produktionsumgebung
- Deployment der Anwendung

**Wartung**
- Fehlerbehebung
- Regelmäßige Updates und Verbesserungen

#### 5. **Algorithmus zur Startzeitberechnung**

**5.1 Anforderungen**
- **Marathon**:
  - Berücksichtigung der Schwierigkeitsklassen (gemischter oder sequentieller Start)
  - Einhaltung von Mindestabständen zwischen bestimmten Teilnehmern (z.B. gleicher Beifahrer)
  - Anpassung der Starttaktung (4, 5 oder 6 Minuten)
  - Möglichkeit zur Einplanung von Pausen (maximal 8 Pausen)
  - Anpassung der Startzeiten basierend auf der benötigten Zeit für die Strecke
  - Handhabung komplexer Zeitabstände zwischen Teilnehmern (z.B. Teilnehmer A braucht 40 Minuten Abstand zu Teilnehmer B und 65 Minuten zu Teilnehmer C)
  - Anzeige der maximal möglichen Zeitabstände, falls eine Anforderung nicht vollständig erfüllt werden kann

- **Dressur und Hindernisfahren**:
  - Möglichkeit zur Definition fortlaufender Startfolgen oder fester Startzeiten
  - Individuell einstellbare Abstände zwischen den Startzeiten
  - Einplanung von Pausen zwischen den Starts

**5.2 Schritte zur Implementierung**
1. Einlesen der Teilnehmerdaten und Veranstaltungskonfiguration
2. Sortierung der Teilnehmer basierend auf den Disziplinen und Schwierigkeitsklassen
3. Iterative Berechnung der Startzeiten unter Einhaltung der Abstandsregeln und Pausen
4. Validierung der berechneten Zeiten und Identifizierung von Konflikten
5. Ausgabe der finalen Startliste oder Anzeige von Konflikten mit Angabe der maximal möglichen Zeitabstände

#### 6. **Ergebnisauswertung**

**6.1 Dressur**
- **Klasse E und A**: Wertnote von 1 bis 10 in 0,1er Schritten, vergeben von 1 bis 3 Richtern.
- **Klasse M und S**: Punkte von 0 bis 500 pro Richter, vergeben von 1 bis 3 Richtern.
- Zuordnung von Richtern zu den Buchstaben C, E oder B im Dressurviereck.
- Verwaltung der Richterdaten mit eindeutigen IDs.

**6.2 Hindernisfahren**
- Eingabe von Strafpunkten (positiver Float) und Zeit (Minuten, Sekunden, Millisekunden).
- Gewinner ist der Teilnehmer mit den wenigsten Strafpunkten und der niedrigsten Zeit.

**6.3 Marathon**
- Eingabe von Zeiten pro Hindernis und zusätzliche Strafpunkte.
- Klasse E fährt maximal 3 Hindernisse, A 4, M 6 und S 8 Hindernisse.
- Möglichkeit zum Ausschluss.

**6.4 Kombinierte Prüfungen**
- Zusammenrechnung der Strafpunkte aus

 Dressur, Kegelfahren und Marathon zur Bestimmung des Gesamtsiegers.
- Verwaltung der kombinierten Prüfungen, die die Ergebnisse der einzelnen Disziplinen zusammenfassen.

**6.5 Live-Ergebnislisten**
- Vorläufige Ergebnislisten, die live für Teilnehmer einsehbar sind.

#### 7. **Zusätzliche Anforderungen**

**7.1 Prüfungsmanagement**
- Formular zur Eingabe und Verwaltung von Prüfungen (Name, Anspannungsart, zugelassene Pferdeart).
- Möglichkeit zur Zuordnung von Teilnehmern zu Prüfungen.
- Verwaltung von Prüfungsinformationen durch Veranstalter.

**7.2 Manuelle Anpassung**
- Funktion zur manuellen Anpassung der Startzeiten durch Veranstalter vor dem Export der Startliste.

**7.3 Entwicklungsumgebung**
- **Docker**: Bereitstellung von Development- und Production-Containern.
- **WSL**: Alternativ zur Docker-Umgebung für die Entwicklung.
