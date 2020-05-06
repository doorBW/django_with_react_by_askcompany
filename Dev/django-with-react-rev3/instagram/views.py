from rest_framework import generics
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

# def post_list(request):
#     # -> 최소 2개 분기
#     pass

# def post_detail(request, pk):
#     # -> 최소 3개 분기
#     pass

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def dispatch(self, request, *args, **kwargs):
        print("request.body : ", request.body) #logger 사용 추천
        print("request.POST : ", request.POST)
        return super().dispatch(request, *args, **kwargs)


class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all() #filter(is_public=True)
    serializer_class = PostSerializer
