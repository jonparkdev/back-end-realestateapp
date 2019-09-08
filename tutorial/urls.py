
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from tutorial.quickstart import views

urlpatterns = [
    url(r'^transactions/$', views.transaction),
]
