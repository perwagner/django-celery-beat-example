# django-celery-beat-example
Runs Celery beat with a DB for the scheduler

## Setup database and message queue
Run
```
docker-compose up
```

## Start worker
```
celery -A beatme worker -B -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

## Start app
Run
```
python manage.py migrate
python manage.py runserver
```
## Start flower
```
flower -A beatme --port=5555
```

# Notes
* The file report.tasks.py contains the tasks that are being run.  
* Use the admin interface to setup the intervals and then periodic tasks.
* Add `["melco"]` as args to the task being setup to make it appear on the '/' url. This way one can 'filter' specific tasks to be used in the UI.