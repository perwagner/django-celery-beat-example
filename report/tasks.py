from time import sleep

from celery import shared_task


@shared_task
def mytest(*args, **kwargs):
    print("Start")
    print(args)
    sleep(3)

    print("Going to end")
    return "The end"
