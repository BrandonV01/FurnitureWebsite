from flask import Blueprint, render_template
from models.shared_models import *
from models.base_model import db

class homeCategory():
    def __init__(self, url, name):
        self.url = url
        self.name = name

# find a way to get these subcategories and maybe even the main categories from the database
livingroomSubCategory = [homeCategory("https://www.ashleyfurniture.com/on/demandware.static/-/Library-Sites-AshcommSharedLibrary/default/dw88c4e8f9/images/category/furniture/living-room/livingroom_landing_winter_20231101/LivingRoom_CLP_1A_DK.jpg", "Sofas & Couches"), homeCategory("https://www.ashleyfurniture.com/on/demandware.static/-/Library-Sites-AshcommSharedLibrary/default/dw186957e7/images/category/furniture/living-room/livingroom_landing_winter_20231101/LivingRoom_CLP_1C_DK.jpg", "Sectionals"), homeCategory("https://www.ashleyfurniture.com/on/demandware.static/-/Library-Sites-AshcommSharedLibrary/default/dw00953f58/images/category/furniture/living-room/livingroom_landing_winter_20231101/LivingRoom_CLP_1F_DK.jpg", "Recliners"), homeCategory("https://www.ashleyfurniture.com/on/demandware.static/-/Library-Sites-AshcommSharedLibrary/default/dwf24ea857/images/category/furniture/living-room/livingroom_landing_winter_20231101/LivingRoom_CLP_1H_DK.jpg", "Accent Chairs"), homeCategory("https://www.ashleyfurniture.com/on/demandware.static/-/Library-Sites-AshcommSharedLibrary/default/dw591af922/images/category/furniture/living-room/livingroom_landing_winter_20231101/LivingRoom_CLP_1K_DK.jpg", "Coffee Tables"), homeCategory("https://www.ashleyfurniture.com/on/demandware.static/-/Library-Sites-AshcommSharedLibrary/default/dwb34c3e19/images/category/furniture/living-room/livingroom_landing_winter_20231101/LivingRoom_CLP_1O_DK.jpg", "More Options")]

shop_pages = Blueprint('shop_pages', __name__, template_folder='templates')

@shop_pages.route("")
@shop_pages.route("/")
def shop():
    tags = tag_list.query
    subtags = subtag_list.query

    return render_template("shop.html", title="Shop - Furniture Store", categories = tags, subtags = subtags)

@shop_pages.route("/all")
def search_all():
    product_list = item_info.query

    return render_template("search.html", search_items = product_list, category = "all", search_name = "All Items", parentpage = "shop", title="Search - Furniture Store")

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

    return render_template("search.html", search_items = product_list, category = "all", search_name = "All Items", parentpage = "shop", title="Search - Furniture Store")

@shop_pages.route("/<string:cat_name>")
def search_cat(cat_name):

    category = tag_list.query.filter_by(tag_name = cat_name).first()
    id_list = item_tag.query.filter_by(tag_id = category.tag_id)
    
    id_array = []
    for item_id in id_list:
        id_array.append(item_id.item_id)

    product_list = item_info.query.filter(item_info.item_id.in_(id_array))

    return render_template("search.html", search_items = product_list, category = cat_name, search_name = cat_name, parentpage = "shop", title="Search - Furniture Store")

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

    return render_template("search.html", search_items = product_list, category = cat_name, search_name = cat_name, parentpage = "shop", title="Search - Furniture Store")

@shop_pages.route("/<string:cat_name>/<string:subcat_name>")
def search_subcat(cat_name, subcat_name):

    subcategory = subtag_list.query.filter_by(subtag_name = subcat_name).first()
    id_list = item_subtag.query.filter_by(subtag_id = subcategory.subtag_id)
    
    id_array = []
    for item_id in id_list:
        id_array.append(item_id.item_id)

    product_list = item_info.query.filter(item_info.item_id.in_(id_array))

    return render_template("search.html", search_items = product_list, category = cat_name, subcategory = subcat_name, search_name = subcat_name, parentpage = "shop", title="Search - Furniture Store")

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

    return render_template("search.html", search_items = product_list, category = cat_name, subcategory = subcat_name, search_name = subcat_name, parentpage = "shop", title="Search - Furniture Store")
