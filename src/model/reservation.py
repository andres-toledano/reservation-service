from src import db
from src.model.classroom import Classroom
from src.model.user import User


class Reservation(db.Model):
    __tablename__ = 'reservation'
    id = db.Column(db.Integer, primary_key=True)
    classroom_id = db.Column(db.String(4), db.ForeignKey('classroom.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    classroom = db.relationship(Classroom, backref=db.backref('reservations', cascade='all, delete-orphan', lazy=True))
    user = db.relationship(User, backref=db.backref('reservations', cascade='all, delete-orphan', lazy=True))

    def __repr__(self):
        return f'<Reservation {self.id} | User: {self.user_id} | Classroom: {self.classroom_id}>'
