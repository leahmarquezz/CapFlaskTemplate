from app import app, login
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import HomeDef
from app.classes.forms import HomeDefForm
from flask_login import login_required
import datetime as dt

@app.route('/homeDef/list')
def homeDefList():
    homeDefs = HomeDef.objects()
    return render_template('homeDefs.html',homeDefs=homeDefs)

@app.route('/homeDef/<homeDefID>')
@login_required
def homeDef(homeDefID):
    thishomeDef = HomeDef.objects.get(id=homeDefID)
    return render_template('profilemy.html',homeDef=thishomeDef)

@app.route('/homeDef/new', methods=['GET', 'POST'])
@login_required
def homeDefNew():
    form = HomeDefForm()
    if form.validate_on_submit():
        newHomeDef = HomeDef(
            subject = form.subject.data,
            definition = form.definition.data,
            author = current_user.id,
            modifydate = dt.datetime.utcnow
        )
        newHomeDef.homeimg.put(form.homeimg.data, content_type = 'image/jpeg')
        newHomeDef.save()
        return redirect(url_for('homeDef',homeDefID=newHomeDef.id))
    return render_template('homeDefform.html',form=form)

@app.route('/homeDef/edit/<homeDefID>', methods=['GET', 'POST'])
@login_required
def homeDefEdit(homeDefID):
    editHomeDef = HomeDef.objects.get(id=homeDefID)
    if current_user != editHomeDef.author:
        flash("you can't edit a post you don't own.")
        return redirect(url_for('homeDef',homeDefID=homeDefID))
    form = HomeDefForm()
    if form.validate_on_submit():
        editHomeDef.update(
            subject = form.subject.data,
            definition = form.definition.data,
            author = current_user.id,
            modifydate = dt.datetime.utcnow
        )
        if form.homeimg.data:
            if editHomeDef.homeimg:
                editHomeDef.homeimg.delete()
            editHomeDef.homeimg.put(form.homeimg.data, content_type = 'image/jpeg')
            editHomeDef.save()
        return redirect(url_for('homeDef',homeDefID=homeDefID))
    form.subject.data = editHomeDef.subject
    form.definition.data = editHomeDef.definition
    form.homeimg.data = editHomeDef.homeimg
    return render_template('homeDefform.html',form=form, homeDef=editHomeDef)

@app.route('/homeDef/delete/<homeDefID>')
@login_required
def homeDefDelete(homeDefID):
    deleteHomeDef = HomeDef.objects.get(id=homeDefID)
    if current_user == deleteHomeDef.author:
        deleteHomeDef.delete()
        flash('the post was deleted.')
    else:
        flash("you can't delete a post you don't own.")  
    return render_template('profilemy.html')