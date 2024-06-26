from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.permanent_session_lifetime = timedelta(days=5)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.string(100))
    email = db.Column(db.string(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    


@app.route("/")
def void_redir():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "GET":
        if "username" in session:
            return redirect(url_for("userpage"))
        else:
            return render_template("login.html")
    else:
        user = request.form["enterence"]
        found_user = users.query.filter_by(name=user).first()
        if found_user:
             session["email"] = found_user.email
        else:
            usr = users(user, None)
            db.session.add(usr)
            db.sessioncommit()
        flash("You have been logged in succesfuly!")
        session.permanent = True
        session["username"] = request.form["enterence"]
        return redirect(url_for("userpage"))

@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username", None)
        session.pop("email", None)
        flash("you have been logged out!", "info")
    return redirect(url_for("login"))

@app.route("/usr", methods = ["POST", "GET"])
def userpage():
    email = None
    if "username" in session:
        if request.method == "POST":
            email=request.form["email"]
            session["email"] = email
            flash("your email is added succesfuly!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("/usr.html", email = email)
    else:
        return redirect(url_for("login"))




if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)