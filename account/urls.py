from django.urls import path

from account import views


urlpatterns = [
    path('login/', views.login, name="login"),
    path('logut/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
]
