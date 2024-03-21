import os
from flask import Blueprint, flash, render_template, request, redirect, url_for, session
from models.base_model import db
from models.shared_models import *
from werkzeug.utils import secure_filename

from argon2 import PasswordHasher

admin_pages = Blueprint('admin_pages', __name__, template_folder='templates/admin')

def is_admin():
    if 'userID' in session:
        user = user_info.query.filter_by(id = session['userID']).first()
        if user:
            return user.is_admin
        else:
            return 0
    else:
        return 0

@admin_pages.route("", methods=["POST", "GET"])
@admin_pages.route("/", methods=["POST", "GET"])
def admin():
    if request.method == "POST":
            ph = PasswordHasher()
            form_email = request.form["login-email"]
            form_password = request.form["login-password"]

            found_user = user_info.query.filter_by(email=form_email).first()

            if found_user and found_user.is_admin:
                db_pass = user_auth.query.filter_by(user_id = found_user.id).first()

                try:
                    ph.verify(db_pass.auth_password, form_password)
                    session['userID'] = found_user.id
                    return redirect(url_for("admin_pages.manage_products"))
                except:
                    return redirect(url_for("admin_pages.admin"))
            else:
                return redirect(url_for("admin_pages.admin"))
    else:
        if is_admin():
            return redirect(url_for("admin_pages.manage_products"))
        else:
            return render_template("admin_login.html", title="admin login")



@admin_pages.route("/manage-users", methods=['POST', 'GET'])
def manage_users():
    if is_admin():
        user_list = user_info.query
        return render_template("manage_users.html", user_list = user_list, title="Manage Users - Furniture Store")
    else:
        return redirect(url_for("admin_pages.admin"))

@admin_pages.route("/manage-users/<int:user_id>/edit", methods=["POST", "GET"])
def edit_user(user_id):
    if is_admin():
        user = user_info.query.get_or_404(user_id)
        if request.method == "POST":
            user.email = request.form["item-name"]
            user.name = request.form["item-description"]
            
            try:
                db.session.commit()
                flash('The user has been updated.', 'success')

                return redirect(url_for("admin_pages.manage_users"))
            except:
                flash('The email already in use.', 'success')
                return redirect(url_for("admin_pages.edit_user", user_id = user_id))
                

        else:
            return render_template("edit_user.html", user = user, title="Edit User - Furniture Store")
    else:
        return redirect(url_for("admin_pages.admin"))
    
@admin_pages.route("/manage-users/<int:user_id>/delete", methods=['POST'])
def delete_user(user_id):
    if is_admin():
        user = user_info.query.get_or_404(user_id)
        user_pass = user_auth.query.filter_by(user_id=user.id, user_email=user.email).first()
        db.session.delete(user)
        db.session.delete(user_pass)
        db.session.commit()
        flash('The user has been deleted', 'success')
        return redirect(url_for('admin_pages.manage_users'))

    else:
        return redirect(url_for("admin_pages.admin"))  



@admin_pages.route("/create-product", methods=["POST", "GET"])
def create_product():
    if request.method == "POST":
        form_name = request.form["item-name"]
        form_description = request.form["item-description"]
        form_price = request.form["item-price"]
        form_image = request.files['files']

        form_cat = request.form["p_tag"]
        form_subcat = request.form["s_tag"]

        found_item = item_info.query.filter_by(item_name = form_name).first()

        if found_item:
            flash('Product already exist', 'success')
            return redirect(url_for("admin_pages.create_product"))
        else:
            file_name = (secure_filename(form_image.filename))

            item = item_info(form_name, form_description, form_price, file_name)
            db.session.add(item) 

            tag = tag_list.query.filter_by(tag_name = form_cat).first()
            itemtag = item_tag(item.item_id, tag.tag_id)
            db.session.add(itemtag)

            subtag = subtag_list.query.filter_by(subtag_name = form_subcat).first()
            itemsubtag = item_subtag(item.item_id, subtag.subtag_id)
            db.session.add(itemsubtag)

            db.session.commit()
            form_image.save(os.path.join('app/static/images/items', file_name))
            
            flash('Product has been created', 'success')
            return redirect(url_for("admin_pages.manage_products"))
    else:
        if is_admin():
            tags = tag_list.query
            subtags = subtag_list.query
            
            form_subtags = []
            for subtag in subtags:
                form_subtags.append([subtag.subtag_name, subtag.parent_name])

            return render_template("create_product.html", tags = tags, subtags = form_subtags, title="Create Product - Furniture Store")
        else:
            return redirect(url_for("admin_pages.admin"))

