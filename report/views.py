from django_celery_beat.models import (
    IntervalSchedule,
    PeriodicTask, 
)
from django.http import HttpResponse
from django.shortcuts import render

from report.models import Order


def index(request):
    context = dict()

    inteval_schedules = IntervalSchedule.objects.all()

    melco_kwargs = {"source": "melco"}
    melco_args = "[\"melco\"]"
    periodic_tasks = PeriodicTask.objects.filter(args=melco_args)
    # periodic_tasks = PeriodicTask.objects.all()
    for task in periodic_tasks:
        print(task.args)


    context['interval_schedules'] = inteval_schedules
    context['periodic_tasks'] = periodic_tasks

    return render(request, 'index.html', context)