from quizApp import app
if __name__ == '__main__':
    app.run(debug = True, use_reloader = False)
    
    
#>>> a = Q_A.query.filter(Users.userID == 3).all()
#>>> a
#[Q_A(What is gourav's fav fruit ?, Apple, Banana, Mango, Orange), Q_A(What is gourav's fav song ?, dwed, qwwd, dwd, dwdw), Q_A(cdxvv, GK, grfdgtgrt, Mango, Orange)]

#>>> a[1]
#Q_A(What is gourav's fav song ?, dwed, qwwd, dwd, dwdw)

#>>> a[0].questions
#"What is gourav's fav fruit ?"

#>>> a[0].option1
#'Apple'

#>>> a[0].option2
#'Banana'

#>>> a[0].option3
#'Mango'

#>>> a[0].option4
#'Orange'