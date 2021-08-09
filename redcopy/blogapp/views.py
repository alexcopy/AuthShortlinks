from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic

from .models import Post


class IndexPostsView(generic.ListView):
    model = Post
    context_object_name = "blog_posts"
    # queryset = BlogPosts.objects.get()
    template_name = 'blogapp/index.html'
