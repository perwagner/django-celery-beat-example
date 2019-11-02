# django-celery-beat-example
Runs Celery beat with a DB for the scheduler


## Start worker
```
celery -A beatme worker -B -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```