from quizApp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def laod_user(userID):
    return Users.query.get(int(userID))

class Users(db.Model, UserMixin):
    __tablename__ = 'Users'

    userID = db.Column(db.Integer, nullable = False, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    QAs = db.relationship('Q_A', backref = 'U_ID', lazy = 'dynamic') 
    def get_id(self):
        return (self.userID)
    def __repr__(self):
        return f'User("{self.userID}", "{self.name}")'

class Q_A(db.Model, UserMixin):
    __tablename__ = 'Q_A'

    user_ID = db.Column(db.Integer, db.ForeignKey('Users.userID'), nullable = False)
    QAid = db.Column(db.Integer, nullable = False, primary_key = True, autoincrement = True)
    questions = db.Column(db.String, nullable = False)
    option1 = db.Column(db.String, nullable = False)
    option2 = db.Column(db.String, nullable = False)
    option3 = db.Column(db.String, nullable = False)
    option4 = db.Column(db.String, nullable = False)
    answer = db.Column(db.String, nullable = False)
    def get_id(self):
        return (self.QAid)
    def __repr__(self):
        return f'Q_A({self.QAid}, {self.questions}, {self.option1}, {self.option2}, {self.option3}, {self.option4})'
 
class Player(db.Model, UserMixin):
    __tablename__ = 'Player'
    
    playerID = db.Column(db.Integer, nullable = False, primary_key = True, autoincrement = True)
    playerName = db.Column(db.String, nullable = False)
    def get_id(self):
        return (self.playerID)
    def __repr__(self):
        return f'Player({self.playerID}, {self.playerName})'

    
class Scoreboard(db.Model, UserMixin):
    __tablename__ = 'Scoreboard'
    index = db.Column(db.Integer, nullable = False, primary_key = True, autoincrement = True)
    score = db.Column(db.Integer, nullable = False)
    playerID = db.Column(db.Integer, nullable = False)
    userID = db.Column(db.Integer, nullable = False)
    def get_id(self):
        return (self.qID)
    def __repr__(self):
        return f'Scoreboard({self.playerID}, {self.userID}, {self.score})'

class Readymade(db.Model, UserMixin):
    QAid = db.Column(db.Integer, nullable = False, primary_key = True, autoincrement = True)
    questions = db.Column(db.String, nullable = False)
    option1 = db.Column(db.String, nullable = False)
    option2 = db.Column(db.String, nullable = False)
    option3 = db.Column(db.String, nullable = False)
    option4 = db.Column(db.String, nullable = False)