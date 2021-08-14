from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.text import slugify
from django.views import generic
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import forms
from .forms import PostForm
from .models import Post, PostView


class IndexPostsView(generic.ListView):
    model = Post
    context_object_name = "blog_posts"
    template_name = 'blogapp/index.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by("-timestamp")


class IndexPostsViewByUser(generic.ListView):
    model = Post
    context_object_name = "blog_posts"
    template_name = 'blogapp/index.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(created_by=self.request.user).order_by('-timestamp')


class AddPostView(generic.CreateView):
    model = Post
    template_name = 'blogapp/add_post.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.slug = slugify(form.instance.title)
        form.save()
        return redirect(reverse("post_view", kwargs={
            'pk': form.instance.pk
        }))

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponse('Unauthorized', status=401)
        return super(AddPostView, self).dispatch(request, *args, **kwargs)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogapp/post.html'
    context_object_name = 'post'

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'pk': post.pk
            }))


class PostListView(ListView):
    form = forms.PostForm
    model = Post
    template_name = 'blogapp/index.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        context['form'] = self.form
        return context


