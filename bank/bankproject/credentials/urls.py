from django.urls import path, include
from . import views
app_name='credentials'

urlpatterns = [
    path('',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('logout/',views.logout,name='logout'),


]