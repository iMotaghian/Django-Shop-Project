# 1 [repo & code template] folders: docs (info of prj) / dockerfiles (dev-stage-production) / envs (environment variables in dev-stage-production) / core (app code)

# 2 [dockerfile & docker-compose.yml] in dockerfile set LABLE (set my name in maintainer) / docker-compose > db > image -> https://hub.docker.com/_/postgres
# in service > backend > image we set "context ." because docker-compose can access to root folder for user requirements.txt

# 3 [start prj & run sever] fill requirements / psycopg: connect DB (PostgreSQL) & PY
# add "command: django-admin startproject core ." to docker-compose
docker compose up --build
# core project , smtp4dev and postgres are create / ignore DB for git > postgres/data/*
# make ".gitkeep" file in empty dir for auto upload in Github /// down docker-compose
# add new "command: python manage.py runserver" & "ports"on backend in docker-compose /// add "expose: - 5432"on DB in docker-compose
docker compose up --build
# -> http://127.0.0.1:8000/

# 4 [devcontainer] install extensions "dev container" - Visual Studio Code Dev Containers
# click on (><) in left bottom of VScode >  top of VScode select "Attach to Running Container..." > and select "backend" > see open new VScode in backend
# open explore and click on "Open Folder" > back one folder and go to "/usr/src/app/" and press "OK" /// need install python in container
pip freeze > requirements.txt
# create new "requirements.txt" in core

# 5 [add environment variable] Continue code in "backend" dev container (><) > "python manage.py runserver 0.0.0.0:8000" > dir: "/usr/src/app/"
# in docker-compose.yml change backend command "runserver" to "bash"
python manage.py runserver 0.0.0.0:8000
# use "python-decouple" for set environment -> https://pypi.org/project/python-decouple/
pip install python-decouple
pip freeze > requirements.txt
# in settings: "from decouple import config" > "config('SECRET_KEY')" /// change "DEBUG"
# change "ALLOWED_HOSTS" /// update'DIRS' in template 
# set "DATABASES" for connect to "PostgreSQL" (in docker-compose > port:5432, user o pass:postgres)
# TIME_ZONE = config("TIME_ZONE",default="UTC")
# add "MEDIA_URL = 'media/'" /// "STATIC_ROOT = BASE_DIR / 'staticfiles'" /// "MEDIA_ROOT = BASE_DIR / 'media'"
# make "static" , "media" & "staticfiles" folder in root folder of core
# add "STATICFILES_DIRS" /// add email config
python manage.py makemigrations
python manage.py migrate
# for check DB install extension > Database Client -> https://marketplace.visualstudio.com/items/?itemName=cweijan.vscode-database-client2
# and set "ports: - 5432:5432" for DB services , after we can connect to DB with "Database Client"

# 6 [Setup project] Continue code in "backend" dev container (><) > "python manage.py runserver 0.0.0.0:8000" /// pip install django-debug-toolbar
# for active DEBUGGER_TOOLBAR set in settings.py > "SHOW_DEBUGGER_TOOLBAR = config("SHOW_DEBUGGER_TOOLBAR", cast=bool, default=True)" /// add url > core/urls.py





