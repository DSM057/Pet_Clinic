from turtle import settiltangle
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('<src>/', views.index),
    path('<src>/<h1>', views.index),
    path('today', views.last_booking, name='last_booking'),
    path('clients', views.last_clients , name = "last_client"),
    path('second', views.survey, name='second'),
    path('second/<src>/', views.survey),
    path('second/<src>/<h1>', views.survey),
    path('reg', views.reg, name='reg'),
    path('success', views.success, name='success'),
    path('failed', views.failed, name='failed'),
    path('regik', views.regik, name='regik'),
    path('regikfailed', views.regikfailed, name='regikfailed'),
    path('regiksuccess', views.regiksuccess, name='regiksuccess'),
    path('login', views.user_login, name='login'),
    path('loginfailed', views.login_failed, name='loginfailed'),
    path('logout', views.logoutUser, name='logout'),
    path('ajax' , views.load_more, name='ajax'),
    path('first_choise' , views.first_choise, name='first_choise'),

    


]