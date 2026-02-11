from django.urls import path
from .import views 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('register',views.register_view,name='register'),
    path('protected',views.protected_view,name='protected'),
   path('logout/', views.logout_view, name='logout'),
    path('user_list_view/', views.user_list_view, name='list'),
]

