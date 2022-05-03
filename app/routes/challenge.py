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
            write1 = form.write1.data,
            write2 = form.write2.data,
            write3 = form.write3.data,
            write4 = form.write4.data,
            write5 = form.write5.data,
            write6 = form.write6.data,
            art1 = form.art1.data,
            art2 = form.art2.data,
            art3 = form.art3.data,
            art4 = form.art4.data,
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
            write1 = form.write1.data,
            write2 = form.write2.data,
            write3 = form.write3.data,
            write4 = form.write4.data,
            write5 = form.write5.data,
            write6 = form.write6.data,
            art1 = form.art1.data,
            art2 = form.art2.data,
            art3 = form.art3.data,
            art4 = form.art4.data,
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
        return redirect(url_for('challenge',challengeID=challengeID))
    form.write1.data = editChallenge.write1
    form.write2.data = editChallenge.write2
    form.write3.data = editChallenge.write3
    form.write4.data = editChallenge.write4
    form.write5.data = editChallenge.write5
    form.write6.data = editChallenge.write6
    form.art1.data = editChallenge.art1
    form.art2.data = editChallenge.art2
    form.art3.data = editChallenge.art3
    form.art4.data = editChallenge.art4
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