from flask import Flask, render_template, redirect, flash
from form import RegisterName, SubmitOwn, SubmitReady, OwnMade, ReadMade
from flask.helpers import url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gstar1525'

@app.route('/', methods = ['GET', 'POST'])
def index():
    _form = RegisterName()
    if _form.validate_on_submit():
        return redirect(url_for('questionType'))
    return render_template('index.html', _form = _form)

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
    if form.done.data:
        return redirect(url_for('shareQuiz'))
    return render_template('ownQue.html', form = form)

@app.route('/readyMadeQue', methods = ['GET', 'POST'])
def readyMadeQue():
    form = ReadMade()
    if form.done.data:
        return redirect(url_for('shareQuiz'))
    return render_template('readyMadeQue.html', form = form)

@app.route('/shareQuiz')
def shareQuiz():
    return render_template('shareQuiz.html')

if __name__ == '__main__':
    app.run(debug = True)