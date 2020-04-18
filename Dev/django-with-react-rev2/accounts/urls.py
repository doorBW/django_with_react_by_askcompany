from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'), # /accounts/login/ => settings.LOGIN_URL 과 동일하다!
    path('logout/', views.logout, name='logout'),
    path('password_change/', views.password_change, name='password_change'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lay("password_change")),
    #                         name='password_change'),
    path('signup/', views.signup, name='signup'),
    path('edit/', views.profile_edit, name='profile_edit'),
]