from flask import Flask, redirect, url_for, render_template, session, request, flash
from datetime import timedelta
import datetime

class news_publication:
    def __init__(self, date, title, sub, cont):
        self.title = title
        self.sub = sub
        self.cont = cont
        self.date = date

global posts
posts = []


app = Flask(__name__)
app.secret_key = "key"
app.permanent_session_lifetime = timedelta(days=5)


@app.route("/dev")
def base():
    return render_template("base.html")

@app.route("/")
def void_redir():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/news")
def news():
    return render_template("news.html", posts=posts)

@app.route("/messages")
def messages_bar():
    return render_template("messages.html")

@app.route("/account")
def account_page():
    if "login" in session:
        return render_template("account.html", nickname = session["nickname"], email = session["email"], fn = session['fn'], sn = session['sn'])
    else:
        return redirect(url_for("login"))

@app.route("/signin", methods = ["POST", "GET"])
def signin():
    if "login" in session:
        return redirect(url_for("account_page"))
    else:
        if request.method == "GET":
            return render_template("signin.html")
        else:
            session.permanent = True
            nickname = request.form["nickname"]
            login = request.form["login"]
            password = request.form["password"]
            email = request.form["email"]
            fn = '-'
            sn = '-'
            session["nickname"] = nickname
            session["login"] = login
            session["password"] = password
            session["email"] = email
            session["fn"] = fn
            session["sn"] = sn
            print(f'\n{nickname} has been logged in\nEmail: {email}\nPassword: {password}\nLogin: {login}\n')
            return redirect(url_for("account_page"))

@app.route("/login", methods = ["POST", "GET"])
def login():
    if "login" in session:  
        return redirect(url_for("account_page"))
    else:
        if request.method == "GET":
            return render_template("login.html")
        else:
            ##change if db
            session.permanent = True
            login = request.form["login"]
            password = request.form["password"]
            nickname = request.form["login"]
            email = nickname + "@gmail.com"
            fn = '-'
            sn = '-'
            session["nickname"] = nickname
            session["login"] = login
            session["password"] = password
            session["email"] = email
            session["fn"] = fn
            session["sn"] = sn
            return redirect(url_for("account_page"))

@app.route("/logout")
def logout():
    session.pop("nickname", None)
    session.pop("email", None)
    session.pop("password", None)
    session.pop("login", None)
    flash("You have been logged out", category="info")
    return redirect(url_for("login"))

@app.route("/settings", methods = ["POST", "GET"])
def account_settings():
    if request.method == "GET":
        return render_template("settings.html", dis_email=session['email'], dis_login = session['login'], dis_password = session['password'], dis_nickname = session['nickname'], dis_fn = session['fn'], dis_sn = session['sn'])
    else:
        #if POST
        login = request.form['login']
        email = request.form['email']
        password = request.form['password']
        nickname = request.form['nickname']
        fn = request.form['fn']
        sn = request.form['sn']
        session["login"] = login
        session["email"] = email
        session["password"] = password
        session["nickname"] = nickname
        session["fn"] = fn
        session["sn"] = sn
        flash('Updated Successfully!')
        return redirect(url_for("account_page"))

@app.route('/admin', methods = ["POST", "GET"])
def admin_panel():
    if request.method == "GET":
        return render_template("admin.html")
    else:
        title = request.form['title']
        sub = request.form['sub']
        cont = request.form['cont']
        date = datetime.datetime.now()
        posts.insert(0, news_publication(date, title, sub, cont))
        return redirect(url_for("news"))


if __name__ == "__main__":
    app.run(debug=True)