from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user
import qrcode
import shutil

auth = Blueprint('auth', __name__)
e=0

@auth.route('/login',methods = ['GET','POST'])
def login():

    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password,password):
                flash("Logged in successfully ",category="success")
                login_user(user,remember = True)
                return redirect(url_for("views.main"))
            else:
               flash("Incorrect password",category="error")
        else:
           flash("email does not exist",category="error")



    return render_template("login.html")


@auth.route('/signup',methods = ['GET','POST'])
def signup():
    if request.method == "POST":

        email = request.form.get("email")
        phone = request.form.get("phone")
        name = request.form.get("name")
        password = request.form.get("password")


        if len(phone) < 10 :
            flash("Invalid phone number",category="error")

        elif len(password) < 7:
             flash("Password too short",category="error")
        elif len(name) < 2 :
            flash("Name must be greater than 1 char !!",category="error")

        else:
          user = User.query.filter_by(email=email).first()

          if not user:
            new_user = User(email=email,name=name,phone=phone,password=generate_password_hash(password,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,remember=True)
            id = current_user.id
            g = qrcode.make("http://127.0.0.1:5000//getinfo/{}".format(id))
            name = '{}.png'.format(id)
            g.save(name)
            shutil.move(fr'{name}','website/static/')

            return redirect(url_for("views.details"))
            flash("Account Created now enter your details",category="success")
          else:
             flash("email already exists",category="error")

    return render_template("signup.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("logout successful",category="success")
    return redirect(url_for("auth.login"))
@auth.route('/home',methods=['GET','POST'])
def home():
  global e
  if e==0:
    return render_template("home.html",user=current_user)
  else :
      return redirect(url_for("auth.login"))
@auth.route('/corona',methods=['GET','POST'])
def corona():
  global e
  if e==0:
    return render_template("corona.html",user=current_user)
  else :
      return redirect(url_for("auth.login"))
@auth.route('/knowledge',methods=['GET','POST'])
def coronatracker():
  global e
  if e==0:
    return render_template("knowledge.html",user=current_user)
  else :
      return redirect(url_for("auth.login"))
@auth.route('/bmi',methods=['GET','POST'])
def bmi():
  global e
  if e==0:
    return render_template("bmi.html",user=current_user)
  else :
      return redirect(url_for("auth.login"))
@auth.route('/teeth',methods=['GET','POST'])
def teeth():
  global e
  if e==0:
    return render_template("teeth.html",user=current_user)
  else :
      return redirect(url_for("auth.login"))
@auth.route('/alcohol',methods=['GET','POST'])
def alcohol():
  global e
  if e==0:
    return render_template("alcohol.html",user=current_user)
  else :
      return redirect(url_for("auth.login"))
@auth.route('/digestion',methods=['GET','POST'])
def digestion():
  global e
  if e==0:
    return render_template("digestion.html",user=current_user)
  else :
      return redirect(url_for("auth.login"))
@auth.route('/diabetes',methods=['GET','POST'])
def diabetes():
  global e
  if e==0:
    return render_template("diabetes.html",user=current_user)
  else :
      return redirect(url_for("auth.login"))
@auth.route('/menstruation',methods=['GET','POST'])
def menstruation():
  global e
  if e==0:
    return render_template("menstruation.html",user=current_user)
  else :
      return redirect(url_for("auth.login"))
@auth.route('/muscle', methods=['GET', 'POST'])
def muscle():
    global e
    if e==0:
          return render_template("muscle.html", user=current_user)
    else:
          return redirect(url_for("auth.login"))

@auth.route('/calorie', methods=['GET', 'POST'])
def calorie():
    global e
    if e==0:
          return render_template("calorie.html", user=current_user)
    else:
          return redirect(url_for("auth.login"))
@auth.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    global e
    if e==0:
          return render_template("chatbot.html", user=current_user)
    else:
          return redirect(url_for("auth.login"))

          return redirect(url_for("auth.login"))
@auth.route('/main', methods=['GET', 'POST'])
def main():
    global e
    if e==0:
          return render_template("main.html", user=current_user)
    else:
          return redirect(url_for("auth.login"))





