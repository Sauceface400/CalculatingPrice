from Name import db
import datetime

class person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return f"Person('{self.username}')"