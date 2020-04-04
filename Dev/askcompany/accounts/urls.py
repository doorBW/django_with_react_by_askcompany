from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = 'accounts' # URL Reverse에서 namespace역할을 하게 됩니다.

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]