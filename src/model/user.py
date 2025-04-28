from src import db
from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum


# Definir el Enum correctamente
class RoleEnum(Enum):
    ADMIN = 'admin'
    USER = 'user'


# En tu modelo
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    degree = db.Column(db.String(20), nullable=False)
    school_number = db.Column(db.String(6), unique=True, nullable=False)
    role = db.Column(SQLAlchemyEnum(RoleEnum, name='role'), nullable=False)  # Usar el Enum correctamente

    def __repr__(self):
        return f'<User {self.name}>'

    def to_dict(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "name": self.name,
            "degree": self.degree,
            "school_number": self.school_number,
            "role": self.role.name
        }
