from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    tweets = db.relationship('Tweet', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.username

    def to_json(self):
        return dict(
            id=self.id,
            username=self.username,
            email=self.email,
        )


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(140))
    pub_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Tweet %r>' % self.content

    def to_json(self):
        return dict(
            id=self.id,
            content=self.content,
            pub_date=str(self.pub_date),
            author=self.user_id,
        )
