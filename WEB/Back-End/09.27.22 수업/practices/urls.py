from django.urls import path
from . import views

urlpatterns = [
    path("is_odd_even/<int:_number>", views.is_odd_even),
    path("operation/<int:number1>/<int:number2>", views.operation),
    path("random_past/", views.random_past),
    path("random_past2/", views.random_past2),
    path("lorem/", views.lorem),
    path("lorem2/", views.lorem2),
    path("print-text/", views.print_text),
    path("index/", views.index),
    path("ping/", views.ping),
    path("pong/", views.pong),
]
