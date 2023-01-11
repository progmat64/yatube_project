from django.shortcuts import get_object_or_404, render

from .models import Group, Post
from .constants import NUMBER_OF_VALUES


def index(request):
    posts = Post.objects.all()[:NUMBER_OF_VALUES]
    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by("-pub_date")[:NUMBER_OF_VALUES]
    context = {
        "group": group,
        "posts": posts,
    }
    return render(request, "posts/group_list.html", context)
