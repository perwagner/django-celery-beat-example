from time import sleep

from celery import shared_task
from beatme.celery import app


# @shared_task
@app.task(ignore_result=True)
def mytest(*args, **kwargs):
    print("Starting mytest task. Will sleep for 15 seconds")
    sleep(15)
    return "Success of mytest"


@shared_task
def xtask(*args, **kwargs):
    print("Start the xtask")
    print(args)
    print(kwargs)

    return "Ending the x-task"


@app.task(ignore_result=True)
def xtasklong(*args, **kwargs):
    print("Start of long task")
    sleep(20)

    print("Long task over")
    return "Success of long task"
