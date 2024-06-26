from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from models.shared_models import *
from models.base_model import db
from sqlalchemy import and_


shop_pages = Blueprint('shop_pages', __name__, template_folder='templates')

@shop_pages.route("")
@shop_pages.route("/")
def shop():
    tags = tag_list.query
    subtags = subtag_list.query

    return render_template("shop.html", title="Shop - Furniture Store", categories = tags, subtags = subtags)

@shop_pages.route('/add_to_cart/<int:item_id>', methods=['POST'])
def add_to_cart(item_id):
    if 'Cart' in session:
        item_cart = session['Cart']
        for item in item_cart:
            if item[0] == item_id:
                item[1] += 1
                session['Cart'] = item_cart
                if 'userID' in session: 
                    itemin_cart = user_cart.query.filter_by(user_id = session['userID'], item_id = item[0]).first()
                    itemin_cart.cart_amount = item[1]
                    db.session.commit()
                flash("Item added to cart", "success")
                return redirect(request.referrer)
        item_cart.append([item_id, 1])
        session['Cart'] = item_cart
        if 'userID' in session: 
            cart = user_cart(session['userID'], item_id, 1)
            db.session.add(cart)
            db.session.commit()
        flash("Item added to cart", "success")
        return redirect(request.referrer)
    else:
        item_cart = []
        item_cart.append([item_id, 1])
        session['Cart'] = item_cart
        if 'userID' in session: 
            cart = user_cart(session['userID'], item_id, 1)
            db.session.add(cart)
            db.session.commit()
        flash("Item added to cart", "success")
        return redirect(request.referrer)
    
@shop_pages.route('/add_to_cart/<int:item_id>/<int:quantity>', methods=['POST'])
def add_to_cart_quantity(item_id, quantity):
    if 'Cart' in session:
        item_cart = session['Cart']
        for item in item_cart:
            if item[0] == item_id:
                item[1] += quantity
                session['Cart'] = item_cart
                if 'userID' in session: 
                    itemin_cart = user_cart.query.filter_by(user_id = session['userID'], item_id = item[0]).first()
                    itemin_cart.cart_amount = item[1]
                    db.session.commit()
                flash("Item added to cart", "success")
                return redirect(request.referrer)
        item_cart.append([item_id, quantity])
        session['Cart'] = item_cart
        if 'userID' in session: 
            cart = user_cart(session['userID'], item_id, quantity)
            db.session.add(cart)
            db.session.commit()
        flash("Item added to cart", "success")
        return redirect(request.referrer)
    else:
        item_cart = []
        item_cart.append([item_id, quantity])
        session['Cart'] = item_cart
        if 'userID' in session: 
            cart = user_cart(session['userID'], item_id, quantity)
            db.session.add(cart)
            db.session.commit()
        flash("Item added to cart", "success")
        return redirect(request.referrer)

@shop_pages.route("/all")
def search_all():
    product_list = item_info.query

    return render_template("search.html", search_items = product_list, category = "all", search_name = "All Items", parentpage = "shop", title="Search All - Furniture Store")

@shop_pages.route("/all/sort/<string:filter>")
def filtered_search_all(filter):
    if filter == "name-ascending":
        product_list = item_info.query.order_by(item_info.item_name.desc())
    elif filter == "name-descending":
        product_list = item_info.query.order_by(item_info.item_name.asc())
    elif filter == "price-ascending":
        product_list = item_info.query.order_by(item_info.item_price.asc())
    else:
        product_list = item_info.query.order_by(item_info.item_price.desc())

    return render_template("search.html", search_items = product_list, category = "all", search_name = "All Items", parentpage = "shop", title="Search All - Furniture Store")