@admin_pages.route("/manage-products", methods=["POST", "GET"])
def manage_products():
    if is_admin():
        product_list = item_info.query
        return render_template("manage_products.html", product_list = product_list, title="Manage Products - Furniture Store")
    else:
        return redirect(url_for("admin_pages.admin"))
    
@admin_pages.route("/manage-products/<int:product_id>/edit", methods=["POST", "GET"])
def edit_product(product_id):
    if is_admin():
        product = item_info.query.get_or_404(product_id)
        itemtagid = item_tag.query.filter_by(item_id = product.item_id).first()
        itemsubtagid = item_subtag.query.filter_by(item_id = product.item_id).first()
        if request.method == "POST":
            product.item_name = request.form["item-name"]
            product.item_description = request.form["item-description"]
            product.item_price = request.form["item-price"]

            form_image = request.files['files']
            file_name = (secure_filename(form_image.filename))

            tag = tag_list.query.filter_by(tag_name = request.form["p_tag"]).first()
            subtag = subtag_list.query.filter_by(subtag_name = request.form["s_tag"]).first()

            itemtagid.tag_id = tag.tag_id
            itemsubtagid.subtag_id = 1
            
            if file_name != product.item_image and file_name != "":
                product.item_image = file_name
            
                form_image.save(os.path.join('app/static/images/items', file_name))
            
            try:
                db.session.commit()
                flash('The product has been updated.', 'success')

                return redirect(url_for("admin_pages.manage_products"))
            except:
                flash('Cannot edit product, try again', 'success')
                return redirect(url_for("admin_pages.edit_product", product_id = product_id))
            
        else:
            tags = tag_list.query
            subtags = subtag_list.query

            for tag in tags:
                if tag.tag_id == itemtagid.tag_id:
                    itemtag = tag.tag_name

            for subtag in subtags:
                if subtag.subtag_id == itemsubtagid.subtag_id:
                    itemsubtag = subtag.subtag_name

            form_subtags = []
            for subtag in subtags:
                form_subtags.append([subtag.subtag_name, subtag.parent_name])
            return render_template("edit_product.html", product = product, tags = tags, subtags = form_subtags, itemtag = itemtag, itemsubtag = itemsubtag, title="Edit Product - Furniture Store")


    else:
        return redirect(url_for("admin_pages.admin"))
    
@admin_pages.route("/manage-products/<int:product_id>/delete", methods=['POST'])
def delete_product(product_id):
    if is_admin():
        product = item_info.query.get_or_404(product_id)
        db.session.delete(product)

        producttag = item_tag.query.filter_by(item_id = product_id).all()
        for pair in producttag:
            db.session.delete(pair)

        productsubtag = item_subtag.query.filter_by(item_id = product_id).all()
        for pair in productsubtag:
            db.session.delete(pair)

        db.session.commit()
        flash('The product has been deleted', 'success')
        return redirect(url_for('admin_pages.manage_products'))

    else:
        return redirect(url_for("admin_pages.admin"))  



@admin_pages.route("/create-tag", methods=["POST", "GET"])
def create_tag():
    if request.method == "POST":
        form_name = request.form["tag-name"]
        form_description = request.form["tag-descriptions"]
        form_image = request.files['files']

        found_tag = tag_list.query.filter_by(tag_name = form_name).first()

        if found_tag:
            flash('Category already exist', 'success')
            return redirect(url_for("admin_pages.create_tag"))
        else:
            file_name = (secure_filename(form_image.filename))

            tag = tag_list(form_name, form_description, file_name)
            db.session.add(tag) 
            db.session.commit()

            form_image.save(os.path.join('app/static/images/tags', file_name))
            
            flash('Category has been created', 'success')
            return redirect(url_for("admin_pages.manage_tags"))
    else:
        if is_admin():
            return render_template("create_tag.html", title="Create Category - Furniture Store")
        else:
            return redirect(url_for("admin_pages.admin"))
 
@admin_pages.route("/manage-tags", methods=["POST", "GET"])
def manage_tags():
    if is_admin():
        tags = tag_list.query
        return render_template("manage_tags.html", tag_list = tags, title="Manage Categories - Furniture Store")
    else:
            return redirect(url_for("admin_pages.admin"))

