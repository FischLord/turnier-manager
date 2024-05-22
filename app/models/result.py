from ..extensions import db

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)
    score = db.Column(db.Float)
    time_minutes = db.Column(db.Integer)
    time_seconds = db.Column(db.Integer)
    time_milliseconds = db.Column(db.Integer)
    penalty_points = db.Column(db.Float)
