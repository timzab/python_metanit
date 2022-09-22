from django.urls import path
from hello import views
# Примечание

urlpatterns = [
    path("", views.index),
    path("contacts/", views.contacts),
]