@admin_pages.route("/manage-tags/<int:tag_id>/edit", methods=["POST", "GET"])
def edit_tag(tag_id):
    if is_admin():
        tag = tag_list.query.get_or_404(tag_id)
        if request.method == "POST":
            tag.tag_name = request.form["item-name"]
            tag.tag_description = request.form["item-description"]

            form_image = request.files['files']
            file_name = (secure_filename(form_image.filename))
            
            if file_name != tag.tag_image and file_name != "":
                tag.tag_image = file_name
            
                form_image.save(os.path.join('app/static/images/tags', file_name))

            try:
                db.session.commit()
                flash('The category has been updated.', 'success')

                return redirect(url_for("admin_pages.manage_tags"))
            except:
                flash('Cannot edit category, check if name already in use', 'success')
                return redirect(url_for("admin_pages.edit_tag", subtag_id = tag_id))
            

        else:
            return render_template("edit_tag.html", tag = tag, title="Edit Category - Furniture Store")


    else:
        return redirect(url_for("admin_pages.admin"))

@admin_pages.route("/manage-tags/<int:tag_id>/delete", methods=['POST'])
def delete_tag(tag_id):
    if is_admin():
        tag = tag_list.query.get_or_404(tag_id)
        db.session.delete(tag)
        db.session.commit()
        flash('The category has been deleted', 'sucecess')
        return redirect(url_for('admin_pages.manage_tags'))
    else:
        return redirect(url_for("admin_pages.admin"))
    


@admin_pages.route("/create-subtag", methods=["POST", "GET"])
def create_subtag():
    if request.method == "POST":
        form_name = request.form["subtag-name"]
        form_description = request.form["subtag-descriptions"]
        form_parent = request.form["p_tag"]

        form_image = request.files['files']

        found_subtag = subtag_list.query.filter_by(subtag_name = form_name).first()

        if found_subtag:
            flash('Sub-Category already exist', 'success')
            return redirect(url_for("admin_pages.create_subtag"))
        else:
            file_name = (secure_filename(form_image.filename))

            subtag = subtag_list(form_name, form_parent, form_description, file_name)
            db.session.add(subtag) 
            db.session.commit()

            form_image.save(os.path.join('app/static/images/subtags', file_name))
            
            flash('Sub-Category has been created', 'success')
            return redirect(url_for("admin_pages.manage_subtags"))
    else:
        if is_admin():
            tags = tag_list.query
            return render_template("create_subtag.html", tags = tags, title="Create Sub-Category - Furniture Store")
        else:
            return redirect(url_for("admin_pages.admin"))
 
@admin_pages.route("/manage-subtags", methods=["POST", "GET"])
def manage_subtags():
    if is_admin():
        subtags = subtag_list.query
        return render_template("manage_subtags.html", subtag_list = subtags, title="Manage Sub-Categories - Furniture Store")
    else:
        return redirect(url_for("admin_pages.admin"))

@admin_pages.route("/manage-subtags/<int:subtag_id>/edit", methods=["POST", "GET"])
def edit_subtag(subtag_id):
    if is_admin():
        subtag = subtag_list.query.get_or_404(subtag_id)
        if request.method == "POST":
            subtag.subtag_name = request.form["item-name"]
            subtag.subtag_description = request.form["item-description"]

            subtag.parent_name = request.form["p_tag"]

            form_image = request.files['files']
            file_name = (secure_filename(form_image.filename))
            
            if file_name != subtag.subtag_image and file_name != "":
                subtag.subtag_image = file_name
            
                form_image.save(os.path.join('app/static/images/subtags', file_name))
            
            try:
                db.session.commit()
                flash('The sub-category has been updated.', 'success')

                return redirect(url_for("admin_pages.manage_subtags"))
            except:
                flash('Cannot edit sub-category, check if name already in use', 'success')
                return redirect(url_for("admin_pages.edit_subtag", subtag_id = subtag_id))
            

        else:
            tags = tag_list.query
            return render_template("edit_subtag.html", subtag = subtag, tags = tags, title="Edit Sub-Category - Furniture Store")


    else:
        return redirect(url_for("admin_pages.admin"))

@admin_pages.route("/manage-subtags/<int:subtag_id>/delete", methods=['POST'])
def delete_subtag(subtag_id):
    if is_admin():
        subtag = subtag_list.query.get_or_404(subtag_id)
        db.session.delete(subtag)
        db.session.commit()
        flash('The category has been deleted', 'sucecess')
        return redirect(url_for('admin_pages.manage_subtags'))
    else:
        return redirect(url_for("admin_pages.admin"))
 