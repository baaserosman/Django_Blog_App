from django.shortcuts import render, redirect
from .models import Post
# from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from .forms import PostForm


def post_list(request):
    qs = Post.objects.filter(status='p')
    context = {
        'object_list' : qs
    }
    return render (request, "blog/post_list.html", context )

def post_create(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        # print(request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # messages.success(request, "Post created successfully!")
            return redirect("blog:list")
    context = {
        'form' : form
    }
    return render (request, "blog/post_create.html", context)