from django.contrib.auth.views import LoginView
from django.urls import path
app_name = 'accounts' # URL Reverse에서 namespace역할을 하게 됩니다.

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
]