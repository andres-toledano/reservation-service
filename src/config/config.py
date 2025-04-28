import os


class Config:
    def __init__(self):
        self.ENV = os.getenv('FLASK_ENV', 'development')
        self.DEBUG = True
        self.PORT = os.getenv('PORT', 5000)
        self.HOST = '0.0.0.0'

        # Cadena de conexión modificada
        self.SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')

        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
