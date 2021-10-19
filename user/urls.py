from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.user_profile, name='user-profile'),
    path('profile/edit/', views.user_profile_edit, name='user_profile_edit'),

    path('reset_password/', auth_view.PasswordResetView.as_view(template_name="auth/pass_reset/password_reset.html"), name='reset_password'),
    
    path('reset_password_sent/', auth_view.PasswordResetDoneView.as_view(template_name="auth/pass_reset/password_reset_sent.html"), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name="auth/pass_reset/password_reset_form.html"), name='password_reset_confirm'),
    
    path('reset_password_complete/', auth_view.PasswordResetCompleteView.as_view(template_name="auth/pass_reset/password_reset_done.html"), name='password_reset_complete'),

]
