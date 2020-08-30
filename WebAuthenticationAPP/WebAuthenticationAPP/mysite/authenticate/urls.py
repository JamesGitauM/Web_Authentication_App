
from django.contrib import admin
from django.urls import path,include
from .import views
app_name='auth'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user,name='login'),
    path('base/', views.showbase,name='base'),
    path('logout/', views.logout_user, name='logout'),
    path('register/',views.register_user,name='register'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('change_password/',views.change_password,name='change_password'),
    path('info_page/',views.info_page,name='info_page')


]