@shop_pages.route("/Deals")
def search_deals():

    subcategories = subtag_list.query.filter(subtag_list.subtag_name.contains("Deals"))

    deal_ids = []
    for deal_tag in subcategories:
        deal_ids.append(deal_tag.subtag_id)

    id_list = item_subtag.query.filter(item_subtag.subtag_id.in_(deal_ids))
    
    id_array = []
    for item_id in id_list:
        id_array.append(item_id.item_id)

    product_list = item_info.query.filter(item_info.item_id.in_(id_array))

    return render_template("search.html", search_items = product_list, category = "Deals", search_name = "All Deals", parentpage = "shop", deal_categories = subcategories, title="Deals - Furniture Store")

@shop_pages.route("/Deals/sort/<string:filter>")
def filtered_search_deals(filter):
    subcategories = subtag_list.query.filter(subtag_list.subtag_name.contains("Deals"))

    deal_ids = []
    for deal_tag in subcategories:
        deal_ids.append(deal_tag.subtag_id)

    id_list = item_subtag.query.filter(item_subtag.subtag_id.in_(deal_ids))
    
    id_array = []
    for item in id_list:
        id_array.append(item.item_id)

    if filter == "name-ascending":
        product_list = item_info.query.filter(item_info.item_id.in_(id_array)).order_by(item_info.item_name.desc())
    elif filter == "name-descending":
        product_list = item_info.query.filter(item_info.item_id.in_(id_array)).order_by(item_info.item_name.asc())
    elif filter == "price-ascending":
        product_list = item_info.query.filter(item_info.item_id.in_(id_array)).order_by(item_info.item_price.asc())
    else:
        product_list = item_info.query.filter(item_info.item_id.in_(id_array)).order_by(item_info.item_price.desc())


    return render_template("search.html", search_items = product_list, category = "Deals", search_name = "All Deals", parentpage = "shop", deal_categories = subcategories, title="Deals - Furniture Store")

@shop_pages.route("/Deals/<string:cat_name>")
def search_cat_deals(cat_name):

    subcategory = subtag_list.query.filter(and_(subtag_list.subtag_name.contains("Deals"), subtag_list.parent_name == cat_name)).first()
    
    id_list = item_subtag.query.filter(item_subtag.subtag_id == subcategory.subtag_id)
    
    id_array = []
    for item_id in id_list:
        print(item_id.item_id)
        id_array.append(item_id.item_id)

    product_list = item_info.query.filter(item_info.item_id.in_(id_array))

    return render_template("search.html", search_items = product_list, category = "Deals", subcategory = cat_name, search_name = cat_name+" Deals", parentpage = "shop", title="Deals "+cat_name+" - Furniture Store")

@shop_pages.route("/Deals/<string:cat_name>/sort/<string:filter>")
def filtered_cat_deals(cat_name, filter):
    
    subcategory = subtag_list.query.filter(and_(subtag_list.subtag_name.contains("Deals"), subtag_list.parent_name == cat_name)).first()
    
    id_list = item_subtag.query.filter(item_subtag.subtag_id == subcategory.subtag_id)
    
    id_array = []
    for item_id in id_list:
        print(item_id.item_id)
        id_array.append(item_id.item_id)

    if filter == "name-ascending":
        product_list = item_info.query.filter(item_info.item_id.in_(id_array)).order_by(item_info.item_name.desc())
    elif filter == "name-descending":
        product_list = item_info.query.filter(item_info.item_id.in_(id_array)).order_by(item_info.item_name.asc())
    elif filter == "price-ascending":
        product_list = item_info.query.filter(item_info.item_id.in_(id_array)).order_by(item_info.item_price.asc())
    else:
        product_list = item_info.query.filter(item_info.item_id.in_(id_array)).order_by(item_info.item_price.desc())
    
    return render_template("search.html", search_items = product_list, category = "Deals", subcategory = cat_name, search_name = cat_name+" Deals", parentpage = "shop", title="Deals "+cat_name+" - Furniture Store")

