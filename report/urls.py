from django.urls import path

from .views import (
    index,
    task_alpha,
    task_beta,
)


urlpatterns = [
    path('', index, name='index'),
    path('alpha', task_alpha, name='alpha'),
    path('beta', task_beta, name='beta'),

]