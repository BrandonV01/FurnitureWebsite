from sqlalchemy import ForeignKeyConstraint
from .base_model import db

class user_info(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True)
    name = db.Column(db.String(50), nullable = False)
    is_admin = db.Column(db.Boolean, nullable = False)

    def __init__(self, email, name, is_admin):
        self.email = email
        self.name = name
        self.is_admin = is_admin
        
class user_auth(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    user_email = db.Column(db.String(50), primary_key = True)
    auth_password = db.Column(db.String(50), nullable = False)
    __table_args__ = (ForeignKeyConstraint([user_id, user_email], [user_info.id, user_info.email]), {})

    def __init__(self, id, email, password):
        self.user_id = id
        self.user_email = email
        self.auth_password = password

class item_info(db.Model):
    item_id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.String(50), nullable = False)
    item_description = db.Column(db.String(400), nullable = False)
    item_price = db.Column(db.Numeric(10, 2), nullable = False)
    item_image = db.Column(db.String(150), nullable = False)

    def __init__(self, name, description, price, url):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_image = url

class user_cart(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'), primary_key = True)
    item_id = db.Column(db.Integer, db.ForeignKey('item_info.item_id'), nullable = False)

    def __init__(self, user, item):
        self.user_id = user
        self.item_id = item

class tag_list(db.Model):
    tag_id = db.Column(db.Integer, primary_key = True)
    tag_name = db.Column(db.String(50), nullable = False, unique = True)
    tag_description = db.Column(db.String(400), nullable = False)
    tag_image = db.Column(db.String(150), nullable = False)

    def __init__(self, name, description, url):
        self.tag_name = name
        self.tag_description = description
        self.tag_image = url

class subtag_list(db.Model):
    tag_id = db.Column(db.Integer, primary_key = True)
    subtag_id = db.Column(db.Integer, primary_key = True)
    subtag_name = db.Column(db.String(50), nullable = False, unique = True)
    subtag_description = db.Column(db.String(400), nullable = False)
    subtag_image = db.Column(db.String(150), nullable = False)

    def __init__(self, parentid, id, name, description, url) -> None:
        self.tag_id = parentid
        self.subtag_id = id
        self.subtag_name = name
        self.subtag_description = description
        self.subtag_image = url

class item_tag(db.Model):
    item_id = db.Column(db.Integer, db.ForeignKey('item_info.item_id'), primary_key = True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag_list.tag_id'), primary_key = True)

    def __init__(self, item, tag):
        self.item_id = item
        self.tag_id = tag

class item_subtag(db.Model):
    item_id = db.Column(db.Integer, db.ForeignKey('item_info.item_id'), primary_key = True)
    subtag_id = db.Column(db.Integer, db.ForeignKey('tag_list.tag_id'), primary_key = True)

    def __init__(self, item, subtag):
        self.item_id = item
        self.subtag_id = subtag