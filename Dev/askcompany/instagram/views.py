from django.views.generic import ListView
from django.shortcuts import render
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
    })

def post_detail(request, pk):
    response = HttpResponse()
    response.write("Hello World")
    response.write("Hello World")
    response.write("Hello World")
    return response