from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    age = db.Column(db.String(64), nullable=False )
    eyesightl = db.Column(db.Float, nullable=False)
    eyesightr = db.Column(db.Float, nullable=False)
    gender = db.Column(db.String(64), nullable=False)
    profession = db.Column(db.String(64), nullable=False)
    answers = db.relationship('Answer', backref='participant', lazy='dynamic')
    favorite_color = db.Column(db.Text)

    def __init__(self, username, email, age,eyesightl,eyesightr,gender,profession):
       self.username = username
       self.email = email
       self.age=age
       self.eyesightl=eyesightl
       self.eyesightr=eyesightr
       self.gender=gender
       self.profession=profession

    def __repr__(self):
        return '<User %r>' % (self.username)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer)
    answer_text =  db.Column(db.Text, nullable=False)
    def __repr__(self):
        return '<Answer %r>' % (self.answer_text)

