from django.urls import include, path
from django.conf.urls import url
from rest_framework.authtoken import views as rest_framework_views
from . import views

urlpatterns = [
    path('', views.ListTodo.as_view(), name="rest_api"),
    path('<int:pk>/', views.DetailTodo.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    url('api-token-auth/', rest_framework_views.obtain_auth_token, name='get_auth_token')
]