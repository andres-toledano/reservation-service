from src import db


class Classroom(db.Model):
    __tablename__ = 'classroom'
    id = db.Column(db.String(4), primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    block = db.Column(db.String(5), nullable=False)
    floor = db.Column(db.Integer, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Classroom {self.name}>'
