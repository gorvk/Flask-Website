from flask import render_template, redirect, request
from quizApp import app, db
from quizApp.form import RegisterName, SubmitOwn, SubmitReady, OwnMade, ReadymadeForm, PlayQuiz, PlayerForm
from quizApp.model import Users, Q_A, Player, Scoreboard, Readymade
from flask.helpers import url_for
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('scoreBoard', _UID = current_user.userID))
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
    if bool(Q_A.query.filter_by(user_ID = current_user.userID).first()):
        return redirect(url_for('scoreBoard', _UID = current_user.userID))
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
    form = ReadymadeForm()
    page = request.args.get('page', 1, type=int)
    readymade = Readymade.query.paginate(per_page=1)
    ready = Readymade.query.all()
    if form.validate_on_submit() and form.done.data:
        for rm in ready:
            if rm.QAid == readymade.page:
                QnA = Q_A(U_ID = current_user , questions = rm.questions, option1 = rm.option1, option2 = rm.option2, option3 = rm.option3, option4 = rm.option4, answer = request.form['options'])
                db.session.add(QnA)
                db.session.commit()
        return redirect(url_for('shareQuiz'))
    if form.validate_on_submit() and form.submit.data:
        for rm in ready:
            if rm.QAid == readymade.page:
                QnA = Q_A(U_ID = current_user , questions = rm.questions, option1 = rm.option1, option2 = rm.option2, option3 = rm.option3, option4 = rm.option4, answer = request.form['options'])
                db.session.add(QnA)
                db.session.commit()
        return redirect(url_for('readyMadeQue', page=(readymade.page+1)))
    return render_template('readyMadeQue.html', form = form, readymade = readymade)

@app.route('/shareQuiz')
@login_required
def shareQuiz():
    QAs = Q_A.query.filter_by(user_ID = current_user.userID).all()
    c_userID = current_user.userID
    return render_template('shareQuiz.html', QAs = QAs, c_userID = c_userID)
    
@app.route('/playQuiz/<_UID>,<_PID>', methods = ['GET', 'POST'])
def playQuiz(_UID, _PID):
    form = PlayQuiz()
    qa = Q_A.query.filter_by(user_ID = _UID).all()
    nQA = len(qa)
    que, ans = [], []
    score = 0
    if form.validate_on_submit() and form.nxt.data:
        for i in range(nQA):
            if int(qa[i].answer) == int(request.form[str(i)]):
                score = score + 1
        scoreboard = Scoreboard( playerID = _PID, userID = _UID, score = score )
        db.session.add(scoreboard)
        db.session.commit()
        return redirect(url_for('scoreBoard', _UID = _UID))
    return render_template('playQuiz.html', nQA = nQA, qa = qa, form = form) 

@app.route('/scoreBoard/<_UID>', methods = ['GET', 'POST'])
def scoreBoard(_UID):
    outOfScore = Q_A.query.filter_by(user_ID = _UID).all()
    scoreboard = Scoreboard.query.filter_by(userID = _UID).all()
    playerIDs , playerNames, playerScores, player = [], [], [], []
    for i in range(len(scoreboard)):
        playerIDs.append(scoreboard[i].playerID)
        playerScores.append(scoreboard[i].score)
    scoreLen = (len(playerScores))
    for k in range(scoreLen):
        player = Player.query.filter_by(playerID = playerIDs[k]).first()
        playerNames.append(player.playerName)   
    
    return render_template('scoreBoard.html', outOfScore = len(outOfScore), _UID = _UID, scoreLen = scoreLen, playerNames = playerNames, playerScores = playerScores)

@app.route('/player/<_UID>', methods = ['GET', 'POST'])
def player(_UID):
    logout_user()
    form = PlayerForm()
    if form.validate_on_submit() and form.play.data:
        player = Player(playerName = form.playerName.data)
        db.session.add(player)
        db.session.commit()
        _PID = player.playerID
        return redirect(url_for('playQuiz', _UID = _UID, _PID = _PID))
    return render_template('player.html', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))