# [Set Bash] Continue code in "backend" dev container (><) > "python manage.py runserver 0.0.0.0:8000" /// OR /// docker-compose exec backend sh

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

# 5 [Create Admin for User & Profile] go to accounts/admin.py /// use from "django-blog"
# add "type" to "Group Permissions" and "add_fieldsets" in admin.py
# set user id and profile id became equal > in accounts/models.py add "pk=instance.pk" in "@receiver" > Profile.objects.create(user=instance, pk=instance.pk)
# make class admin for profile

# 6 [Accounting URLs & Login Page] add "accounts" app to core/urls.py > path('accounts/', include('accounts.urls'))
# make accounts/urls.py > add "login", " register" and "logout" view in paths also in accounts/views.py /// also we can use path('',include('django.contrib.auth.urls')) in accounts/urls
# make forms.py in "accounts" folder /// in views.py > LoginView /// in template make "accounts" folder & login.html
# make class AuthenticationForm in forms.py /// update login.html
# login.html > add "action" , "method" in <form>  > change name="email" to name="username" in input >  and {% csrf_token %}

# 7 [show error with toastify JS and set REDIRECT] show error in html "{% if messages %}" add to "{% block content %}" -> https://gist.github.com/adamghill/8246816
# other way: make messages.html in template and add it ro base.html
# for show alarms > Toastify JS -> https://apvarun.github.io/toastify-js/ & https://github.com/apvarun/toastify-js/blob/master/README.md
# download from https://github.com/apvarun/toastify-js/tree/master and copy "src" to project > "core/static/vendor/" and rename to toastify
# add to base.html in <script> >  <script src="{% static 'vendor/toastify/toastify.js' %}"></script>
# add to base.html in <link> CSS > <link rel="stylesheet" href="{% static 'vendor/toastify/toastify.css' %}">
# edit messages.html for add Toastify JS code > <script>
# add "LOGIN_REDIRECT_URL = '/'" to settings.py

# 8 [log out management] in accounts/urls.py > path('logout', views.LogoutView.as_view(), name='logout') /// and views.py > LogoutView
# set "LOGOUT_REDIRECT_URL" in "settings.py" for after log our direction page

# 9 [Set address to homepage Button] go to base.html and edit > "<a class="nav-link active" href="/index.html">صفحه اصلی</a>" > {% url 'website:index' %}
# "class="btn btn-primary btn-transition" > {% url 'accounts:login' %}
# open "HTML-Shop-Template" and copy code that when user is login form card.html > <a class="" href="./account-home.html"> ....
# use "{% if request.user.is_authenticated %}" for login our logout Button

# 10 [Design accounting Button] make HTML code for user profile and logout


















