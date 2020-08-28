from flask import (
    Flask, redirect, url_for, render_template, request, session
)
from datetime import timedelta

app = Flask(__name__)
"""
! SESSION DATA
"""
app.secret_key = "HEAUH@#*&(!*#H$)@"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return redirect(url_for("login"))
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
"""
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["_name"]
        if len(user) > 0:
            session.permanent = True #by default session dont save permanent data
            session["user"] = user
            return redirect(url_for("user"))
        else: 
            return render_template("login.html")
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")
pass 

@app.route("/user/")
def user():
    if "user" in session:
        user = session["user"]
        print(user)
        return render_template("user.html"
            ,user=user
        )
    else:
        return redirect(url_for("login"))
pass 

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
pass



# Last video: Flask Tutorial #3
if __name__ == "__main__":
    print("Hello o/")
    # debug = true, restart the app when file is saved
    app.run(debug=True)
pass

