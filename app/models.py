from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255))
    email= db.Column(db.String(255), unique=True, index= True)
    user_password=db.Column(db.String(255))
    bio=db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    comments=db.relationship('Comment', backref='user', lazy="dynamic")
    
    def __repr__(self):
        return f'User  {self.username}'

    @property
    def password(self):
        raise AttributeError("Password has no read attribute")
    @password.setter
    def password(self, password):
        self.user_password = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.user_password, password)
    

class Comment(db.Model):
    __tablename__='comments'

    id= db.Column(db.Integer, primary_key=True)
    pitch_comment=db.Column(db.String())
    posted=db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id= db.Column(db.Integer, db.ForeignKey('pitches.id'))
    
    def __repr__(self):
        return f'User {self.pitch_comment}'

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments=Comment.query.filter_by(pitch_id=id).all()
        return comments


class Pitch(db.Model):

    __tablename__= 'pitches'

    id=db.Column(db.Integer, primary_key=True)
    pitch_category=db.Column(db.String(255))
    pitch_upvote = db.Column(db.Integer)
    pitch_downvote= db.Column(db.Integer)
    pitch_body=db.Column(db.String(300))
    review=db.relationship('Comment', backref='pitch', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def save_pitch(self):
        db.session.add(self)
        db.session.commit
    
    @classmethod
    def get_pitch(cls, pitch_category):
        pitch=Pitch.query.filter_by(pitch_category=pitch_category).all()
        return pitch
    @classmethod
    def get_pitch_by_id(cls, pitch_id):
        pitch=Pitch.query.filter_by(pitch_id=id).all()
        return pitch
    
