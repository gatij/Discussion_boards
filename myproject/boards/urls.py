from django.urls import path
from . import views


# url specific to boards app only
urlpatterns = [
    path('', views.home, name='boards_home'),
]