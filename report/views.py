from celery.result import AsyncResult
from django_celery_beat.models import (
    IntervalSchedule,
    PeriodicTask, 
)
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from report.models import Order
from report.tasks import (
    mytest,
    xtask,
    xtasklong,
)
from report.forms import (
    AsyncResultForgetForm,
)


def index(request):
    if request.method == 'POST':
        form = AsyncResultForgetForm(request.POST)

        if form.is_valid():
            queue_id = form.cleaned_data['async_result']
            print(f"ID: {queue_id}")


            res = AsyncResult(queue_id)
            print(f"res.ready: {res.ready()}")
            print(f"res.status: {res.status}")
            
            print(res.result)
            res.forget()

            return HttpResponseRedirect('')




    context = dict()
    form = AsyncResultForgetForm()

    inteval_schedules = IntervalSchedule.objects.all()

    melco_kwargs = {"source": "melco"}
    melco_args = "[\"melco\"]"
    periodic_tasks = PeriodicTask.objects.filter(args=melco_args)
    # periodic_tasks = PeriodicTask.objects.all()
    for task in periodic_tasks:
        print(task.args)


    context['interval_schedules'] = inteval_schedules
    context['periodic_tasks'] = periodic_tasks
    context['form'] = form

    return render(request, 'index.html', context)



def task_alpha(request):
    context = dict()

    r = xtasklong.delay()
    print(r)
    context['result'] = r

    return render(request, 'task_alpha.html', context)    


def task_beta(request):
    context = dict()

    r = xtask.delay()
    print(r)
    context['result'] = r

    return render(request, 'task_alpha.html', context)        