from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.contrib import messages
from .models import Tag, Post

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
