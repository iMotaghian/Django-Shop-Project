# 1 [repo & code template] folders: docs (info of prj) / dockerfiles (dev-stage-production) / envs (environment variables in dev-stage-production) / core (app code)

# 2 [dockerfile & docker-compose.yml] in dockerfile set LABLE (set my name in maintainer) / docker-compose > db > image -> https://hub.docker.com/_/postgres
# in service > backend > image we set "context ." because docker-compose can access to root folder for user requirements.txt

# 3 [start prj & run sever] fill requirements / psycopg: connect DB (PostgreSQL) & PY
# add "command: django-admin startproject core ." to docker-compose
docker compose up --build
# core project , smtp4dev and postgres are create / ignore DB for git > postgres/data/*
# make ".gitkeep" file in empty dir for auto upload in Github // down docker-compose
# add new "command: python manage.py runserver" & "ports"on backend in docker-compose /// add "expose: - 5432"on DB in docker-compose
docker compose up --build
# -> http://127.0.0.1:8000/

# 4 [devcontainer] install extensions "dev container" - Visual Studio Code Dev Containers
# click on "><" in left bottom of VScode >  top of VScode select "Attach to Running Container..." > and select "backend" > see open new VScode in backend
# open explore and click on "Open Folder" > back one folder and go to "/usr/src/app/" and press "OK" // need install python in container
pip freeze > requirements.txt
# create new "requirements.txt" in core