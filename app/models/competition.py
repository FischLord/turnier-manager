from ..extensions import db

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    class_name = db.Column(db.String(50), nullable=False)
    allowed_horse_type = db.Column(db.String(50), nullable=False)
    results = db.relationship('Result', backref='competition', lazy=True)
