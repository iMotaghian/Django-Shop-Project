# 1 [website app - create pages] Continue code in "backend" dev container (><) > "python manage.py runserver 0.0.0.0:8000"
# create "website" django application in backend service
python manage.py startapp website
# add website to "INSTALLED_APPS" in settings and update core/urls for website > path('/', include('website.urls')),
# also add debug STATIC urls to core/urls > "settings.DEBUG" (only for debug mode)
# create "urls.py" in website folder and update it > urlpatterns = [] /// app_name
# create home page view in website/url and view > path("",views.IndexView.as_view(),name="index") > IndexView in view (user class TemplateView)
# create index.html & base.html in template folder
# in website/urls & website/view > views.ContactView.as_view() & views.AboutView.as_view() /// about.html /// contact.html

# 2 []



















