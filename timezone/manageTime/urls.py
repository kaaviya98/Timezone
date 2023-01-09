from django.urls import path
from . import views

app_name = "manageTime"

urlpatterns = [
    path("", views.displayview, name="display"),
    path("change/", views.changecityview, name="change_city"),

]