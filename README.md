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