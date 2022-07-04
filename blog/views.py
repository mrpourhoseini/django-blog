from django.shortcuts import render, get_object_or_404
from blog.models import Post


# Create your views here.
def home(request):
    posts = Post.objects.filter(status=Post.StatusChoices.PUBLISHED)
    context = {
        'posts': posts,
    }
    return render(request, "pages/index.html", context)


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, "pages/detail.html", context)
