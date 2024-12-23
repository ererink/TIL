from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path('search/', views.search, name='search'),
]