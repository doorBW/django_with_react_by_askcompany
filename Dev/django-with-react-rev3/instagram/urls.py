from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet) # 2개의 URL 생성


urlpatterns = [
    path('public/', views.public_post_list),
    path('', include(router.urls)),
]