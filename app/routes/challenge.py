from app import app, login
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Challenge
from app.classes.forms import ChallengeForm
from flask_login import login_required
import datetime as dt

@app.route('/challenge/list')
def challengeList():
    challenges = Challenge.objects()
    return render_template('challenges.html',challenges=challenges)

# @app.route('/defaultChallenge')
# @login_required
# def defaultChallenge():
#     myChallenges = Challenge.objects(author=current_user)
#     return render_template('challenge.html', myChallenges=myChallenges)

@app.route('/challenge/<challengeID>')
@login_required
def challenge(challengeID):
    thisChallenge = Challenge.objects.get(id=challengeID)
    myChallenges = Challenge.objects(author=current_user)
    return render_template('challenge.html', myChallenges=myChallenges, challenge=thisChallenge)

@app.route('/challenge')
@login_required
def myChallenge():
    try:
        challenge = Challenge.objects.get(author=current_user.id)
    except:
        challenge = None
    return render_template('challenge.html', challenge=challenge)

@app.route('/challenge/new', methods=['GET', 'POST'])
@login_required
def challengeNew():
    form = ChallengeForm()
    if form.validate_on_submit():
        newChallenge = Challenge(
            challenge1 = form.challenge1.data,
            challenge2 = form.challenge2.data,
            challenge3 = form.challenge3.data,
            challenge4 = form.challenge4.data,
            challenge5 = form.challenge5.data,
            challenge6 = form.challenge6.data,
            challenge7 = form.challenge7.data,
            challenge8 = form.challenge8.data,
            challenge9 = form.challenge9.data,
            challenge10 = form.challenge10.data,
            reflection1 = form.reflection1.data,
            reflection2 = form.reflection2.data,
            reflection3 = form.reflection3.data,
            reflection4 = form.reflection4.data,
            reflection5 = form.reflection5.data,
            reflection6 = form.reflection6.data,
            reflection7 = form.reflection7.data,
            reflection8 = form.reflection8.data,
            reflection9 = form.reflection9.data,
            reflection10 = form.reflection10.data,
            author = current_user.id
        )
        newChallenge.save()
        return redirect(url_for('challenge',challengeID=newChallenge.id))
    return render_template('challengeform.html',form=form)

@app.route('/challenge/edit/<challengeID>', methods=['GET', 'POST'])
@login_required
def challengeEdit(challengeID):
    editChallenge = Challenge.objects.get(id=challengeID)
    if current_user != editChallenge.author:
        flash("you can't update a challenge you don't own.")
        return redirect(url_for('challenge',challengeID=challengeID))
    form = ChallengeForm()
    if form.validate_on_submit():
        editChallenge.update(
            challenge1 = form.challenge1.data,
            challenge2 = form.challenge2.data,
            challenge3 = form.challenge3.data,
            challenge4 = form.challenge4.data,
            challenge5 = form.challenge5.data,
            challenge6 = form.challenge6.data,
            challenge7 = form.challenge7.data,
            challenge8 = form.challenge8.data,
            challenge9 = form.challenge9.data,
            challenge10 = form.challenge10.data,
            reflection1 = form.reflection1.data,
            reflection2 = form.reflection2.data,
            reflection3 = form.reflection3.data,
            reflection4 = form.reflection4.data,
            reflection5 = form.reflection5.data,
            reflection6 = form.reflection6.data,
            reflection7 = form.reflection7.data,
            reflection8 = form.reflection8.data,
            reflection9 = form.reflection9.data,
            reflection10 = form.reflection10.data,
            author = current_user.id,
        )
        return redirect(url_for('challenge',challengeID=challengeID))
    form.challenge1.data = editChallenge.challenge1
    form.challenge2.data = editChallenge.challenge2
    form.challenge3.data = editChallenge.challenge3
    form.challenge4.data = editChallenge.challenge4
    form.challenge5.data = editChallenge.challenge5
    form.challenge6.data = editChallenge.challenge6
    form.challenge7.data = editChallenge.challenge7
    form.challenge8.data = editChallenge.challenge8
    form.challenge9.data = editChallenge.challenge9
    form.challenge10.data = editChallenge.challenge10
    form.reflection1.data = editChallenge.reflection1
    form.reflection2.data = editChallenge.reflection2
    form.reflection3.data = editChallenge.reflection3
    form.reflection4.data = editChallenge.reflection4
    form.reflection5.data = editChallenge.reflection5
    form.reflection6.data = editChallenge.reflection6
    form.reflection7.data = editChallenge.reflection7
    form.reflection8.data = editChallenge.reflection8
    form.reflection9.data = editChallenge.reflection9
    form.reflection10.data = editChallenge.reflection10
    return render_template('challengeform.html',form=form, challenge=editChallenge)

@app.route('/challenge/delete/<challengeID>')
@login_required
def challengeDelete(challengeID):
    deleteChallenge = Challenge.objects.get(id=challengeID)
    if current_user == deleteChallenge.author:
        deleteChallenge.delete()
        flash('the post was deleted.')
    else:
        flash("you can't delete a post you don't own.")  
    return render_template('challenge.html')