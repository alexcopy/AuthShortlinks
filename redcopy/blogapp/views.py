from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import forms
from .forms import PostForm
from .models import Post
from accounts import models


def get_author(user):
    qs = models.User.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

class IndexPostsView(generic.ListView):
    model = Post
    context_object_name = "blog_posts"
    # queryset = BlogPosts.objects.get()
    template_name = 'blogapp/index.html'


class PostListView(ListView):
    form = forms.PostForm
    model = Post
    template_name = 'blogapp/index.html'
    context_object_name = 'queryset'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        context['form'] = self.form
        return context

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.author = get_author(self.request.user)
        form.save()
        return redirect(reverse("post-detail", kwargs={
            'pk': form.instance.pk
        }))


def post_create(request):
    title = 'Create'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, "post_create.html", context)