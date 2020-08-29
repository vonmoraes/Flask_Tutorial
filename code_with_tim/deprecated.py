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