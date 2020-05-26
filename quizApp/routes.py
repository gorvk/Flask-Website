from flask import render_template, redirect
from quizApp import app, db
from quizApp.form import RegisterName, SubmitOwn, SubmitReady, OwnMade, ReadyMade
from quizApp.model import Users, Q_A
from flask.helpers import url_for
from flask_login import login_user, current_user, logout_user

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('questionType'))
    form = RegisterName()
    if form.validate_on_submit():
        user = Users(name = form.userName.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember = True)
        print(f"Username : {form.userName.data}")
        return redirect(url_for('questionType'))
    return render_template('index.html', form = form)

@app.route('/questionType', methods = ['GET', 'POST'])
def questionType():
    form1 = SubmitOwn()
    form2 = SubmitReady()
    
    if form1.submitOwn.data:
        return redirect(url_for('ownQue'))
    if form2.submitReady.data:
        return redirect(url_for('readyMadeQue'))
    return render_template('questionType.html', form1 = form1, form2 = form2)

@app.route('/ownQue', methods = ['GET', 'POST'])
def ownQue():
    form = OwnMade()
    if form.validate_on_submit() and form.done.data:
        print(f"Question : {form.question.data}\nOptions : {form.option_1.data},  {form.option_2.data}, {form.option_3.data}, {form.option_4.data}")
        return redirect(url_for('shareQuiz'))
    elif form.validate_on_submit() and form.nxt.data:
        print(f"Question : {form.question.data}\nOptions : {form.option_1.data},  {form.option_2.data}, {form.option_3.data}, {form.option_4.data}")
        return redirect(url_for('ownQue'))
    return render_template('ownQue.html', form = form)

@app.route('/readyMadeQue', methods = ['GET', 'POST'])
def readyMadeQue():
    form = ReadyMade()
    if form.validate_on_submit() and form.done.data:
        print(f"Question : {form.question.label}\nOptions : {form.option.data}")
        return redirect(url_for('shareQuiz'))
    elif form.validate_on_submit() and form.submitReady.data:
        print(f"Question : {form.question.label}\nOptions : {form.option.data}")
        return redirect(url_for('readyMadeQue'))
    elif form.validate_on_submit() and form.skip.data:
        print(f"Question : {form.question.label}\nOptions : {form.option.data}")
        return redirect(url_for('readyMadeQue'))
    return render_template('readyMadeQue.html', form = form)

@app.route('/shareQuiz')
def shareQuiz():
    return render_template('shareQuiz.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))