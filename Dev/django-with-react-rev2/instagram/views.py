from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.contrib import messages
from .models import Tag, Post

@login_required
def index(request):
    suggested_user_list = get_user_model().objects.all()\
                        .exclude(pk=request.user.pk)\
                        .exclude(pk__in=request.user.following_set.all())[:3] # 팔로우한 사람은 빼자! ORM 코드로 작성

    return render(request, "instagram/index.html",{
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

def user_page(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    post_list = Post.objects.filter(author=page_user)
    post_list_count = post_list.count() # 실제 데이터베이스에 count 쿼리를 던지게 된다.
    # len(post_list) # -> 이렇게 되면 post_list를 실제로 다 가져와서 메모리에 올려두고 개수를 세는 것이다.
    return render(request, "instagram/user_page.html", {
        "page_user": page_user,
        "post_list": post_list,
        "post_list_count": post_list_count,
    })