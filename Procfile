# Procfile
web: gunicorn --workers=1 wsgi:app --access-logfile=-
git init
git add .
git commit -m "First deployment of Flask boilerplate"

heroku create --region=eu
git push heroku master

heroku ps                  # Do you have a free dyno up running `gunicorn`?

heroku open                # Do you get an "Hello world" in the browser?
heroku logs -n 1000 --tail # Check the access logs are c
