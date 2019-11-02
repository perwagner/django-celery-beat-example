from time import sleep

from celery import shared_task
from beatme.celery import app


# @shared_task
@app.task(ignore_result=True)
def mytest(*args, **kwargs):
    print("Start")
    print(args)
    sleep(3)

    print("Going to end")
    return "The end"


@shared_task
def xtask(*args, **kwargs):
    print("Start the xtask")
    print(args)
    print(kwargs)

    return "Ending the x-task"