import os

from flask_wtf import form
from Name.form import entryName, deleteBTN
from Name.model import person
from flask import render_template, redirect, url_for, request, flash
from Name import app, db

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route("/", methods=['GET', 'POST'])
def entrance():
    form = entryName()
    if form.validate_on_submit():
        user = person(username=form.username.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Welcome Plase answer the following question to get the results", 'success')
        return redirect(url_for('listName'))
    return render_template('entrance.html', form=form)

@app.route("/list", methods=['GET', 'POST'])
def listName():
    form = deleteBTN()
    user = person.query.all()
    return render_template('theList.html', user=user, form=form)

@app.route("/delete", methods=['GET', 'POST'])
def deleteStage():
    person.query.delete()
    db.session.commit()
    return redirect(url_for('entrance'))
