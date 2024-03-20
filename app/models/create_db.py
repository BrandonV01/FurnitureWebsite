from .base_model import db
from .shared_models import *
from argon2 import PasswordHasher

def create_db():
    create_admin()
    create_items()
    create_category()

def create_admin():
    found_user = user_info.query.filter_by(email='adminaccount@email.com').first()
    if not found_user:
        usr = user_info('adminaccount@email.com', 'admin', True)
        db.session.add(usr)
        db.session.commit()

        get_userinfo = user_info.query.filter_by(email='adminaccount@email.com').first()

        ph = PasswordHasher()
        hash_password = ph.hash('adminpassw0rd')
        auth = user_auth(get_userinfo.id, get_userinfo.email, hash_password)
        db.session.add(auth)
        db.session.commit()

def create_items():
    item = item_info('Medley Rio Sofa', "Rio Sofa's classic silhouette is wrapped in plush cushioning that pairs timeless appeal with enveloping comfort. Lean into its soft, higher seat back to find perfect upright support, or curl up and get cozy. Handcrafted in the USA to your specifications for flexible styling and comfort options."
                     , 2448, "sofa1.jpg")
    db.session.add(item)
    db.session.commit()

def create_category():
    tag = tag_list('Living Room', 'Furniture for living room', 'living_room_cat.webp')
    db.session.add(tag)

    tag = tag_list('Bedroom', 'Furniture for bedroom', 'bedroom_cat.webp')
    db.session.add(tag)

    tag = tag_list('Bathroom', 'Furniture for bathroom', 'bathroom_cat.webp')
    db.session.add(tag)

    tag = tag_list('Kitchen', 'Furniture for kitchen', 'kitchen_cat.webp')
    db.session.add(tag)

    tag = tag_list('Office', 'Furniture for office', 'office_cat.webp')
    db.session.add(tag)

    tag = tag_list('Outdoor', 'Furniture for outdoor', 'outdoor_cat.webp')
    db.session.add(tag)

    db.session.commit()