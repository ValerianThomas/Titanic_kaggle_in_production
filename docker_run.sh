#!/bin/sh

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

cd /titanic

if [ "$SHOULD_FILL_DB" == "yes" ]; then
    python fill_db.py
fi
gunicorn api:app