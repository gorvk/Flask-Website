from flask import render_template, redirect, request
from quizApp import app, db
from quizApp.form import RegisterName, SubmitOwn, SubmitReady, OwnMade, ReadyMade, PlayQuiz
from quizApp.model import Users, Q_A
from flask.helpers import url_for
from flask_login import login_user, current_user, logout_user, login_required

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
        return redirect(url_for('questionType'))
    return render_template('index.html', form = form)

@app.route('/questionType', methods = ['GET', 'POST'])
@login_required
def questionType():
    form1 = SubmitOwn()
    form2 = SubmitReady()
    
    if form1.submitOwn.data:
        return redirect(url_for('ownQue'))
    if form2.submitReady.data:
        return redirect(url_for('readyMadeQue'))
    return render_template('questionType.html', form1 = form1, form2 = form2)

@app.route('/ownQue', methods = ['GET', 'POST'])
@login_required
def ownQue():
    form = OwnMade()
    if form.validate_on_submit() and form.done.data:
        QnA = Q_A(U_ID = current_user , questions = form.question.data, option1 = form.option_1.data, option2 = form.option_2.data, option3 = form.option_3.data, option4 = form.option_4.data, answer = form.answer.data)
        db.session.add(QnA)
        db.session.commit()
        return redirect(url_for('shareQuiz'))
    elif form.validate_on_submit() and form.nxt.data:
        QnA = Q_A(U_ID = current_user , questions = form.question.data, option1 = form.option_1.data, option2 = form.option_2.data, option3 = form.option_3.data, option4 = form.option_4.data, answer = form.answer.data)
        db.session.add(QnA)
        db.session.commit()
        return redirect(url_for('ownQue'))
    return render_template('ownQue.html', form = form)

@app.route('/readyMadeQue', methods = ['GET', 'POST'])
@login_required
def readyMadeQue():
    form = ReadyMade()
    if form.validate_on_submit() and form.done.data:
        return redirect(url_for('shareQuiz'))
    elif form.validate_on_submit() and form.submitReady.data:
        return redirect(url_for('readyMadeQue'))
    elif form.validate_on_submit() and form.skip.data:
        return redirect(url_for('readyMadeQue'))
    return render_template('readyMadeQue.html', form = form)

@app.route('/shareQuiz')
@login_required
def shareQuiz():
    QAs = Q_A.query.filter_by(user_ID = current_user.userID).all()
    c_userID = current_user.userID
    return render_template('shareQuiz.html', QAs = QAs, c_userID = c_userID)
    
@app.route('/playQuiz/<_UID>', methods = ['GET', 'POST'])
def playQuiz(_UID):
    form = PlayQuiz()
    qa = Q_A.query.filter_by(user_ID = _UID).all()
    nQA = len(qa)
    if form.validate_on_submit() and form.nxt.data:
        return redirect(url_for('scoreBoard', _UID = _UID))
    return render_template('playQuiz.html', nQA = nQA, qa = qa, form = form) 

@app.route('/scoreBoard/<_UID>', methods = ['GET', 'POST'])
def scoreBoard(_UID):
    QAs = Q_A.query.filter_by(user_ID = _UID).all()
    return render_template('scoreBoard.html', QAs = QAs)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))