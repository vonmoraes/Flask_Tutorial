from flask import (
    Flask, redirect, url_for, render_template, request, session, flash
)
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

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
class user(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column( db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email
    pass
pass

@app.route("/")
def home():
    return render_template("index.html")
pass

"""
! #1 BASICS


@app.route("/user_teste/<name>")
def user_test(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="admin"))
"""
"""
! #2 HTML

@app.route("/<text>")
def home_page(text):
    names_list = ["lucas", "luana", "lukita", "luanita"]
    return render_template("video1.html"
        ,content = text
        ,names=names_list
    )
    
    # <body>
    #     <h1> HELLO </h1>
    #     <!-- receive var from python code -->
    #     <!-- {% #expression statement %} -->
    #     <p> TEXT : {{content}}</p>
    #     {% for x in names %}
    #         <!-- {{variable}} -->
    #         <p> IMPAR: {{x}} </p>
    #     {% endfor %}
    # </body>
    
pass
"""
"""
! #3 BOOTSTRAP - INHERITANCE

@app.route("/boot")
def boot_page():
    text = "Some content! "
    return render_template("index.html"
        ,content = text
    )
pass
"""
"""
! #4 HTTP Methods (GET/POST)
! #5 SESSIONS
! #6 FLASH
! #7 SQLAlchemy
! #8 Continuação SQLAlchemy
"""
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        _user = request.form["_name"]
        if len(_user) > 0:
            session.permanent = True #by default session dont save permanent data
            session["user"] = _user

            found_user = user.query.filter_by(name=_user).first()
            if found_user:
                session["email"] = found_user.email
            else:
                usr = user(_user, "")
                db.session.add(usr) # ADD TO DB
                db.commit()


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
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html"
            ,user=user
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



# Last video: Flask Tutorial #3
if __name__ == "__main__":
    print("Hello o/")
    db.create_all()
    # debug = true, restart the app when file is saved
    app.run(debug=True)
pass

