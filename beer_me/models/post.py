from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Model
class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(80), unique=True)
    post_text = db.Column(db.String(255))

    def __init__(self, title, post_text):
        self.title = title
        self.post_text = post_text

