from . import db

class User(db.Model):
    __tablename__ = 'users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255))
    user_password=db.Column(db.String(255))


    def __repr__(self):
        return f'User  {self.username}'

# class Comment(db.Model):
#     __tablename__ = 'comments'
    
#     id=db.Column(db.Integer(), primary_key=True)
#     title=db.Column(db.String())
#     comment_by = db.Column(db.String)
#     comment=db.Column(db.String())
#     date_submitted = db.Column(db.String())