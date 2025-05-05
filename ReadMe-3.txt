# 1 [repo & code template] folders: docs (info of prj) / dockerfiles (dev-stage-production) / envs (environment variables in dev-stage-production) / core (app code)
# 2 [dockerfile & docker-compose.yml] in dockerfile set LABLE (set my name in maintainer) / docker-compose > db > image -> https://hub.docker.com/_/postgres
# in service > backend > image we set "context ." because docker-compose can access to root folder for user requirements.txt
# 3 []