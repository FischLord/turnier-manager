from ..extensions import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    participants = db.relationship('Participant', backref='event', lazy=True)
    competitions = db.relationship('Competition', backref='event', lazy=True)
