from time import sleep

from celery import shared_task


@shared_task
def mytest():
    print("Start")

    sleep(3)

    print("Going to end")
    return "The end"
