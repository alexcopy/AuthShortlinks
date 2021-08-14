from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.IndexPostsView.as_view(), name='indexblog'),
    path('myposts', views.IndexPostsViewByUser.as_view(), name='myposts'),
    path('tinymce/', include('tinymce.urls'), name='tiny'),
    path('add_post/', views.AddPostView.as_view(), name='addpost'),
    # path('delete/<url_id>/', views.delete_shorturl, name='delete_post'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_view'),
]
