from django.urls import path
from . import views
from django.conf.urls import url

app_name = "Bot"
urlpatterns = [
    path('', views.Home, name='home'),
    path('post/', views.Post, name='post'),
]
