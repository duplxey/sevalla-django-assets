from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_view, name="uploads-index"),
    path("upload/", views.upload_view, name="uploads-upload"),
]
