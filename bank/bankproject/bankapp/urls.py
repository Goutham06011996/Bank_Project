from . import views
from django.urls import path


app_name='bankapp'


urlpatterns = [
    path('',views.index,name='index'),
    path('application_form/', views.application_form, name='application_form'),
    path('form/', views.form, name='form'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),


]




