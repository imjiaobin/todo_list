from django.urls import path
from . import views

# 這邊測試時,都是在/api的目錄下
urlpatterns = [
    path("", views.list, name="list"),
]
