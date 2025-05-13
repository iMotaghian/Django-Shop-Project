# [Set Bash] Continue code in "backend" dev container (><) > "python manage.py runserver 0.0.0.0:8000" /// OR /// docker-compose exec backend sh

# 1 [Modify header and Make Store app] modify header in base.html (item list , contact us & about us)
# start app shop for our project
# bash:
python manage.py startapp shop
# add shop to setting.py (installed app)
# add in core/urls > path('shop/', include('shop.urls'))
# add "urls.py" in "shop" folder and add first url > "path("product/grid/",views.ShopProductGridView.as_view(),name="product-grid")" and set its view
# for "template_name = "shop/products-grid.html" > make new "shop" folder in template folder and make "products-grid.html"
# form "HTML-Shop-Template" open "products-grid.html" and copy code to "shop/products-grid.html"

# 2 [Shop ORM] open shop/models.py
# on_delete=models.PROTECT > if user deleted all data of user are safe and dont deleted
# allow_unicode=True > can use other language
# because we use image in database we should install pillow in bash
python -m pip install Pillow
# now we make migration in bash
python manage.py makemigrations
python manage.py migrate

# 3 [shop admin view] open shop/admin.py and make ProductModelAdmin,ProductCategoryModelAdmin,ProductImageModelAdmin
# for add to admin we can use old way in "accounts/admin" or use special decorative "@admin.register(ProductModel)" before related class (Inheritance class of model)

# 4 [make data by Faker] in "shop" folder make dir > management/commands/generate_products.py, generate_categories.py & __init__.py
# install faker with bash
pip install faker
# make commands class for generate_categories.py and run it in bash
python manage.py generate_categories
# make images folder in shop/management/commands and copy img in to folder
# make commands class for generate_products.py and run it in bash
python manage.py generate_products


# 5 [Show Product List in template] edit product-grid.html and also this view "ShopProductGridView"
# use "{% for object in object_list %}{% endfor %}" for loop of item
# "{% for category in object.category.all %}" > because category is Many To Many 
# "{% if not forloop.last %}" > in last for loop don't work
# for price use "{{object.get_price}}" > get_price make in related model and this function can calculate discount of price // (from decimal import Decimal)

# 6 []






