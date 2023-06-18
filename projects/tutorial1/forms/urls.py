from django.urls import path

from . import views

app_name = 'forms'

urlpatterns = [
    path("", views.index, name="index"),
    path("show-forms", views.show_forms, name="show-forms"),
]
