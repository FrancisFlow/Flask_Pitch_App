from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Comment, Pitch
from flask_login import login_required, current_user
from .forms import UpdateProfile, PitchForm, CommentForm
from .. import db, photos

@main.route('/')
def index():
    """ 
    Root index page
    """
    title='PitchArena'
    pitches=Pitch.query.all()
    users= User.query.all()
    product_pitch= Pitch.query.filter_by(pitch_category='product_pitch').all()
    pickupline_pitch= Pitch.query.filter_by(pitch_category='pickuplines').all()
    return render_template('index.html', title=title, pitches=pitches, pickuplines=pickupline_pitch, users=users, product_pitch=product_pitch)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update', methods=['POST', 'GET'])
@login_required
def update_profile(uname):
    user= User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
        
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio=form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile', uname=user.username))
    
    return render_template('profile/update.html', form=form, user=user)

@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user=User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename=photos.save(request.files['photo'])
        path=f'photos/{filename}'
        user.profile_pic_path= path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))

#new comment route

@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    form=CommentForm()
    comments=Comment.query.all()
    if form.validate_on_submit():
        pitch_comment= form.pitch_comment.data
        new_comment= Comment(pitch_comment=pitch_comment)
        db.session.add(new_comment)
        db.session.commit()
        form.pitch_comment.data=""

    return render_template('comment.html', comment_form=form, comments=comments)



@main.route('/new_pitch', methods=['GET', 'POST'])
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        pitch=form.pitch_body.data
        pitch_category= form.pitch_category.data
        new_pitch=Pitch(pitch_body=pitch, pitch_category=pitch_category, pitch_upvote=0, pitch_downvote=0, posted_by=current_user.username)
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html', new_pitch_form=form)

