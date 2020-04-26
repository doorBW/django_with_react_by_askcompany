from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.contrib import messages
from .models import Tag, Post

@login_required
def index(request):
    timesince = timezone.now() - timedelta(days=3)
    post_list = Post.objects.all()\
                .filter( # .filter(author__in=request.user.following_set.all())
                    Q(author=request.user) | # OR 조건
                    Q(author__in=request.user.following_set.all())
                )\
                .filter(
                    created_at__gte=timesince # graeter than equal
                )
    suggested_user_list = get_user_model().objects.all()\
                        .exclude(pk=request.user.pk)\
                        .exclude(pk__in=request.user.following_set.all())[:3] # 팔로우한 사람은 빼자! ORM 코드로 작성

    return render(request, "instagram/index.html",{
        "post_list": post_list,
        "suggested_user_list": suggested_user_list,
    })

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # 아래 태그 추가를 하려면 일단 post가 저장되어야 한다.
            # ManyToManyField는 우선 pk값이 존재해야함.
            post.tag_set.add(*post.extract_tag_list())
            
            messages.success(request, "포스팅을 저장했습니다.")
            return redirect(post) # TODO: get_absolute_url 활용
    else:
        form = PostForm()

    return render(request, "instagram/post_form.html", {
        "form": form,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "instagram/post_detail.html", {
        "post": post,
    })

@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # TODO: like 처리 필요
    post.like_user_set.add(request.user)

    messages.success(request, f"포스팅#{post.pk}를 좋아합니다.")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    return redirect(redirect_url)

@login_required
def post_unlike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # TODO: unlike 처리 필요
    post.like_user_set.remove(request.user)

    messages.success(request, f"포스팅#{post.pk} 좋아요를 취소합니다.")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    return redirect(redirect_url)

@login_required
def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(comment.post)
    else:
        form = CommentForm()
    return render(request, "instagram/comment_form.html", {
        "form": form,
    })


def user_page(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    post_list = Post.objects.filter(author=page_user)
    post_list_count = post_list.count() # 실제 데이터베이스에 count 쿼리를 던지게 된다.
    # len(post_list) # -> 이렇게 되면 post_list를 실제로 다 가져와서 메모리에 올려두고 개수를 세는 것이다.

    if request.user.is_authenticated:
        is_follow = request.user.following_set.filter(pk=page_user.pk).exists()
    else:
        is_follow = False

    return render(request, "instagram/user_page.html", {
        "page_user": page_user,
        "post_list": post_list,
        "post_list_count": post_list_count,
        "is_follow": is_follow,
    })