# user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.custom_user_signup, name='user_signup'),
    # path('login/', views.CustomUserLoginSerializer, name='user_signup'),
    
    path('login/', views.custom_user_login, name='login'),
    path('logout/', views.custom_user_logout, name='logout'),
    path('get-user-info/', views.get_protected_data, name='get-user-info'),
    path('get_all_users/', views.get_all_users_with_roles, name='get_all_users'),
]

