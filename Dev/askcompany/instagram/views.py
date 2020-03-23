from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404
from .models import Post
# Create your views here.

post_list = ListView.as_view(model=Post)

# def post_list(request):
#     qs = Post.objects.all()
#     # request.GET
#     # request.POST
#     # request.FILES
#     q = request.GET.get('q', '') # 두번째 인자는 반환값이 없을 때의 반환값 설정하는 인자
#     if q:
#         qs = qs.filter(message__icontains=q)
#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,
#      })

# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     # try: 
#     #     post = Post.objects.get(pk=pk) # DoesNotExist 예외
#     # except Post.DoesNotExist:
#     #     raise Http404
#     return render(request, 'instagram/post_detail.html',{
#         'post': post,
#     })

post_detail = DetailView.as_view(model=Post)

def archives_year(request,year):
    return HttpResponse(f"{year}년 archives")
