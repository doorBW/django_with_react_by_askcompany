"""askcompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView

class RootView(TemplateView):
    template_name = 'root.html'

urlpatterns = [
    path('', RedirectView.as_view(
        # url='/instagram/'
        pattern_name='instagram:post_list',
        ), name='root'),
    # path('', RootView.as_view(), name='root'),
    # path('', TemplateView.as_view(template_name='root.html'), name='root'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog1/', include('blog1.urls')),
    path('instagram/', include('instagram.urls')),
]

if settings.DEBUG:
    # settings.MEDIA_URL
    # settings.MEDIA_ROOT
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
