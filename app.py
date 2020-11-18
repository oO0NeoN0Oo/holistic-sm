from flask import Flask, escape, request, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    name = "ben"
    return render_template("home.html", name=name)

if __name__ == "__main__":
    app.run()

@app.route("/login")
def login():
    return render_template("login.html")