@shop_pages.route("/<string:cat_name>")
def search_cat(cat_name):

    category = tag_list.query.filter_by(tag_name = cat_name).first()
    id_list = item_tag.query.filter_by(tag_id = category.tag_id)
    
    id_array = []
    for item_id in id_list:
        id_array.append(item_id.item_id)

    product_list = item_info.query.filter(item_info.item_id.in_(id_array))

    return render_template("search.html", search_items = product_list, category = cat_name, search_name = cat_name, parentpage = "shop", title="Search "+cat_name+" - Furniture Store")

@shop_pages.route("/<string:cat_name>/sort/<string:filter>")
def filtered_search_cat(cat_name, filter):

    category = tag_list.query.filter_by(tag_name = cat_name).first()
    id_list = item_tag.query.filter_by(tag_id = category.tag_id)
    
    id_array = []
    for item_id in id_list:
        id_array.append(item_id.item_id)

    if filter == "name-ascending":
        product_list = item_info.query.filter(item_info.item_id.in_(id_array)).order_by(item_info.item_name.desc())
    elif filter == "name-descending":
        product_list = item_info.query.filter(item_info.item_id.in_(id_array)).order_by(item_info.item_name.asc())
    elif filter == "price-ascending":
        product_list = item_info.query.filter(item_info.item_id.in_(id_array)).order_by(item_info.item_price.asc())
    else:
        product_list = item_info.query.filter(item_info.item_id.in_(id_array)).order_by(item_info.item_price.desc())

    return render_template("search.html", search_items = product_list, category = cat_name, search_name = cat_name, parentpage = "shop", title="Search "+cat_name+" - Furniture Store")

@shop_pages.route("/<string:cat_name>/<string:subcat_name>")
def search_subcat(cat_name, subcat_name):

    subcategory = subtag_list.query.filter_by(subtag_name = subcat_name).first()
    id_list = item_subtag.query.filter_by(subtag_id = subcategory.subtag_id)
    
    id_array = []
    for item_id in id_list:
        id_array.append(item_id.item_id)

    product_list = item_info.query.filter(item_info.item_id.in_(id_array))

    return render_template("search.html", search_items = product_list, category = cat_name, subcategory = subcat_name, search_name = subcat_name, parentpage = "shop", title="Search "+subcat_name+" - Furniture Store")

@shop_pages.route("/<string:cat_name>/<string:subcat_name>/sort/<string:filter>")
def filtered_search_subcat(cat_name, subcat_name, filter):

    subcategory = subtag_list.query.filter_by(subtag_name = subcat_name).first()
    id_list = item_subtag.query.filter_by(subtag_id = subcategory.subtag_id)
    
    id_array = []
    for item_id in id_list:
        id_array.append(item_id.item_id)

    if filter == "name-ascending":
        product_list = item_info.query.filter(item_info.item_id.in_(id_array)).order_by(item_info.item_name.desc())
    elif filter == "name-descending":
        product_list = item_info.query.filter(item_info.item_id.in_(id_array)).order_by(item_info.item_name.asc())
    elif filter == "price-ascending":
        product_list = item_info.query.filter(item_info.item_id.in_(id_array)).order_by(item_info.item_price.asc())
    else:
        product_list = item_info.query.filter(item_info.item_id.in_(id_array)).order_by(item_info.item_price.desc())

    return render_template("search.html", search_items = product_list, category = cat_name, subcategory = subcat_name, search_name = subcat_name, parentpage = "shop", title="Search "+subcat_name+" - Furniture Store")

@shop_pages.route("/p/<int:item_id>")
def item_page(item_id):

    item_information = item_info.query.filter_by(item_id = item_id).first()

    itemtag = item_tag.query.filter_by(item_id = item_id).first()
    itemsubtag = item_subtag.query.filter_by(item_id = item_id).first()

    cat = tag_list.query.filter_by(tag_id = itemtag.tag_id).first()
    subcat = subtag_list.query.filter_by(subtag_id = itemsubtag.subtag_id).first()


    return render_template("item_page.html", item_information = item_information, category = cat.tag_name, subcategory = subcat.subtag_name)