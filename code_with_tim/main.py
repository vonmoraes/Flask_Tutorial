from flask import (
    Flask, redirect, url_for, render_template, request, session, flash
)
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
"""
! SESSION DATA AND APP CONFIG
"""
app.secret_key = "precisaparacriarsesion"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

"""
! MODULE
"""
db = SQLAlchemy(app)
class dbuser(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column( db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email
    pass
pass

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")
pass

"""
! #4 HTTP Methods (GET/POST)
! #5 SESSIONS
! #6 FLASH
! #7 SQLAlchemy
! #8 Continuação SQLAlchemy
! #9 Static (Compensa ver para pegar arquivos na pasta)
?     url_for('static', filename='nome')  
"""
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        _user = request.form["_name"]
        if len(_user) > 0:
            session.permanent = True #by default session dont save permanent data
            session["user"] = _user
            found_user = dbuser.query.filter_by(name=_user).first()
            if found_user:
                session["email"] = found_user.email
            else:
                usr = dbuser(_user, "")
                db.session.add(usr) # ADD TO DB
                db.session.commit()
            return redirect(url_for("user"))
        else: 
            return render_template("login.html")
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")
pass 

@app.route("/user/", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = dbuser.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html"
            ,user=user
            ,email=email
        )
    else:
        return redirect(url_for("login"))
pass 

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("email", None)
    flash("You have been logged out!", "info")
    return redirect(url_for("login"))
pass

@app.route("/view/users")
def view_users():
    return render_template("view.html", values=dbuser.query.all())
pass


@app.route("/view/users/delete/<user>")
def delete_users(user):
    found_user = dbuser.query.filter_by(name=user).delete()
    return "deleted"
pass



# Last video: Flask Tutorial #3
if __name__ == "__main__":
    if not os.path.exists('users.sqlite3'):
        db.create_all()
    # debug = true, restart the app when file is saved
    app.run(debug=True)
pass

