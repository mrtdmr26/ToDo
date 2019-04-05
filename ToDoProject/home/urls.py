from django.conf.urls import url
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home_main, name='home_main'),
    path('signup/', views.SignUp.as_view(), name='signup')
]