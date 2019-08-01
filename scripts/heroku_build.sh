docker build -t registry.heroku.com/titanic-val/web .
heroku login
heroku container:login
docker push registry.heroku.com/titanic-val/web
heroku container:release web -a titanic-val
