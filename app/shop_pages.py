from flask import Blueprint, render_template
from models.shared_models import *

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
    