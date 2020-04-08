from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'accounts' # URL Reverse에서 namespace역할을 하게 됩니다.

urlpatterns = [
    path('login/', LoginView.as_view(
        # form_class=AuthenticationForm,
        form_class=LoginForm,
        template_name='accounts/login_form.html'
        ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('signup/', views.signup, name='signup'),
    
]