from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.user_profile, name='user-profile'),
    path('profile/edit/', views.user_profile_edit, name='user_profile_edit'),
]
