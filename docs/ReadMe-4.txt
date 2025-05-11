# 1 [website app - create pages] Continue code in "backend" dev container (><) > "python manage.py runserver 0.0.0.0:8000"
# create "website" django application in backend service
python manage.py startapp website
# add website to "INSTALLED_APPS" in settings and update core/urls for website > path('/', include('website.urls')),
# also add debug STATIC urls to core/urls > "settings.DEBUG" (only for debug mode)
# create "urls.py" in website folder and update it > urlpatterns = [] /// app_name
# create home page view in website/url and view > path("",views.IndexView.as_view(),name="index") > IndexView in view (user class TemplateView)
# create index.html & base.html in template folder
# in website/urls & website/view > views.ContactView.as_view() & views.AboutView.as_view() /// about.html /// contact.html

# 2 [insert HTML for index] Continue code in "backend" dev container (><) > "python manage.py runserver 0.0.0.0:8000"
# use "Front RTL" : open index.html > copy <head> till top of code on template/base.html
# copy header body footer ...
# copy all item in "assets" folder in "Front RTL" to "static" folder
# replace address of file in code > example: "/assets/css/vendor.min.css" >>> "{% static 'css/vendor.min.css' %}"
# insert content from "Front RTL index.html" (<main></main>) >> template/index.html

# 3 [Accounting - User Model] Continue code in "backend" dev container (><) > "python manage.py runserver 0.0.0.0:8000"
# make accounts app
python manage.py startapp accounts
# make urls.py in "accounts" and fill it
# update accounts/models.py   /// make accounts/validators.py 

# 4 [Profile model & AUTH_USER_MODEL] Continue code in "backend" dev container (><) > "python manage.py runserver 0.0.0.0:8000"
# add "@receiver(post_save, sender=User)" to accounts/models and add "accounts" to settings INSTALLED_APPS
# after creating custom user model in settings we should set AUTH method (AUTH_USER_MODEL)
# need migration but we cant set makemigrations for twist for User models, so we must deleted DB and after it set makemigrations
# for delete PostgreSQL first down postgres service and delete "data" folder on "postgres" folder and restart postgres service
# in bash:
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# 5 []







docker-compose exec backend sh











