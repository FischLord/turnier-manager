#### 1. **Veranstaltungen (events)**
- `id`: Integer, Primary Key
- `name`: String, Name der Veranstaltung
- `start_date`: Date, Startdatum der Veranstaltung
- `end_date`: Date, Enddatum der Veranstaltung
- `location`: String, Ort der Veranstaltung

#### 2. **Prüfungen (competitions)**
- `id`: Integer, Primary Key
- `event_id`: Integer, Foreign Key (Referenz zu events.id)
- `name`: String, Name der Prüfung
- `type`: String, Typ der Prüfung (Dressur, Marathon, Hindernisfahren)
- `class`: String, Leistungsklasse (E, A, M, S)
- `allowed_horse_type`: String, Erlaubte Pferdeart (Pony, Pferd)

#### 3. **Kombinierte Prüfungen (combined_competitions)**
- `id`: Integer, Primary Key
- `event_id`: Integer, Foreign Key (Referenz zu events.id)
- `name`: String, Name der kombinierten Prüfung

#### 4. **Teilnehmer (participants)**
- `id`: Integer, Primary Key
- `name`: String, Name des Teilnehmers
- `event_id`: Integer, Foreign Key (Referenz zu events.id)

#### 5. **Startnummern (start_numbers)**
- `id`: Integer, Primary Key
- `participant_id`: Integer, Foreign Key (Referenz zu participants.id)
- `competition_id`: Integer, Foreign Key (Referenz zu competitions.id)
- `number`: Integer, Einzigartige Startnummer pro Teilnehmer und Prüfung

#### 6. **Pferde (horses)**
- `id`: Integer, Primary Key
- `name`: String, Name des Pferdes
- `participant_id`: Integer, Foreign Key (Referenz zu participants.id)
- `event_id`: Integer, Foreign Key (Referenz zu events.id)
- `horse_number`: Integer, Einzigartige Pferdenummer pro Veranstaltung

#### 7. **Richter (judges)**
- `id`: Integer, Primary Key
- `name`: String, Name des Richters

#### 8. **Prüfungs-Richter-Zuordnung (competition_judges)**
- `id`: Integer, Primary Key
- `competition_id`: Integer, Foreign Key (Referenz zu competitions.id)
- `judge_id`: Integer, Foreign Key (Referenz zu judges.id)
- `position`: String, Position des Richters (C, E, B)

#### 9. **Ergebnisse (results)**
- `id`: Integer, Primary Key
- `start_number_id`: Integer, Foreign Key (Referenz zu start_numbers.id)
- `competition_id`: Integer, Foreign Key (Referenz zu competitions.id)
- `score`: Float, Wertnote (für Dressur)
- `time_minutes`: Integer, Zeit in Minuten (für Marathon und Hindernisfahren)
- `time_seconds`: Integer, Zeit in Sekunden (für Marathon und Hindernisfahren)
- `time_milliseconds`: Integer, Zeit in Millisekunden (für Marathon und Hindernisfahren)
- `penalty_points`: Float, Strafpunkte (für Marathon und Hindernisfahren)

### Beziehungen

- **Veranstaltungen und Prüfungen**: Eine Veranstaltung kann mehrere Prüfungen haben. (1:n)
- **Veranstaltungen und kombinierte Prüfungen**: Eine Veranstaltung kann mehrere kombinierte Prüfungen haben. (1:n)
- **Teilnehmer und Veranstaltungen**: Ein Teilnehmer kann an mehreren Veranstaltungen teilnehmen. (1:n)
- **Prüfungen und Teilnehmer**: Ein Teilnehmer kann an mehreren Prüfungen innerhalb einer Veranstaltung teilnehmen. (m:n)
- **Pferde und Teilnehmer**: Ein Teilnehmer kann mehrere Pferde haben, die bei einer Veranstaltung antreten. (1:n)
- **Prüfungen und Richter**: Eine Prüfung kann mehrere Richter haben, die ihr zugeordnet sind. (m:n)
- **Startnummern und Prüfungen**: Eine Startnummer gehört zu einem Teilnehmer in einer spezifischen Prüfung. (1:n)
- **Ergebnisse und Prüfungen**: Ein Ergebnis gehört zu einer spezifischen Startnummer in einer spezifischen Prüfung. (1:n)

### Beispiel eines SQL-Schemas

```sql
CREATE TABLE events (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    location TEXT NOT NULL
);

CREATE TABLE competitions (
    id INTEGER PRIMARY KEY,
    event_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    class TEXT NOT NULL,
    allowed_horse_type TEXT NOT NULL,
    FOREIGN KEY (event_id) REFERENCES events (id)
);

CREATE TABLE combined_competitions (
    id INTEGER PRIMARY KEY,
    event_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    FOREIGN KEY (event_id) REFERENCES events (id)
);

CREATE TABLE participants (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    event_id INTEGER NOT NULL,
    FOREIGN KEY (event_id) REFERENCES events (id)
);

CREATE TABLE start_numbers (
    id INTEGER PRIMARY KEY,
    participant_id INTEGER NOT NULL,
    competition_id INTEGER NOT NULL,
    number INTEGER NOT NULL,
    FOREIGN KEY (participant_id) REFERENCES participants (id),
    FOREIGN KEY (competition_id) REFERENCES competitions (id)
);

CREATE TABLE horses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    participant_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    horse_number INTEGER NOT NULL,
    FOREIGN KEY (participant_id) REFERENCES participants (id),
    FOREIGN KEY (event_id) REFERENCES events (id)
);

CREATE TABLE judges (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE competition_judges (
    id INTEGER PRIMARY KEY,
    competition_id INTEGER NOT NULL,
    judge_id INTEGER NOT NULL,
    position TEXT NOT NULL,
    FOREIGN KEY (competition_id) REFERENCES competitions (id),
    FOREIGN KEY (judge_id) REFERENCES judges (id)
);

CREATE TABLE results (
    id INTEGER PRIMARY KEY,
    start_number_id INTEGER NOT NULL,
    competition_id INTEGER NOT NULL,
    score FLOAT,
    time_minutes INTEGER,
    time_seconds INTEGER,
    time_milliseconds INTEGER,
    penalty_points FLOAT,
    FOREIGN KEY (start_number_id) REFERENCES start_numbers (id),
    FOREIGN KEY (competition_id) REFERENCES competitions (id)
);
```
