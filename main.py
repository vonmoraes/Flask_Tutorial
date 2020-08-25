from flask import (
    Flask, redirect, url_for, render_template
)
app = Flask(__name__)


# aula 1
@app.route("/<text>")
def home_page(text):
    return render_template("index.html", content = text, names=)
pass

@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"


@app.route("/admin")
def admin():
    return redirect(url_for("user", name="admin"))

#aula 2


if __name__ == "__main__":
    print("Hello o/")
    app.run()
pass

