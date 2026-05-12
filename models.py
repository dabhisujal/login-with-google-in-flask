from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String(200), unique=True, nullable=True)
    email = db.Column(db.String(200), unique=True)
    picture = db.Column(db.String(300))

    def __str__(self):
        return f"User: {self.email}"