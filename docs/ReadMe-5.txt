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











