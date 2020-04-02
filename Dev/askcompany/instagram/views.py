from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest, Http404
from .models import Post
from .forms import PostForm
# Create your views here.

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user # 현재 로그인 User Instance
            post.save()
            return redirect(post)
    else:
        form = PostForm()

    return render(request, 'instagram/post_form.html',{
        'form': form
    })

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 작성자 Check Tip
    if post.author != request.user:
        messages.error(request, '작성자만 수정할 수 있습니다.')
        return redirect(post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm(instance=post)

    return render(request, 'instagram/post_form.html',{
        'form': form
    })

# post_list = login_required(ListView.as_view(model=Post, paginate_by=10))

# @method_decorator(login_required, name='dispatch')
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 100

post_list = PostListView.as_view()

# @login_required
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
#         'post': post, # or 'object': post, 
#     })

# post_detail = DetailView.as_view(
#     model=Post,
#     queryset=Post.objects.filter(is_public=True))

class PostDetailView(DetailView):
    model = Post
    # queryset = Post.object.filter(is_public=True)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs

post_detail = PostDetailView.as_view()


# def archives_year(request,year):
#     return HttpResponse(f"{year}년 archives")

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)


post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)