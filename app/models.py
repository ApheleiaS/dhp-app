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
        return 'Id %r,Username %r,Age %r, Gender %r,FavColor %r' % ( self.id, self.username, self.age, self.gender, self.favorite_color)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, nullable=False)
    answer_text =  db.Column(db.Text, nullable=False)

    def __init__(self, u_id, q_id, answer_text):
        self.user_id = u_id
        self.question_id = q_id
        self.answer_text = answer_text

    def __repr__(self):
        return 'User %r,Question %r,Answer %r' % (self.user_id, self.question_id, self.answer_text)

