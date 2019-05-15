from django.urls import path
from . import views
from django.conf.urls import url

app_name = "Bot"
urlpatterns = [
    path('', views.Home, name='Bot-Home'),
    #path('Bot/', Post.as_view()),
]
