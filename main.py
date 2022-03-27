from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(50))
    level = db.Column(db.String(50))
    xp = db.Column(db.String(50))
    credit = db.Column(db.String(50))


x = 0

user_list = []

chart = {25: [10, 25], 35: [15, 35], 45: [20, 45]}

@app.route('/banned_web_attempt', methods = ["POST"])
def update_num():
    global x

    if request.get_data().decode("utf-8")  != "breach=true" and x == 0:
        return jsonify('',render_template('study_update.html', x = 'STUDYING'))

    else:
        print('Recieved notice of attempt to access banned website.')
        if x == 0:
            x += 5
        else:
            x -= 1
        return jsonify('',render_template('study_update.html', x = 'NOT STUDYING'))
    

@app.route('/update_stats', methods = ["POST"])
def update_stats():
        print(request.get_data().decode("utf-8"))
        time = request.get_data().decode("utf-8")[5:7]
        time = int(time)
        print(time)
        username = request.get_data().decode("utf-8")[14:]
        print(username)
        user = User.query.filter_by(user = username).first()

        new_xp = int(user.xp) + chart[time][0]
        new_xp = str(new_xp)
        new_credits = int(user.credit) + chart[time][1]
        new_credits = str(new_credits)
        new_level = int(user.level) + 1
        new_level = str(new_level)

        db.session.delete(user)
        db.session.commit()


        user = User(user = username, level = new_level, xp = new_xp, credit = new_credits)
        db.session.add(user)
        db.session.commit()

        return "success"
     
@app.route('/study', methods = ["GET"])
def study():
    global user_list

    username =  request.args.get('username')

    if User.query.filter_by(user = username).first() is None:
        user = User(user = username, level = '0', xp = '0', credit = '0')
        db.session.add(user)
        db.session.commit()
        print('recived sign in from ' + username + ' and added query')
        user_list.append(username)
    else:
        print('Returning sign in from ' + username)
        user_list.append(username)
    
    return render_template('study.html', x = 'STUDYING', username = username)


@app.route('/stats', methods = ["POST"])
def stats():
    username = request.form.get('username')
    print(username)
    user = User.query.filter_by(user = username).first()
    return render_template('stats.html', username = user.user, level = user.level, xp = user.xp, credit = user.credit)

    
app.run(debug = True)