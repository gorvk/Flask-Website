from flask import Flask, render_template, redirect, flash
from form import RegisterName, OwnTypeForm, ReadyTypeForm
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
    _form1 = OwnTypeForm()
    _form2 = ReadyTypeForm()
    
    if _form1.submitOwn.data:
        return redirect(url_for('ownQue'))
    if _form2.submitReady.data:
        return redirect(url_for('readyMadeQue'))
    return render_template('questionType.html', _form1 = _form1, _form2 = _form2)

@app.route('/ownQue')
def ownQue():
    return render_template('ownQue.html')

@app.route('/readyMadeQue')
def readyMadeQue():
    return render_template('readyMadeQue.html')

if __name__ == '__main__':
    app.run(debug = True)
