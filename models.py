from __init__ import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(30), nullable=False)
    post = db.Column(db.Text, nullable=False)
    relief = db.Column(db.Boolean, default=False)
