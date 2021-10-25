from helpers.app_setup import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    complete = db.Column(db.Boolean, nullable=False)
    depends_on = db.Column(db.PickleType, nullable=True)
    db.UniqueConstraint(title)
