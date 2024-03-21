from flask import Flask, flash, redirect, url_for, render_template, request, session
from shop_pages import shop_pages
from admin_pages import admin_pages
from models.base_model import db
from models.shared_models import *
from models.create_db import create_db
from argon2 import PasswordHasher

app = Flask(__name__)
app.register_blueprint(shop_pages, url_prefix="/shop")
app.register_blueprint(admin_pages, url_prefix="/admin")
app.secret_key = "ags69tgano10"

app.config['UPLOAD_FOLDER'] = '/static/images'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furniture_store.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
@app.route("/Home")
@app.route("/home")
def home():
    saleUrls = ['images/floorsale.png', 'images/newyearsale.jpg', 'images/febsale.jpg', 'images/presidentsale.jpg']
    tags = tag_list.query

    return render_template("home.html", title = "Furniture Store", urls = saleUrls, categories = tags)

@app.route("/login", methods=["POST", "GET"])   
def login():
    if request.method == "POST":
        ph = PasswordHasher()

        if request.form["form-group"] == "SignIn":
            form_email = request.form["login-email"]
            form_password = request.form["login-password"]
    
            found_user = user_info.query.filter_by(email = form_email).first()
            
            if found_user:
                db_pass = user_auth.query.filter_by(user_id = found_user.id).first()

                try:
                    ph.verify(db_pass.auth_password, form_password)
                    session['userID'] = found_user.id
                    flash('Successfully logged in!', 'success')
                    return redirect(url_for("home"))
                except:
                    flash('Unable to successfully login', 'success')
                    return redirect(url_for("login"))
            else:
                flash('Unable to successfully login', 'success')
                return redirect(url_for("login"))

        elif request.form["form-group"] == "CreateAccount":
            fname = request.form["signup-fname"]
            lname = request.form["signup-lname"]
            fullname = fname + " " + lname
            form_email = request.form["signup-email"]
            form_password = request.form["signup-password"]
            hash_password = ph.hash(form_password)
            
            found_user = user_info.query.filter_by(email=form_email).first()

            if found_user:
                flash('User already exist', 'success')
                return redirect(url_for("login"))
            else:
                usr = user_info(form_email, fullname, False)
                db.session.add(usr)
                db.session.commit()

                get_userinfo = user_info.query.filter_by(email=form_email).first()

                auth = user_auth(get_userinfo.id, get_userinfo.email, hash_password)
                db.session.add(auth)
                db.session.commit()
                
                flash('Account created successfully', 'success')

                return redirect(url_for("login"))

    else:
        return render_template("login.html", title = "Login - Furniture Store")
    
@app.route("/logout")   
def logout():
    if 'userID' in session: 
        session.pop('userID', None)
        flash('User logged out', 'success')
        return redirect(url_for("home"))
    else:
        flash('No user logged in', 'success')
        return redirect(url_for("login"))

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_db()
    app.run(debug=True)