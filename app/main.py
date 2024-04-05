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
                    return redirect(url_for("sync_cart"))
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

@app.route("/login/sync_cart")
def sync_cart():
    if 'Cart' in session:
        item_cart = session['Cart']
        cart = user_cart.query.filter_by(user_id = session['userID'])
        
        id_array = []
        for item in item_cart:
            id_array.append(item[0])
        
        for item in cart:
            if item.item_id not in id_array:
                item_cart.append([item.item_id, item.cart_amount])
        session['Cart'] = item_cart
        
        for item in item_cart:
            in_cart = user_cart.query.filter_by(user_id = session['userID'], item_id = item[0]).first()
            if not in_cart:
                cart = user_cart(session['userID'], item[0], item[1])
                db.session.add(cart)
                db.session.commit()
        session.pop('Cart')
        return redirect(url_for("sync_cart"))
    else:
        item_cart = []
        cart = user_cart.query.filter_by(user_id = session['userID'])

        for item in cart:
            item_cart.append([item.item_id, item.cart_amount])

        session['Cart'] = item_cart
        return redirect(url_for("home"))

@app.route("/cart")
def shopping_cart():
    if 'Cart' in session:
        shop_cart = session['Cart']

        item_ids = []
        for item in shop_cart:
            item_ids.append(item[0])
        
        item_list = item_info.query.filter(item_info.item_id.in_(item_ids))

        return render_template("cart.html", item_list = item_list, shop_cart = shop_cart)
    else:
        return render_template("cart.html")

@app.route("/cart/update_quantity/<int:item_id>/<int:quantity>")
def shopping_cart_update(item_id, quantity):
    item_cart = session['Cart']
    for item in item_cart:
        if item[0] == item_id:
            item[1] = quantity
            session['Cart'] = item_cart
            if 'userID' in session: 
                itemin_cart = user_cart.query.filter_by(user_id = session['userID'], item_id = item[0]).first()
                itemin_cart.cart_amount = item[1]
                db.session.commit()
            flash("Item amount updated", "success")
            return redirect(request.referrer)

@app.route("/cart/delete/<int:item_id>")
def shopping_cart_delete(item_id):
    item_cart = session['Cart']
    for idx, item in enumerate(item_cart):
        if item[0] == item_id:
            item_cart.pop(idx)
            session['Cart'] = item_cart
            if 'userID' in session: 
                itemin_cart = user_cart.query.filter_by(user_id = session['userID'], item_id = item[0]).first()
                db.session.delete(itemin_cart)
                db.session.commit()
            flash("Item deleted from cart", "success")
    return redirect(url_for("shopping_cart"))

@app.route("/search/<string:term>")
def search_term(term):
    term = term.title()
         
    is_category = tag_list.query.filter_by(tag_name = term).first()
    is_subcategory = subtag_list.query.filter_by(subtag_name = term).first()
    if is_category:
        return redirect(url_for("shop_pages.search_cat", cat_name = term))
    elif is_subcategory:
        return redirect(url_for("shop_pages.search_subcat",cat_name = is_subcategory.parent_name,  subcat_name = term))
    else:
        product_list = item_info.query.filter(item_info.item_name.contains(term) | item_info.item_description.contains(term))

    if not product_list.first():
        flash('Did not find matching item', 'success')
        return redirect(url_for("shop_pages.search_all"))
    
    

    return render_template("search.html", search_items = product_list, category = term, search_name = term, parentpage = "search", title="Search - Furniture Store")

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_db()
    app.run(debug=True)