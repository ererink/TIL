from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('members/', views.members, name='members'),
    path('<int:pk>/', views.detail, name='detail'),
]