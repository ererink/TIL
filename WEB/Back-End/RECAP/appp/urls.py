from django.urls import path

# . => 현재의 폴더에서 views를 불러온다.
from . import views

# 앱 이름을 설정하여 해당 이름으로 불릴 수 있게 설정한다.
app_name = "appp"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("new/", views.new, name="new"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/", views.detail, name="detail"),
]
